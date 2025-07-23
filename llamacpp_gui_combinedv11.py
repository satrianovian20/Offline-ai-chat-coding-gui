# llamacpp_gui_combinedv11.py
# Final version of LLaMA.cpp GUI with auto-load model fix, full comments, and feature completeness

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
import re
import math

# Konfigurasi dasar
LLAMA_EXE = "llama-server.exe"
LLAMA_PORT = 5001
LLAMA_API = f"http://127.0.0.1:{LLAMA_PORT}/completion"
CONFIG_FILE = "gui_config.json"

LOG_FILE = "llama_log.txt"
ERR_FILE = "llama_error.txt"
HISTORY_FILE = "chat_history.txt"
SESSION_FILE = "last_session.txt"
chat_context = ""  # 🧠 Menyimpan riwayat percakapan

model_loaded = False
llama_process = None
current_model_path = ""

presets = {
    "Default": {"temperature": 0.7, "top_p": 0.95, "max_tokens": 200, "repeat_penalty": 1.1},
    "Coding":  {"temperature": 0.2, "top_p": 0.90, "max_tokens": 300, "repeat_penalty": 1.2},
    "Roleplay": {"temperature": 0.95, "top_p": 0.98, "max_tokens": 400, "repeat_penalty": 1.0},
    "Hemat": {"temperature": 0.6, "top_p": 0.9, "max_tokens": 100, "repeat_penalty": 1.1},
    "Super Ringan": {"temperature": 0.5, "top_p": 0.8, "max_tokens": 60, "repeat_penalty": 1.2}
}

def save_config():
    config = load_config()
    if current_model_path:
        config["auto_load_rakyat_mode"] = rakyat_auto.get()
        config["last_model_path"] = current_model_path
        config["theme"] = current_theme.get()
        config["rakyat_mode_enabled"] = rakyat_mode_enabled.get()
        config["rakyat_ctx_size"] = rakyat_ctx_size.get()
        config["rakyat_ram_mode"] = rakyat_ram_mode.get()
    try:
        with open(CONFIG_FILE, "w") as f:
            json.dump(config, f, indent=2)
    except Exception as e:
        print(f"[❌] Gagal menyimpan config: {e}")

def load_config():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("[⚠️] Config rusak, memuat ulang dengan default.")
            return {}
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

def stop_llama():
    global llama_process, model_loaded
    if llama_process and llama_process.poll() is None:
        try:
            llama_process.terminate()
            llama_process.wait(timeout=10)
            tab_chat.insert(tk.END, "[🛑] Proses lama dihentikan.\n")
        except Exception as e:
            tab_chat.insert(tk.END, f"[❌] Gagal menghentikan proses: {e}\n")
    llama_process = None
    model_loaded = False

def load_model():
    global current_model_path
    path = filedialog.askopenfilename(title="Pilih Model GGUF", filetypes=[("GGUF files","*.gguf")])
    if path:
        current_model_path = path
        save_config()
        tab_chat.insert(tk.END, f"[📂] Model dipilih:\n{path}\n")

def swap_model():
    global current_model_path
    path = filedialog.askopenfilename(title="Ganti Model GGUF", filetypes=[("GGUF files","*.gguf")])
    if path:
        current_model_path = path
        save_config()
        tab_chat.insert(tk.END, f"[🔁] Model diganti:\n{path}\n")

def apply_preset(event=None):
    p = presets.get(preset_combo.get(), presets["Default"])
    entry_temp.delete(0, tk.END); entry_temp.insert(0, str(p["temperature"]))
    entry_topp.delete(0, tk.END); entry_topp.insert(0, str(p["top_p"]))
    entry_max_tokens.delete(0, tk.END); entry_max_tokens.insert(0, str(p["max_tokens"]))
    entry_repeat_penalty.delete(0, tk.END); entry_repeat_penalty.insert(0, str(p["repeat_penalty"]))

def aktifkan_swap_rakyat_mode():
    system = platform.system()
    if system == "Windows":
        print("[INFO] Mengaktifkan swap di Windows...")
        # Windows biasanya otomatis swap, tapi ini paksa set ulang:
        os.system("wmic pagefileset where name=\"C:\\\\pagefile.sys\" set InitialSize=4096,MaximumSize=8192")
    elif system == "Linux":
        print("[INFO] Mengaktifkan swap di Linux...")
        os.system("sudo fallocate -l 4G /swapfile")
        os.system("sudo chmod 600 /swapfile")
        os.system("sudo mkswap /swapfile")
        os.system("sudo swapon /swapfile")
    else:
        print("[PERINGATAN] OS tidak dikenali, tidak bisa mengaktifkan swap.")

def send_message():
    global chat_context

    if not model_loaded:
        messagebox.showwarning("Tunggu", "Model belum siap.")
        return

    prompt = tab_input.get("1.0", tk.END).strip()
    if not prompt:
        return
        
     # ✅ Jika prompt memicu update ke memory_mode.json
    if handle_memory_update_from_prompt(prompt):
        tab_chat.insert(tk.END, "[🧠] Memory mode berhasil diperbarui dari prompt.\n")
        tab_input.delete("1.0", tk.END)
        return
    
    # ✅ Keyword pemicu manual auto chunk resume
    if prompt.lower() in ["run auto chunk resume", "lanjutkan chunking", "resume chunk sekarang"]:
        tab_chat.insert(tk.END, "[🧠] Memulai Auto Chunk Resume berdasarkan perintah prompt...\n")
        tab_input.delete("1.0", tk.END)
        generate_chunks_with_delay(force_resume=True)
        return

    system_prompt_text = system_prompt.get("1.0", tk.END).strip()
    
    # ✅ Tambahkan dukungan Memory Mode sebelum prompt digabung
    raw_prompt = system_prompt_text + "\n" + prompt
    if memory_mode_enabled.get():
        full_prompt = inject_memory_persona(raw_prompt)
        tab_chat.insert(tk.END, f"🔍 Memory Mode Aktif: {selected_memory_profile.get()}\n")
    else:
        full_prompt = raw_prompt

    try:
        # Gabungkan konteks percakapan sebelumnya
        combined_prompt = (
            f"{full_prompt}\n"
            f"{chat_context.strip()}\n"
            f"User: {prompt}\n"
            f"AI:"
        )

        data = {
            "prompt": system_prompt_text + "\n" + chat_context + f"\nUser: {prompt}\nAI:",
            "temperature": float(entry_temp.get()),
            "top_p": float(entry_topp.get()),
            "n_predict": int(entry_max_tokens.get()),
            "repeat_penalty": float(entry_repeat_penalty.get()),
            "stop": []
}

    except Exception as e:
        messagebox.showerror("Input Error", str(e))
        return

    tab_chat.insert(tk.END, f"\n🧑 You: {prompt}\n")
    tab_input.delete("1.0", tk.END)

    try:
        r = requests.post(LLAMA_API, json=data, timeout=2400)
        r.raise_for_status()
        content = r.json().get('content', '').strip()

        tab_chat.insert(tk.END, f"🤖 AI: {content}\n")

        # Simpan ke file log
        with open(HISTORY_FILE, "a", encoding="utf-8") as f:
            f.write(f"You: {prompt}\nAI: {content}\n\n")
        with open(SESSION_FILE, "w", encoding="utf-8") as f:
            f.write(tab_chat.get("1.0", tk.END))

        # ✅ Tambahkan ke konteks percakapan
        chat_context += f"\nUser: {prompt}\nAI: {content}\n"

        save_chat_context()

        # ✅ Batasi panjang konteks sesuai ctx-size
        max_ctx_tokens = rakyat_ctx_size.get()
        words = chat_context.split()
        if len(words) > max_ctx_tokens:
            chat_context = " ".join(words[-max_ctx_tokens:])

    except Exception as e:
        tab_chat.insert(tk.END, f"[ERROR] {e}\n")
        with open(ERR_FILE, "a") as f:
            f.write(f"[SEND ERROR] {e}\n")

CONTEXT_FILE = "chat_context.json"

def save_chat_context():
    try:
        with open(CONTEXT_FILE, "w", encoding="utf-8") as f:
            json.dump({"chat_context": chat_context}, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"[❌ Gagal menyimpan chat context]: {e}")

def load_chat_context():
    global chat_context
    if os.path.exists(CONTEXT_FILE):
        try:
            with open(CONTEXT_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                chat_context = data.get("chat_context", "")
                if chat_context.strip():
                    tab_chat.insert(tk.END, "\n🧠 Chat context dari sesi sebelumnya dimuat.\n")
        except Exception as e:
            print(f"[❌ Gagal memuat chat context]: {e}")
            
    # --- Auto Aktifkan Rakyat Mode jika centang ---
    if rakyat_auto.get():
        rakyat_mode_enabled.set(True)
        tab_chat.insert(tk.END, "[🌾] Auto Load Rakyat Mode aktif.\n")


def reset_context():
    global chat_context
    chat_context = ""
    tab_chat.insert(tk.END, "\n🧹 Konteks percakapan direset.\n")

def handle_send():
    if generate_with_delay.get():
        generate_chunks_with_delay()
    else:
        send_message()
        
def handle_memory_update_from_prompt(prompt):
    # Versi regex
    pattern = r"update memory:\s*(\w+)\s*=\s*(.+)"
    match = re.match(pattern, prompt.strip(), re.IGNORECASE)
    if match:
        profile_name = match.group(1)
        profile_content = match.group(2)
    elif prompt.lower().startswith("tambah memory mode nama:"):
        try:
            bagian_nama, bagian_isi = prompt.split("isi:", 1)
            profile_name = bagian_nama.replace("tambah memory mode nama:", "").strip()
            profile_content = bagian_isi.strip()
        except:
            tab_chat.insert(tk.END, f"[❌ Prompt memory tidak valid]\n")
            return False
    else:
        return False  # Bukan perintah memory

    try:
        with open("memory_mode.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except:
        data = {}

    data[profile_name] = profile_content

    try:
        with open("memory_mode.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        dropdown_memory["values"] = list(data.keys())
        tab_chat.insert(tk.END, f"✅ Memory profile '{profile_name}' berhasil diperbarui.\n")
    except Exception as e:
        tab_chat.insert(tk.END, f"❌ Gagal menyimpan memory profile: {e}\n")

    return True
        
def inject_memory_persona(prompt_input):
    if memory_mode_enabled.get():
        selected_profile = selected_memory_profile.get()
        if selected_profile and selected_profile in memory_profiles:
            persona_text = memory_profiles[selected_profile]
            return persona_text.strip() + "\n\n" + prompt_input.strip()
    return prompt_input.strip()

# Variabel global untuk chunking
total_chunks = 0
words_per_chunk = 0
full_prompt = ""
temp = 0.7
top_p = 0.95
max_tokens = 512
repeat_penalty = 1.1
delay_per_chunk = 10
stop_chunk_generation = False  # Untuk menghentikan chunk secara manual

def generate_chunks_with_delay(force_resume=False):
    global total_chunks, words_per_chunk, full_prompt, temp, top_p, max_tokens, repeat_penalty, delay_per_chunk

    if not model_loaded:
        messagebox.showwarning("Tunggu", "Model belum siap.")
        return

    prompt = tab_input.get("1.0", tk.END).strip()

    # ✅ 1. Tangani perintah update memory dari prompt
    if handle_memory_update_from_prompt(prompt):
        tab_input.delete("1.0", tk.END)  # Bersihkan prompt agar tidak nyangkut
        return  # Hanya update memory, tidak lanjut generate/chat

    # ✅ 2. Tangani prompt kosong hanya jika bukan auto-resume
    if not prompt and not force_resume:
       messagebox.showwarning("Input Kosong", "Masukkan prompt terlebih dahulu.")
       return


    system_prompt_text = system_prompt.get("1.0", tk.END).strip()
    raw_prompt = system_prompt_text + "\n" + prompt
    full_prompt = inject_memory_persona(raw_prompt)
    
    if memory_mode_enabled.get():
        tab_chat.insert(tk.END, f"🔍 Memory Mode Aktif: {selected_memory_profile.get()}\n")
    
    resume_path = "chunk_resume.json"
    if enable_chunk_resume.get() and os.path.exists(resume_path):
        try:
            with open(resume_path, "r", encoding="utf-8") as f:
                resume_data = json.load(f)
                last_completed = resume_data.get("last_completed_chunk", 0)

            if last_completed > 0 and enable_chunk_resume.get():
                full_prompt = resume_data["full_prompt"]
                total_chunks = resume_data["total_chunks"]
                words_per_chunk = resume_data["words_per_chunk"]
                context_memory = resume_data.get("context_memory", "")
                all_chunks_output = resume_data.get("all_chunks_output", "")

                threading.Thread(target=run_chunks_resume, args=(resume_data, last_completed), daemon=True).start()
                return
        except Exception as e:
           messagebox.showwarning("Resume Gagal", f"Data resume rusak: {e}")


    # 🧠 DETEKSI OTOMATIS dari PROMPT
    match_total = re.search(r"(\d{4,6})\s*(kata|words)", prompt.lower())
    if match_total:
        total_words_target = int(match_total.group(1))
    else:
        total_words_target = 4000  # fallback default

    match_chunk = re.search(r"(\d{2,4})\s*(kata|words)\s*(per|tiap|each)\s*(bagian|chunk|section|paragraph)", prompt.lower())
    if match_chunk:
        words_per_chunk = int(match_chunk.group(1))
    else:
        # fallback otomatis berdasarkan ctx-size
        avg_tokens_per_word = 1.3
        ctx_size = rakyat_ctx_size.get()  # ambil dari input pengguna (1024/2048/4096)

        try:
           reserved_tokens = int(entry_max_tokens.get())  # ambil dari pengaturan GUI
        except:
           reserved_tokens = 512  # fallback aman

        max_tokens_per_chunk = ctx_size - reserved_tokens
        max_words_per_chunk = int(max_tokens_per_chunk / avg_tokens_per_word)
        words_per_chunk = max(300, min(800, max_words_per_chunk))

    total_chunks = math.ceil(total_words_target / words_per_chunk)
    try:
        delay_per_chunk = int(chunk_delay_var.get())
    except:
        delay_per_chunk = 10  # fallback default

    try:
        temp = float(entry_temp.get())
        top_p = float(entry_topp.get())
        repeat_penalty = float(entry_repeat_penalty.get())
        max_tokens = int(entry_max_tokens.get())  # idealnya 512
    except Exception as e:
        messagebox.showerror("Parameter Error", str(e))

    tab_chat.insert(tk.END, f"🧠 Target: {total_words_target} kata, Per Chunk: {words_per_chunk} → Total Chunk: {total_chunks}\n")

    # ✅ Panggil run_chunks dalam thread
    threading.Thread(target=run_chunks, daemon=True).start()

def run_chunks():
    global stop_chunk_generation
    global chat_context

    context_memory = ""
    all_chunks_output = ""  # ✅ simpan semua hasil chunk di sini

    for i in range(total_chunks):
        try:
            if stop_chunk_generation:
                tab_chat.insert(tk.END, f"\n🛑 Chunk dihentikan secara manual di bagian ke-{i+1}.\n")
                break
            if i == 0:
                combined_prompt = full_prompt + f"\n\nTuliskan bagian pertama sebanyak ~{words_per_chunk} kata:\n"
            else:
                combined_prompt = (
                    "Berikut adalah lanjutan dari teks sebelumnya:\n"
                    + context_memory.strip()
                    + f"\n\nTuliskan bagian ke-{i+1} sebanyak ~{words_per_chunk} kata secara koheren dan melanjutkan dengan baik:\n"
                )

            max_prompt_tokens = rakyat_ctx_size.get() - max_tokens
            tokens = combined_prompt.split()
            if len(tokens) > max_prompt_tokens:
                combined_prompt = " ".join(tokens[-max_prompt_tokens:])

            data = {
                "prompt": combined_prompt,
                "temperature": temp,
                "top_p": top_p,
                "n_predict": max_tokens,
                "repeat_penalty": repeat_penalty,
                "stop": []
            }

            tab_chat.insert(tk.END, f"\n⏳ [Chunk {i+1}/{total_chunks}] Menghasilkan...\n")
            r = requests.post(LLAMA_API, json=data, timeout=240)
            r.raise_for_status()
            content = r.json().get("content", "").strip()

            tab_chat.insert(tk.END, f"🤖 AI (Chunk {i+1}): {content}\n")
            tab_chat.see(tk.END)

            # ✅ Tambahkan ke file output:
            all_chunks_output += f"\n\n=== [Chunk {i+1}] ===\n{content}"

            # ✅ Update context untuk kelanjutan
            context_memory += "\n" + content
            context_tokens = context_memory.split()
            ctx_user = rakyat_ctx_size.get()
            if len(context_tokens) > ctx_user:
                context_memory = " ".join(context_tokens[-ctx_user:])
                
            # ✅ Simpan state jika auto resume aktif
            if enable_chunk_resume.get():
                status_resume = {
                    "total_chunks": total_chunks,
                    "words_per_chunk": words_per_chunk,
                    "last_completed_chunk": i + 1,
                    "full_prompt": full_prompt,
                    "context_memory": context_memory,
                    "all_chunks_output": all_chunks_output
                }
                with open("chunk_resume.json", "w", encoding="utf-8") as f:
                    json.dump(status_resume, f, ensure_ascii=False, indent=2)
            
            time.sleep(delay_per_chunk)
        except Exception as e:
            tab_chat.insert(tk.END, f"[❌ Error Chunk {i+1}]: {e}\n")
            break

    # ✅ Setelah semua chunk selesai, simpan ke file
    try:
        with open("generated_chunks.txt", "w", encoding="utf-8") as f:
            f.write(all_chunks_output.strip())
        tab_chat.insert(tk.END, f"\n📁 Semua chunk disimpan ke 'generated_chunks.txt'\n")
    except Exception as e:
        tab_chat.insert(tk.END, f"\n[❌ Gagal menyimpan file]: {e}\n")

    # ✅ RESET FLAG setelah selesai
    stop_chunk_generation = False
    chat_context += context_memory
    save_chat_context()
    generate_with_delay.set(False)  # Auto-uncheck setelah selesai generate chunk
    
def run_chunks_resume(resume_data, start_from_chunk):
    global stop_chunk_generation, chat_context

    total = resume_data["total_chunks"]
    context_memory = resume_data.get("context_memory", "")
    all_chunks_output = resume_data.get("all_chunks_output", "")

    for i in range(start_from_chunk, total):
        try:
            if stop_chunk_generation:
                tab_chat.insert(tk.END, f"\n🧼 Chunk dihentikan secara manual di chunk ke-{i+1}.\n")
                break

            if i == 0:
                combined_prompt = resume_data["full_prompt"] + f"\n\nTuliskan bagian pertama sebanyak ~{words_per_chunk} kata:\n"
            else:
                combined_prompt = (
                    "Berikut adalah lanjutan dari teks sebelumnya:\n"
                    + context_memory.strip()
                    + f"\n\nTuliskan bagian ke-{i+1} sebanyak ~{words_per_chunk} kata secara koheren dan melanjutkan dengan baik:\n"
                )

            max_prompt_tokens = rakyat_ctx_size.get() - max_tokens
            tokens = combined_prompt.split()
            if len(tokens) > max_prompt_tokens:
                combined_prompt = " ".join(tokens[-max_prompt_tokens:])

            data = {
                "prompt": combined_prompt,
                "temperature": temp,
                "top_p": top_p,
                "n_predict": max_tokens,
                "repeat_penalty": repeat_penalty,
                "stop": []
            }

            tab_chat.insert(tk.END, f"\n⏳ [Chunk {i+1}/{total}] Menghasilkan (resume)...\n")
            r = requests.post(LLAMA_API, json=data, timeout=240)
            r.raise_for_status()
            content = r.json().get("content", "").strip()

            tab_chat.insert(tk.END, f"🤖 AI (Chunk {i+1}): {content}\n")
            tab_chat.see(tk.END)

            all_chunks_output += f"\n\n=== [Chunk {i+1}] ===\n{content}"
            context_memory += "\n" + content

            # Simpan progres ke file
            status_resume = {
                "total_chunks": total,
                "words_per_chunk": words_per_chunk,
                "last_completed_chunk": i + 1,
                "full_prompt": resume_data["full_prompt"],
                "context_memory": context_memory,
                "all_chunks_output": all_chunks_output
            }
            with open("chunk_resume.json", "w", encoding="utf-8") as f:
                json.dump(status_resume, f, ensure_ascii=False, indent=2)

            time.sleep(delay_per_chunk)
        except Exception as e:
            tab_chat.insert(tk.END, f"[❌ Error Chunk {i+1}]: {e}\n")
            break

    # ✅ Finalisasi
    try:
        with open("generated_chunks.txt", "w", encoding="utf-8") as f:
            f.write(all_chunks_output.strip())
        tab_chat.insert(tk.END, f"\n📁 Semua chunk disimpan ke 'generated_chunks.txt'\n")
    except Exception as e:
        tab_chat.insert(tk.END, f"\n[❌ Gagal menyimpan file]: {e}\n")

    stop_chunk_generation = False
    chat_context += context_memory
    save_chat_context()
    generate_with_delay.set(False)

    # Hapus file resume jika semua selesai
    if not stop_now:
        if os.path.exists("chunk_resume.json"):
            os.remove("chunk_resume.json")

def stop_chunking():
    global stop_chunk_generation
    stop_chunk_generation = True
    tab_chat.insert(tk.END, "\n🛑 Permintaan untuk menghentikan chunk diterima.\n")

def start_llama(model_path, ctx_size=4096):
    global llama_process, model_loaded

    stop_llama()

    if not os.path.isfile(LLAMA_EXE):
        tab_chat.insert(tk.END, f"[❌] File {LLAMA_EXE} tidak ditemukan!\n")
        return

    args = [
        LLAMA_EXE,
        "--model", model_path,
        "--port", str(LLAMA_PORT),
        "--ctx-size", str(ctx_size)
    ]

    tab_chat.insert(tk.END, f"[⏳] Memulai server dengan model:\n{model_path}\n")
    try:
        llama_process = subprocess.Popen(
            args, stderr=subprocess.PIPE
        )
        threading.Thread(target=stream_output, args=(llama_process,), daemon=True).start()

        elapsed = wait_until_ready()
        if elapsed != -1:
            tab_chat.insert(tk.END, f"[✅] Model siap! (dalam {elapsed:.1f} detik)\n")
        else:
            tab_chat.insert(tk.END, "[❌] Gagal menjalankan model (timeout)\n")
    except Exception as e:
        tab_chat.insert(tk.END, f"[❌] Gagal menjalankan server: {e}\n")

def start_llama_from_settings():
    global current_model_path
    if not current_model_path or not os.path.isfile(current_model_path):
        messagebox.showerror("Error", "Model belum dipilih atau file tidak ditemukan.")
        return

    if rakyat_mode_enabled.get():
        ctx = rakyat_ctx_size.get()
        ram_mode = rakyat_ram_mode.get()
        tab_chat.insert(tk.END, f"[🌾] Rakyat Mode Aktif — ctx={ctx}, RAM Mode={ram_mode}\n")
        if ram_mode.lower().startswith("swap"):
            aktifkan_swap_rakyat_mode()
    else:
        ctx = 4096
        tab_chat.insert(tk.END, "[⚙️] Mode Normal aktif (ctx=4096)\n")

    start_llama(current_model_path, ctx_size=ctx)

def clear_history():
    open(HISTORY_FILE, "w").close()
    open(SESSION_FILE, "w").close()
    tab_chat.delete("1.0", tk.END)
    tab_chat.insert(tk.END, "[🧹] Riwayat dibersihkan.\n")

def upload_file_to_input():
    path = filedialog.askopenfilename(title="Pilih File", filetypes=[("Text","*.txt"),("All Files","*.*")])
    if not path: return
    try:
        with open(path,"r",encoding="utf-8") as f: content = f.read()
    except:
        with open(path,"r",encoding="latin1",errors="ignore") as f: content = f.read()
    tab_input.insert(tk.END, f"\n[📎] Konten file:\n{content[:1000]}...\n")

    # Kirim ringkasan ke kolom chat log
    if len(content) > 1000:
        summary = content[:500] + "\n...(diringkas)"
        tab_chat.insert(tk.END, f"[📎] Konten file (ringkasan):\n{summary}\n")
    else:
        tab_chat.insert(tk.END, f"[📎] Konten file:\n{content}\n")

def switch_theme(theme):
    themes = {
        "Gelap": {"bg": "#222", "fg": "white"},
        "Terang": {"bg": "#f0f0f0", "fg": "black"}
    }
    t = themes.get(theme, themes["Gelap"])
    for widget in [tab_chat, tab_input, system_prompt]:
        widget.config(bg=t["bg"], fg=t["fg"])
    style.theme_use("clam" if theme == "Gelap" else "default")
    current_theme.set(theme)
    save_config()

# --- GUI ---
root = tk.Tk()
root.title("LLaMA.cpp Server GUI")
root.geometry("900x850")
conf = load_config()
rakyat_mode_enabled = tk.BooleanVar(value=False)
rakyat_ctx_size = tk.IntVar(value=1024)
rakyat_ram_mode = tk.StringVar(value="Normal")
style = ttk.Style(); style.theme_use("clam")
style.configure("TLabel", background="#222", foreground="white")
style.configure("TFrame", background="#222")
style.configure("TButton", background="#333", foreground="white")
style.configure("TCombobox", fieldbackground="#333", background="#222", foreground="white")

notebook = ttk.Notebook(root)
frame_main = ttk.Frame(notebook); frame_settings = ttk.Frame(notebook); frame_system = ttk.Frame(notebook)
notebook.add(frame_main, text="💬 Chat"); notebook.add(frame_settings, text="⚙️ Pengaturan"); notebook.add(frame_system, text="🧠 Sistem")
notebook.pack(expand=True, fill="both")
rakyat_auto = tk.BooleanVar(value=conf.get("auto_load_rakyat_mode", False))
ttk.Checkbutton(frame_settings, text="Auto Load Rakyat Mode", variable=rakyat_auto).grid(row=5, column=0, columnspan=3, sticky="w")
ttk.Label(frame_settings, text="💡 Rakyat Mode").grid(row=10, column=0, sticky="w")

ttk.Checkbutton(frame_settings, text="Aktifkan Rakyat Mode", variable=rakyat_mode_enabled).grid(row=10, column=1, columnspan=2, sticky="w")

ttk.Label(frame_settings, text="CTX Size").grid(row=11, column=0, sticky="w")
ttk.Entry(frame_settings, textvariable=rakyat_ctx_size, width=10).grid(row=11, column=1, sticky="w")

ttk.Label(frame_settings, text="Mode RAM").grid(row=12, column=0, sticky="w")
ttk.Combobox(frame_settings, textvariable=rakyat_ram_mode, values=["Normal", "Swap Aktif", "Swap Maksimal"], width=15).grid(row=12, column=1, sticky="w")

ttk.Button(frame_settings, text="🧹 Reset Konteks Chat", command=reset_context).grid(row=13, column=0, sticky="w", pady=10)

frame_top = ttk.Frame(frame_main); frame_top.pack(pady=5)
ttk.Button(frame_top, text="📂 Muat Model", command=load_model).pack(side="left", padx=5)
ttk.Button(frame_top, text="🔁 Ganti Model", command=swap_model).pack(side="left", padx=5)
ttk.Button(frame_top, text="▶️ Mulai LLaMA Server", command=lambda: threading.Thread(target=start_llama_from_settings, daemon=True).start()).pack(side="left", padx=5)
preset_combo = ttk.Combobox(frame_top, values=list(presets.keys()), width=15)
preset_combo.set("Default"); preset_combo.bind("<<ComboboxSelected>>", apply_preset); preset_combo.pack(side="left")

status_label = tk.Label(frame_main, text="", fg="lime"); status_label.pack()
progress = ttk.Progressbar(frame_main, mode="indeterminate"); progress.pack(fill="x", padx=10)

tab_chat = scrolledtext.ScrolledText(frame_main, wrap=tk.WORD, height=25, width=120, bg="#111", fg="white")
tab_chat.pack(padx=10, pady=10); tab_chat.insert(tk.END, "💬 Selamat datang!\n")
load_chat_context()

if os.path.exists(SESSION_FILE):
    with open(SESSION_FILE, "r", encoding="utf-8") as f:
        tab_chat.insert(tk.END, f.read())

# Input teks
tab_input = tk.Text(frame_main, height=4, width=120, bg="#222", fg="white")
tab_input.pack(padx=10, pady=5)

# Frame untuk tombol dan opsi
frame_actions = ttk.Frame(frame_main)
frame_actions.pack(pady=5)

generate_with_delay = tk.BooleanVar(value=False)

# Tombol Kirim Chat / Generate Chunk
kirim_btn = ttk.Button(frame_actions, text="📨 Kirim Chat", command=lambda: handle_send())
kirim_btn.grid(row=0, column=0, padx=5, pady=3, sticky="w")

# Checkbox Generate Chunk Delay
ttk.Checkbutton(frame_actions, text="Generate Chunk Delay", variable=generate_with_delay).grid(row=0, column=1, padx=5, pady=3, sticky="w")

# Entry Delay (detik)
chunk_delay_var = tk.IntVar(value=10)
delay_entry = ttk.Entry(frame_actions, textvariable=chunk_delay_var, width=5)
delay_entry.grid(row=0, column=2, padx=2, pady=3)
ttk.Label(frame_actions, text="detik").grid(row=0, column=3, padx=2, pady=3)

# Checkbox Auto Resume
enable_chunk_resume = tk.BooleanVar(value=True)
chk_resume = ttk.Checkbutton(frame_actions, text="🧠 Auto Resume", variable=enable_chunk_resume)
chk_resume.grid(row=0, column=4, padx=5, pady=3)

# Tombol Stop Chunk
stop_chunk_btn = ttk.Button(frame_actions, text="🛑 Stop Chunk", command=lambda: stop_chunking())
stop_chunk_btn.grid(row=0, column=5, padx=5, pady=3)

# Tombol Ambil File
ttk.Button(frame_actions, text="📎 Ambil File", command=upload_file_to_input).grid(row=0, column=6, padx=5, pady=3)

# Fungsi untuk update label tombol
def update_button_label():
    if generate_with_delay.get():
        kirim_btn.config(text="🚀 Generate Chunk")
    else:
        kirim_btn.config(text="📨 Kirim Chat")

generate_with_delay.trace_add("write", lambda *args: update_button_label())

# ✅ Variabel Memory Mode
memory_mode_enabled = tk.BooleanVar(value=False)
selected_memory_profile = tk.StringVar()

# Checkbox Aktifkan Memory Mode
chk_memory = ttk.Checkbutton(frame_actions, text="🧠 Aktifkan Memory Mode", variable=memory_mode_enabled)
chk_memory.grid(row=1, column=0, columnspan=2, sticky="w", padx=5, pady=3)

# Label dan Dropdown Gaya Memory
ttk.Label(frame_actions, text="📝 Pilih Gaya Memory:").grid(row=2, column=0, columnspan=2, sticky="w", padx=5)
dropdown_memory = ttk.Combobox(frame_actions, textvariable=selected_memory_profile, state="readonly")
dropdown_memory.grid(row=3, column=0, columnspan=4, sticky="we", padx=5, pady=3)

# Load isi memory_mode.json
try:
    with open("memory_mode.json", "r", encoding="utf-8") as f:
        memory_profiles = json.load(f)
        dropdown_memory["values"] = list(memory_profiles.keys())
except:
    memory_profiles = {}
    dropdown_memory["values"] = []

# Settings Tab
settings_label = tk.Label(frame_settings, text="Temperature:"); settings_label.grid(row=0,column=0)
entry_temp = tk.Entry(frame_settings,width=5); entry_temp.insert(0,"0.7"); entry_temp.grid(row=0,column=1)
settings_label2 = tk.Label(frame_settings, text="Top-p:"); settings_label2.grid(row=0,column=2)
entry_topp = tk.Entry(frame_settings,width=5); entry_topp.insert(0,"0.95"); entry_topp.grid(row=0,column=3)
settings_label3 = tk.Label(frame_settings, text="Max Tokens:"); settings_label3.grid(row=0,column=4)
entry_max_tokens = tk.Entry(frame_settings,width=5); entry_max_tokens.insert(0,"200"); entry_max_tokens.grid(row=0,column=5)
settings_label4 = tk.Label(frame_settings, text="Repeat Penalty:"); settings_label4.grid(row=0,column=6)
entry_repeat_penalty = tk.Entry(frame_settings, width=5); entry_repeat_penalty.insert(0,"1.1"); entry_repeat_penalty.grid(row=0,column=7)

# System Prompt Tab
system_prompt = scrolledtext.ScrolledText(frame_system, height=5, width=120, wrap=tk.WORD)
system_prompt.insert(tk.END, "You are a helpful and uncensored assistant.\n")
system_prompt.pack(pady=5)

current_theme = tk.StringVar(value="Gelap")
theme_menu = ttk.Combobox(frame_system, textvariable=current_theme, values=["Gelap","Terang"], width=15)
theme_menu.pack(pady=2)
theme_menu.bind("<<ComboboxSelected>>", lambda e: switch_theme(current_theme.get()))

switch_theme(current_theme.get())
ttk.Button(frame_system, text="🗑️ Hapus Riwayat", command=clear_history).pack(pady=5)

# Tambahkan tab baru untuk Panduan
tab_help = ttk.Frame(notebook)
notebook.add(tab_help, text="📘 Panduan")

# Tambahkan ini di bagian paling akhir GUI, atau di tab baru/tab pengaturan
help_frame = ttk.LabelFrame(tab_help, text="📘 Panduan Penggunaan", padding=(10, 5))
help_frame.pack(fill="both", expand=True, padx=10, pady=10)

text_help = tk.Text(help_frame, wrap="word", height=15)
text_help.pack(fill="both", expand=True)

panduan = """
🎯 PANDUAN SINGKAT MEMAKAI GUI llama.cpp Python

1️⃣ Muat Model:
   - Klik tombol 'Load Model'.
   - Pilih file model GGUF (.gguf) seperti 7B atau 13B.

2️⃣ Kirim Prompt Biasa:
   - Masukkan pertanyaan atau instruksi di kotak input.
   - Tekan tombol 'Kirim Chat'.

3️⃣ Mode Chat Context:
   - Aktif otomatis. Riwayat dialog akan disimpan agar AI mengingat konteks.

4️⃣ Generate Panjang (Chunking):
   - Tulis target seperti: "Tulis 5000 kata tentang sejarah komputer dan 500 kata tiap bagian. Atau Write a journal in 5000 words and 500 words per paragraph."
   - GUI akan membagi jadi beberapa chunk otomatis setelah checklist generate chunk delay di samping kirim chat.
   - Gunakan 'Stop Chunk' jika ingin hentikan generate chunk di tengah.

5️⃣ Auto Resume:
   - Jika fitur aktif, chunk akan lanjut otomatis saat aplikasi dibuka ulang.
   - gunakan kata kunci "run auto chunk resume", "lanjutkan chunking", "resume chunk sekarang" di prompt dan klik tombol kirim chat untuk menjalankan fitur auto run chunk resume.

6️⃣ Memory Mode:
   - Centang opsi 'Aktifkan Memory Mode'.
   - Pilih gaya karakter/mentor di dropdown.
   - Tambah memory baru via prompt: tambah memory mode nama:<nama> isi:<isi>, contoh: tambah memory mode nama: Guru Fisika isi: Kamu adalah guru fisika sabar yang menjelaskan konsep dengan analogi sehari-hari.
   - contoh upadete memori ai via prompt adalah update memory: guru_fisika = Kamu adalah guru fisika yang sabar dan suka memberi analogi lucu.
   - Format update memory mode ai via prompt adalah update memory: nama_profile = isi atau update memory: nama_profile = isi memory terbaru, serta tambah memory mode nama: [NAMA] isi: [ISI]

7️⃣ Pengaturan Tambahan:
   - Atur temperature, top_p, ctx-size, dan delay di menu pengaturan.

8️⃣ Hemat RAM:
   - GUI hanya berukuran kilobytes.
   - Bisa menjalankan model 13B Q5_K_M dengan RAM 14GB aktif (tanpa GPU) dan model 8B Q8_0 dengan RAM 12 GB aktif dari total ram 16GB.
   - GUI tidak akan ngecrash dan memilih untuk optimalisasi ram dan cpu untuk tetap jalan.
   - Ada fitur auto load rakyat mode di menu pengaturan.
   
️⃣ Tema Gui:
   - Tema Gelap
   - Tema Terang
   - Pengaturan tema ada di menu sistem.

️⃣ Ambil File:
   - Input Prompt From File text (Bisa masukan prompt lewat file txt)
   - Input File lain dari docx, epub, html, dan pdf ke kolom chat.

📁 Semua hasil tersimpan di:
   - `generated_chunks.txt` (hasil panjang)
   - `chat_history.txt` dan `chat_context.json` (riwayat percakapan)
   - `chunk_resume.json` (lanjutkan chunk otomatis)
   - `last_session.txt` 

💡 Tips:
   - Jangan gunakan emoji terlalu banyak di prompt.
   - Hindari copy-paste dari Word — gunakan Notepad atau Notepad++.
"""

text_help.insert(tk.END, panduan)
text_help.config(state="disabled")  # Agar tidak bisa diubah pengguna

# Tab baru untuk README
tab_readme = ttk.Frame(notebook)
notebook.add(tab_readme, text="📄 README")

readme_frame = ttk.LabelFrame(tab_readme, text="📘 Informasi README dan Lisensi", padding=(10, 5))
readme_frame.pack(fill="both", expand=True, padx=10, pady=10)

text_readme = tk.Text(readme_frame, wrap="word", height=20)
text_readme.pack(fill="both", expand=True)

isi_readme = """
# 🎉 llama.cpp GUI Python (Versi Ringan Rakyat) 🇮🇩

GUI Python hanya berukuran kilobytes yang mampu menjalankan model AI 7B - 13B (Q4_K_M) tanpa GPU, tanpa web server. 
Hemat RAM, hemat kuota, dan bisa dijalankan oleh pengguna umum dengan sistem RAM 16GB.

## 📜 LICENSE - MIT License
Copyright (c) 2025 Satria Novian

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies 
of the Software, and to permit persons to whom the Software is furnished to do so, 
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

**THE SOFTWARE IS PROVIDED "AS IS"**, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
including but not limited to the warranties of MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE 
and NONINFRINGEMENT. In no event shall the authors or copyright holders be liable for any claim, 
damages or other liability, whether in an action of contract, tort or otherwise, arising from, 
out of or in connection with the software or the use or other dealings in the Software.

---

🧠 Dibuat oleh: **Satria Novian**  
📅 Tahun: 2025  
"""

text_readme.insert(tk.END, isi_readme)
text_readme.config(state="disabled")  # Membuatnya hanya bisa dibaca

# Load config
conf = load_config()
rakyat_mode_enabled.set(conf.get("rakyat_mode_enabled", False))
rakyat_ctx_size.set(conf.get("rakyat_ctx_size", 1024))
rakyat_ram_mode.set(conf.get("rakyat_ram_mode", "Normal"))
if "theme" in conf:
    current_theme.set(conf["theme"])
    switch_theme(conf["theme"])

# Auto load model dengan Rakyat Mode (ctx-size 1024)
if "last_model_path" in conf:
    model_path = conf["last_model_path"]
    if os.path.isfile(LLAMA_EXE) and os.path.isfile(model_path):
        current_model_path = model_path
        if conf.get("auto_load_rakyat_mode", False):
            tab_chat.insert(tk.END, "[🌾] Auto-muat model dalam RAKYAT MODE...\n")
            ctx = conf.get("rakyat_ctx_size", 1024)
            threading.Thread(target=start_llama, args=(model_path, ctx), daemon=True).start()
        else:
            threading.Thread(target=start_llama, args=(model_path,), daemon=True).start()

root.mainloop()