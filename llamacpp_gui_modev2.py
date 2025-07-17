import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import subprocess
import threading
import requests
import time
import os

LLAMA_EXE = "llama-server.exe"
LLAMA_PORT = 5001
LLAMA_API = f"http://127.0.0.1:{LLAMA_PORT}/completion"

model_loaded = False
llama_process = None

LOG_FILE = "llama_log.txt"
ERR_FILE = "llama_error.txt"

presets = {
    "Default": {"temperature": 0.7,  "top_p": 0.95, "max_tokens": 200},
    "Coding":  {"temperature": 0.2,  "top_p": 0.90, "max_tokens": 300},
    "Roleplay":{"temperature": 0.95, "top_p": 0.98, "max_tokens": 400},
}

def wait_until_ready(timeout=60):
    global model_loaded
    start = time.time()
    for _ in range(timeout):
        try:
            r = requests.post(LLAMA_API, json={"prompt": "Hello", "n_predict": 5}, timeout=5)
            if r.status_code == 200:
                model_loaded = True
                return time.time() - start
        except:
            pass
        time.sleep(1)
    return -1

def stream_output(process):
    with open(LOG_FILE, "a", encoding="utf-8") as log, open(ERR_FILE, "a", encoding="utf-8") as errlog:
        if process.stderr is None:
            log.write("[ERROR] stderr stream not available.\n")
            return
        for line in process.stderr:
            decoded = line.decode(errors="ignore")
            log.write(decoded)
            errlog.write(decoded)
            tab_chat.insert(tk.END, f"[LOG] {decoded}")
            tab_chat.see(tk.END)

def start_llama(model_path):
    global llama_process
    tab_chat.insert(tk.END, "\n[⏳] Menjalankan llama-server...\n")

    if not os.path.isfile(LLAMA_EXE) or not os.path.isfile(model_path):
        messagebox.showerror("Error", "llama-server.exe atau model GGUF tidak ditemukan.")
        return

    try:
        llama_process = subprocess.Popen([
            LLAMA_EXE, "--model", model_path,
            "--port", str(LLAMA_PORT),
            "--ctx-size", "2048",
        ], stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
        threading.Thread(target=stream_output, args=(llama_process,), daemon=True).start()

        tab_chat.insert(tk.END, "[⏳] Menunggu model siap...\n")
        load_time = wait_until_ready()

        # Jika proses ternyata mati sebelum siap
        if llama_process.poll() is not None:
            tab_chat.insert(tk.END, "[❌] Gagal memuat model. Proses keluar lebih awal.\n")
            with open(ERR_FILE, "a") as f:
                f.write("[FATAL] Model gagal start. Periksa file .gguf atau resource Anda.\n")
            messagebox.showerror("Gagal", "Model tidak bisa dijalankan. Cek file error log.")
            return

        tab_chat.insert(tk.END, f"[✅] Model siap dalam {load_time:.2f}s\n" if load_time > 0 else "[❌] Gagal memuat model (timeout).\n")

    except Exception as e:
        messagebox.showerror("Error", str(e))
        with open(ERR_FILE, "a") as f:
            f.write(f"[EXCEPTION] {e}\n")

def load_model():
    path = filedialog.askopenfilename(title="Pilih Model GGUF", filetypes=[("GGUF files","*.gguf")])
    if path:
        threading.Thread(target=start_llama, args=(path,), daemon=True).start()

def apply_preset(event=None):
    p = presets.get(preset_combo.get(), presets["Default"])
    entry_temp.delete(0, tk.END); entry_temp.insert(0, str(p["temperature"]))
    entry_topp.delete(0, tk.END); entry_topp.insert(0, str(p["top_p"]))
    entry_max_tokens.delete(0, tk.END); entry_max_tokens.insert(0, str(p["max_tokens"]))

def send_message():
    if not model_loaded:
        messagebox.showwarning("Tunggu", "Model belum siap.")
        return
    prompt = tab_input.get("1.0", tk.END).strip()
    if not prompt: return
    try:
        data = {
            "prompt": prompt,
            "temperature": float(entry_temp.get()),
            "top_p": float(entry_topp.get()),
            "n_predict": int(entry_max_tokens.get()),
            "stop": ["<|endoftext|>","You:"]
        }
    except Exception as e:
        messagebox.showerror("Input Error", str(e)); return

    tab_chat.insert(tk.END, f"\n🧑 You: {prompt}\n")
    tab_input.delete("1.0", tk.END)
    try:
        r = requests.post(LLAMA_API, json=data, timeout=120)
        r.raise_for_status()
        tab_chat.insert(tk.END, f"🤖 AI: {r.json().get('content','').strip()}\n")
    except Exception as e:
        tab_chat.insert(tk.END, f"[ERROR] {e}\n")
        with open(ERR_FILE, "a") as f:
            f.write(f"[SEND ERROR] {e}\n")

def upload_file_to_input():
    path = filedialog.askopenfilename(title="Pilih File", filetypes=[("Text","*.txt"),("All Files","*.*")])
    if not path: return
    try:
        with open(path,"r",encoding="utf-8") as f: content = f.read()
    except:
        with open(path,"r",encoding="latin1",errors="ignore") as f: content = f.read()
    tab_input.insert(tk.END, f"\n[📎] Konten file:\n{content[:1000]}...\n")

# GUI
root = tk.Tk()
root.title("LLaMA.cpp Server GUI")
root.geometry("900x800")

notebook = ttk.Notebook(root)
frame_main = ttk.Frame(notebook); frame_settings = ttk.Frame(notebook)
notebook.add(frame_main, text="💬 Chat"); notebook.add(frame_settings, text="⚙️ Pengaturan")
notebook.pack(expand=True, fill="both")

frame_top = ttk.Frame(frame_main); frame_top.pack(pady=5)
ttk.Button(frame_top, text="📂 Muat Model", command=load_model).pack(side="left", padx=5)
preset_combo = ttk.Combobox(frame_top, values=list(presets.keys()), width=15)
preset_combo.set("Default"); preset_combo.bind("<<ComboboxSelected>>", apply_preset); preset_combo.pack(side="left")

tab_chat = scrolledtext.ScrolledText(frame_main, wrap=tk.WORD, height=25, width=120)
tab_chat.pack(padx=10, pady=10); tab_chat.insert(tk.END, "💬 Selamat datang!\n")

tab_input = tk.Text(frame_main, height=4, width=120); tab_input.pack(padx=10, pady=5)
frame_actions = ttk.Frame(frame_main); frame_actions.pack(pady=5)
ttk.Button(frame_actions, text="📨 Kirim Chat", command=send_message).pack(side="left", padx=5)
ttk.Button(frame_actions, text="📎 Ambil File", command=upload_file_to_input).pack(side="left", padx=5)

tk.Label(frame_settings, text="Temperature:").grid(row=0,column=0); entry_temp = tk.Entry(frame_settings,width=5); entry_temp.insert(0,"0.7"); entry_temp.grid(row=0,column=1)
tk.Label(frame_settings, text="Top-p:").grid(row=0,column=2); entry_topp = tk.Entry(frame_settings,width=5); entry_topp.insert(0,"0.95"); entry_topp.grid(row=0,column=3)
tk.Label(frame_settings, text="Max Tokens:").grid(row=0,column=4); entry_max_tokens = tk.Entry(frame_settings,width=5); entry_max_tokens.insert(0,"200"); entry_max_tokens.grid(row=0,column=5)

root.mainloop()