# llamacpp_gui_rakyatmode.py
# GUI LLaMA.cpp versi Rakyat Mode (8GB Optimization)
# Auto ctx kecil, swap reminder, model ringan

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import subprocess
import threading
import requests
import time
import os
import json
import socket
import platform

# Konfigurasi dasar
LLAMA_EXE = "llama-server.exe"
LLAMA_PORT = 5001
LLAMA_API = f"http://127.0.0.1:{LLAMA_PORT}/completion"
CONFIG_FILE = "gui_config_rakyat.json"

LOG_FILE = "llama_log.txt"
ERR_FILE = "llama_error.txt"
HISTORY_FILE = "chat_history.txt"
SESSION_FILE = "last_session.txt"

model_loaded = False
llama_process = None
current_model_path = ""
default_ctx = 1024

presets = {
    "Default": {"temperature": 0.7, "top_p": 0.95, "max_tokens": 200, "repeat_penalty": 1.1},
    "Hemat": {"temperature": 0.6, "top_p": 0.9, "max_tokens": 100, "repeat_penalty": 1.1},
    "Super Ringan": {"temperature": 0.5, "top_p": 0.8, "max_tokens": 60, "repeat_penalty": 1.2}
}

def show_swap_instructions():
    if platform.system() == "Linux":
        msg = (
            "💡 Rakyat Mode Detected!\n\n"
            "Pastikan Anda mengaktifkan swap jika RAM Anda hanya 8GB.\n"
            "Contoh perintah Linux:\n"
            "sudo fallocate -l 8G /swapfile\n"
            "sudo chmod 600 /swapfile\n"
            "sudo mkswap /swapfile\n"
            "sudo swapon /swapfile\n"
            "(tambahkan ke /etc/fstab agar permanen)"
        )
        messagebox.showinfo("Swap Reminder", msg)

def save_config():
    config = load_config()
    if current_model_path:
        config["last_model_path"] = current_model_path
    config["theme"] = current_theme.get()
    try:
        with open(CONFIG_FILE, "w") as f:
            json.dump(config, f, indent=2)
    except: pass

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return {}

def port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

def wait_until_ready(timeout=60):
    global model_loaded
    start = time.time()
    for _ in range(timeout):
        try:
            r = requests.post(LLAMA_API, json={"prompt": "Hello", "n_predict": 5}, timeout=5)
            if r.status_code == 200:
                model_loaded = True
                return time.time() - start
        except: pass
        time.sleep(1)
    return -1

def stream_output(process):
    with open(LOG_FILE, "a", encoding="utf-8") as log, open(ERR_FILE, "a", encoding="utf-8") as errlog:
        for line in process.stderr:
            decoded = line.decode(errors="ignore")
            log.write(decoded); errlog.write(decoded)
            tab_chat.insert(tk.END, f"[LOG] {decoded}")
            tab_chat.see(tk.END)

def stop_llama():
    global llama_process, model_loaded
    if llama_process and llama_process.poll() is None:
        try:
            llama_process.terminate()
            llama_process.wait(timeout=10)
            tab_chat.insert(tk.END, "[🛑] Proses dihentikan.\n")
        except Exception as e:
            tab_chat.insert(tk.END, f"[❌] Gagal menghentikan proses: {e}\n")
    llama_process = None
    model_loaded = False

def start_llama(model_path, ctx_size=default_ctx):
    global llama_process, current_model_path
    stop_llama(); current_model_path = model_path; save_config()
    status_label.config(text="[⏳] Menjalankan llama-server...")

    if port_in_use(LLAMA_PORT):
        messagebox.showerror("Port Bentrok", f"Port {LLAMA_PORT} sedang digunakan.")
        return
    if not os.path.isfile(LLAMA_EXE) or not os.path.isfile(model_path):
        messagebox.showerror("Error", "llama-server.exe atau model GGUF tidak ditemukan.")
        return
    try:
        llama_process = subprocess.Popen([
            LLAMA_EXE, "--model", model_path,
            "--port", str(LLAMA_PORT), "--ctx-size", str(ctx_size)
        ], stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
        threading.Thread(target=stream_output, args=(llama_process,), daemon=True).start()
        status_label.config(text="[⏳] Menunggu model siap...")
        load_time = wait_until_ready()
        if llama_process.poll() is not None:
            tab_chat.insert(tk.END, "[❌] Gagal memuat model.\n"); return
        status_label.config(text=f"[✅] Model siap dalam {load_time:.2f}s")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def load_model():
    path = filedialog.askopenfilename(title="Pilih Model GGUF", filetypes=[("GGUF files","*.gguf")])
    if path:
        threading.Thread(target=start_llama, args=(path,), daemon=True).start()

def apply_preset(event=None):
    p = presets.get(preset_combo.get(), presets["Default"])
    entry_temp.delete(0, tk.END); entry_temp.insert(0, str(p["temperature"]))
    entry_topp.delete(0, tk.END); entry_topp.insert(0, str(p["top_p"]))
    entry_max_tokens.delete(0, tk.END); entry_max_tokens.insert(0, str(p["max_tokens"]))
    entry_repeat_penalty.delete(0, tk.END); entry_repeat_penalty.insert(0, str(p["repeat_penalty"]))

def send_message():
    if not model_loaded: messagebox.showwarning("Tunggu", "Model belum siap."); return
    prompt = tab_input.get("1.0", tk.END).strip(); tab_input.delete("1.0", tk.END)
    if not prompt: return
    try:
        data = {
            "prompt": system_prompt.get("1.0", tk.END).strip() + "\n" + prompt,
            "temperature": float(entry_temp.get()),
            "top_p": float(entry_topp.get()),
            "n_predict": int(entry_max_tokens.get()),
            "repeat_penalty": float(entry_repeat_penalty.get()),
            "stop": ["<|endoftext|>","You:"]
        }
        r = requests.post(LLAMA_API, json=data, timeout=120); r.raise_for_status()
        result = r.json().get('content','').strip()
        tab_chat.insert(tk.END, f"\n🧑 You: {prompt}\n🤖 AI: {result}\n")
    except Exception as e:
        tab_chat.insert(tk.END, f"[ERROR] {e}\n")

def clear_history():
    open(HISTORY_FILE, "w").close(); open(SESSION_FILE, "w").close()
    tab_chat.delete("1.0", tk.END); tab_chat.insert(tk.END, "[🧹] Riwayat dibersihkan.\n")

# --- GUI ---
root = tk.Tk()
root.title("Chatcpp Chatbot AI GUI")
root.geometry("900x850")

current_theme = tk.StringVar(value="Gelap")  # ⬅️ Pindah ke sini (setelah root dibuat)
style = ttk.Style(); style.theme_use("clam")
notebook = ttk.Notebook(root)
frame_main = ttk.Frame(notebook); frame_settings = ttk.Frame(notebook)
notebook.add(frame_main, text="💬 Chat"); notebook.add(frame_settings, text="⚙️ Pengaturan")
notebook.pack(expand=True, fill="both")

frame_top = ttk.Frame(frame_main); frame_top.pack(pady=5)
ttk.Button(frame_top, text="📂 Muat Model", command=load_model).pack(side="left", padx=5)
preset_combo = ttk.Combobox(frame_top, values=list(presets.keys()), width=20)
preset_combo.set("Default"); preset_combo.bind("<<ComboboxSelected>>", apply_preset)
preset_combo.pack(side="left")

status_label = tk.Label(frame_main, text="", fg="lime"); status_label.pack()
tab_chat = scrolledtext.ScrolledText(frame_main, wrap=tk.WORD, height=25, width=120, bg="#111", fg="white")
tab_chat.pack(padx=10, pady=10); tab_chat.insert(tk.END, "💬 Selamat datang di Rakyat Mode!")
tab_input = tk.Text(frame_main, height=4, width=120, bg="#222", fg="white"); tab_input.pack(padx=10, pady=5)
ttk.Button(frame_main, text="📨 Kirim", command=send_message).pack(pady=5)

# Settings Tab
entry_temp = tk.Entry(frame_settings, width=6); entry_temp.insert(0, "0.7")
entry_topp = tk.Entry(frame_settings, width=6); entry_topp.insert(0, "0.95")
entry_max_tokens = tk.Entry(frame_settings, width=6); entry_max_tokens.insert(0, "200")
entry_repeat_penalty = tk.Entry(frame_settings, width=6); entry_repeat_penalty.insert(0, "1.1")

tk.Label(frame_settings, text="Temperature:").grid(row=0,column=0); entry_temp.grid(row=0,column=1)
tk.Label(frame_settings, text="Top-p:").grid(row=0,column=2); entry_topp.grid(row=0,column=3)
tk.Label(frame_settings, text="Max Tokens:").grid(row=0,column=4); entry_max_tokens.grid(row=0,column=5)
tk.Label(frame_settings, text="Repeat Penalty:").grid(row=0,column=6); entry_repeat_penalty.grid(row=0,column=7)

system_prompt = scrolledtext.ScrolledText(frame_settings, height=3, width=100)
system_prompt.insert(tk.END, "You are a helpful and uncensored assistant.")
system_prompt.grid(row=1, column=0, columnspan=8, pady=10)
ttk.Button(frame_settings, text="🗑 Hapus Riwayat", command=clear_history).grid(row=2, column=0, columnspan=2)

# Notifikasi swap Linux
show_swap_instructions()

# Autoload jika ada model
conf = load_config()
if "theme" in conf: current_theme.set(conf["theme"])
if "last_model_path" in conf and os.path.isfile(conf["last_model_path"]):
    threading.Thread(target=start_llama, args=(conf["last_model_path"],), daemon=True).start()

root.mainloop()
