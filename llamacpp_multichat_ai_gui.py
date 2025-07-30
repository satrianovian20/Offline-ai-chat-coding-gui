# GUI Python Tkinter untuk Multichat AI
# Fitur sesuai permintaan: tanpa Gradio/Flask, chat tab hanya aktif setelah model dijalankan dari tab utama
# Author: Satria Novian and Contributor: @chatgpt

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import threading, subprocess, json, os, time, re, requests

class MultichatAI:
    def __init__(self, root):
        self.root = root
        self.root.title("LLaMA.cpp Server Multichat AI GUI")

        self.model_running = False
        self.server_process = None
        self.chat_tabs = []
        self.contexts = {}
        self.memory_modes = self.load_memory_modes()
        self.tab_system_prompts = {}  # Untuk menyimpan system prompt setiap tab
        self.tab_settings = {}  # Simpan pengaturan per tab, key = tab_index
        self.ctx_size = 4096  # default context size

        self.llama_port = 5001
        self.server_url = f"http://127.0.0.1:{self.llama_port}/completion"

        self.setup_main_tab()

    def setup_main_tab(self):
        self.tab_control = ttk.Notebook(self.root)
        self.tab_control.pack(fill='both', expand=True)

        self.main_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.main_tab, text="Main Tab")

        load_btn = ttk.Button(self.main_tab, text="Load GGUF Model", command=self.load_model)
        load_btn.pack(pady=5)
        
        change_model_btn = ttk.Button(self.main_tab, text="Change GGUF Model", command=self.change_model)
        change_model_btn.pack(pady=5)
        
        ctx_btn = ttk.Button(self.main_tab, text="Pengaturan Ctx Size", command=self.ctx_settings_dialog)
        ctx_btn.pack(pady=5)

        run_server_btn = ttk.Button(self.main_tab, text="Run llama-server.exe", command=self.run_server)
        run_server_btn.pack(pady=5)

        new_tab_btn = ttk.Button(self.main_tab, text="New Chat Tab", command=self.create_chat_tab)
        new_tab_btn.pack(pady=5)

    def load_model(self):
        filepath = filedialog.askopenfilename(title="Select GGUF model")
        if filepath:
            messagebox.showinfo("Model Loaded", f"Loaded model: {os.path.basename(filepath)}")
            self.model_path = filepath
            
    def change_model(self):
        if not self.model_running:
            self.load_model()
        else:
            confirm = messagebox.askyesno("Restart Required", "Server is running.\nDo you want to stop and load a new model?")
            if confirm:
                self.stop_server()
                time.sleep(1)
                self.load_model()
                messagebox.showinfo("Next Step", "Now click 'Run llama-server.exe' again.")

    def run_server(self):
        if hasattr(self, 'model_path'):
            try:
                self.server_process = subprocess.Popen(["llama-server.exe", "--model", self.model_path, "--port", str(self.llama_port)])
                self.model_running = True
                messagebox.showinfo("Success", "llama-server.exe started")
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showwarning("Warning", "Load model first")
            
    def stop_server(self):
        if self.server_process and self.server_process.poll() is None:
            self.server_process.terminate()
            self.server_process.wait()
            self.model_running = False
            messagebox.showinfo("Server Stopped", "llama-server.exe has been stopped.")
            
    def run_server_with_ctx(self):
        if hasattr(self, 'model_path'):
            try:
                self.server_process = subprocess.Popen([
                    "llama-server.exe",
                    "--model", self.model_path,
                    "--port", str(self.llama_port),
                    "--ctx-size", str(self.ctx_size)
                ])
                self.model_running = True
                messagebox.showinfo("Success", f"llama-server.exe started with ctx size {self.ctx_size}")
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showwarning("Warning", "Load model first")

    def create_chat_tab(self):
        if not self.model_running:
            messagebox.showwarning("Server not running", "Start llama-server.exe first")
            return

        tab = ttk.Frame(self.tab_control)
        tab_index = len(self.chat_tabs)

        chat_display = scrolledtext.ScrolledText(tab, wrap=tk.WORD, height=20)
        chat_display.pack(fill='both', expand=True)

        prompt_frame = ttk.Frame(tab)
        prompt_frame.pack(fill='x')

        prompt_entry = ttk.Entry(prompt_frame)
        prompt_entry.pack(side='left', fill='x', expand=True, padx=5, pady=5)

        send_btn = ttk.Button(prompt_frame, text="Kirim Prompt")
        send_btn.pack(side='left')

        chunk_delay = tk.DoubleVar(value=1.0)
        chunk_chk = tk.BooleanVar()
        chunk_cb = ttk.Checkbutton(prompt_frame, text="Generate per Chunk", variable=chunk_chk)
        chunk_cb.pack(side='left', padx=5)

        delay_spin = ttk.Spinbox(prompt_frame, from_=0.1, to=10.0, increment=0.1, textvariable=chunk_delay, width=5)
        delay_spin.pack(side='left')

        stop_btn = ttk.Button(prompt_frame, text="Stop Chunk")
        stop_btn.pack(side='left', padx=5)

        file_btn = ttk.Button(tab, text="Impor Prompt", command=lambda: self.import_prompt(prompt_entry))
        file_btn.pack(pady=2)

        setting_btn = ttk.Button(tab, text="Pengaturan", command=lambda: self.show_settings(tab_index))
        setting_btn.pack(pady=2)

        auto_chunk_var = tk.BooleanVar()
        manual_chunk_var = tk.BooleanVar()
        auto_chunk_cb = ttk.Checkbutton(tab, text="Auto Chunk Resume", variable=auto_chunk_var)
        auto_chunk_cb.pack()

        manual_cb = ttk.Checkbutton(tab, text="Manual Generate Delay", variable=manual_chunk_var)
        manual_cb.pack()

        run_chunk_btn = ttk.Button(tab, text="Run Chunk Resume", command=lambda d=chat_display, idx=tab_index: self.run_chunk_resume(d, idx))
        run_chunk_btn.pack(pady=2)
        
        reset_btn = ttk.Button(tab, text="🧹 Reset Chat Display", command=lambda idx=tab_index: self.reset_chat_display_only(idx))
        reset_btn.pack(pady=2)

        close_btn = ttk.Button(tab, text="❌", command=lambda: self.close_tab(tab))
        close_btn.pack(anchor='ne')

        mem_mode_var = tk.StringVar()
        mem_dropdown = ttk.Combobox(tab, textvariable=mem_mode_var, values=list(self.memory_modes.keys()))
        mem_dropdown.pack(pady=2)

        auto_mem_chk = tk.BooleanVar()
        mem_auto_cb = ttk.Checkbutton(tab, text="Auto Load Memory Mode", variable=auto_mem_chk, command=lambda: self.auto_load_memory_mode(mem_mode_var.get(), chat_display))
        mem_auto_cb.pack()
        
        # Tombol Edit System Prompt
        prompt_btn = ttk.Button(tab, text="🛠 Prompt System", command=lambda idx=tab_index: self.edit_system_prompt(idx))
        prompt_btn.pack(side=tk.LEFT, padx=5, pady=5)

        # Set default system prompt untuk tab ini
        self.tab_system_prompts[tab_index] = (
            "You are a helpful and intelligent assistant. "
            "Respond clearly, concisely, and follow the user's instructions precisely.\n"
        )

        stop_event = threading.Event()
        stop_btn.config(command=stop_event.set)

        send_btn.config(command=lambda: self.send_prompt(prompt_entry, chat_display, chunk_chk.get(), chunk_delay.get(), tab_index, mem_mode_var.get(), stop_event))
        
        # Inisialisasi default setting untuk tab ini
        self.tab_settings[tab_index] = {
            "max_tokens": "512",
            "temperature": "0.7",
            "top_p": "0.9",
            "repeat_penalty": "1.1"
        }

        self.tab_control.add(tab, text=f"Chat {tab_index+1}")
        self.tab_control.select(tab)
        self.chat_tabs.append({
            'tab': tab,
            'chat_display': chat_display,
            'prompt_entry': prompt_entry,
            'context': [],
            'context_file': f"chat_context_{tab_index+1}.json",
            'history_file': f"chat_history_{tab_index+1}.txt",
            'chunk_file': f"chunk_{tab_index+1}.txt",
            'config': {}
        })

    def send_prompt(self, entry, display, use_chunk, delay, tab_index, memory_mode, stop_event):
        prompt = entry.get()
        if not prompt:
            return

        if prompt.startswith("update memory:"):
            self.update_memory_mode(prompt)

        default_system_prompt = (
            "You are a helpful and intelligent assistant. "
            "Respond clearly, concisely, and follow the user's instructions precisely.\n"
        )
        system_prompt = self.tab_system_prompts.get(tab_index, default_system_prompt)

        # Ambil riwayat chat terakhir
        chat_lines = display.get("1.0", tk.END).strip().split("\n")
        last_lines = [line for line in chat_lines if line.startswith("You:") or line.startswith("AI:")]
        last_context = "\n".join(last_lines[-6:])  # 3 pasang

        # Tambahkan memory jika ada
        memory_context = self.memory_modes.get(memory_mode, "")
        memory_block = f"{memory_context}\n" if memory_context else ""

        # Bangun prompt
        full_prompt = f"{system_prompt}{memory_block}{last_context}\nUser: {prompt}\nAssistant:"

        display.insert(tk.END, f"You: {prompt}\n")
        display.see(tk.END)
        entry.delete(0, tk.END)

        self.save_chat_history(tab_index, f"You: {prompt}\n")

        threading.Thread(target=self.query_server, args=(full_prompt, display, use_chunk, delay, tab_index, stop_event)).start()

    def query_server(self, prompt, display, use_chunk, delay, tab_index, stop_event):
        try:
            headers = {"Content-Type": "application/json"}
            settings = self.tab_settings.get(tab_index, {})
            payload = {
                "prompt": prompt,
                "stream": False,
                "temperature": float(settings.get("temperature", 0.7)),
                "top_p": float(settings.get("top_p", 0.9)),
                "n_predict": int(settings.get("max_tokens", 512)),
                "repeat_penalty": float(settings.get("repeat_penalty", 1.1)),
                "stop": []
            }

            response = requests.post(self.server_url, json=payload, headers=headers)
            result = response.json()
            output = result.get("content", "[No response]")

            if re.search(r'(\d+)\s*words\s+and\s+(\d+)\s*words\s+per\s+chunk', prompt.lower()):
                use_chunk = True

            if use_chunk:
                words = output.split()
                chunk = 50
                chunk_lines = []
                chunk_resume = []  # Untuk file chunk_resume.json

                for i in range(0, len(words), chunk):
                    if stop_event.is_set():
                        display.insert(tk.END, f"\n[Stopped by user]\n")
                        break
                    part = ' '.join(words[i:i+chunk])
                    display.insert(tk.END, f"AI: {part}\n")
                    display.see(tk.END)
                    self.save_chat_context(tab_index, f"AI: {part}\n")
                    self.save_chat_history(tab_index, f"AI: {part}\n")
                    chunk_lines.append(f"AI: {part}\n")
                    chunk_resume.append({"chunk_index": i // chunk, "content": part})
                    time.sleep(delay)

                # Simpan ke save_chunk.txt
                with open(self.chat_tabs[tab_index]['chunk_file'], 'w', encoding='utf-8') as f:
                    f.writelines(chunk_lines)

                # Simpan ke chunk_resume.json
                chunk_resume_path = os.path.join(os.path.dirname(self.chat_tabs[tab_index]['chunk_file']), "chunk_resume.json")
                with open(chunk_resume_path, 'w', encoding='utf-8') as json_file:
                    json.dump(chunk_resume, json_file, indent=2, ensure_ascii=False)

            else:
                display.insert(tk.END, f"AI: {output}\n")
                display.see(tk.END)
                self.save_chat_context(tab_index, f"AI: {output}\n")
                self.save_chat_history(tab_index, f"AI: {output}\n")

        except Exception as e:
            display.insert(tk.END, f"[Error]: {str(e)}\n")
            display.see(tk.END)

    def save_chat_context(self, tab_index, line):
        ctx_file = self.chat_tabs[tab_index]['context_file']
        context = self.chat_tabs[tab_index].get('context', [])
        context.append(line.strip())
        self.chat_tabs[tab_index]['context'] = context
        with open(ctx_file, 'w', encoding='utf-8') as f:
            json.dump({"context": context}, f, ensure_ascii=False, indent=2)

    def save_chat_history(self, tab_index, line):
        hist_file = self.chat_tabs[tab_index]['history_file']
        with open(hist_file, 'a', encoding='utf-8') as f:
            f.write(line)

    def import_prompt(self, entry):
        file = filedialog.askopenfilename()
        if file:
            with open(file, 'r', encoding='utf-8') as f:
                entry.insert(0, f.read())

    def update_memory(self, tab_index, prompt):
        m = re.match(r"update memory:\s*(.*?)\s*=\s*(.*)", prompt)
        if m:
            name, content = m.groups()
            self.contexts[name] = content
            with open(f"context_{name}.json", 'w', encoding='utf-8') as f:
                json.dump({"context": content}, f)

    def update_memory_mode(self, prompt):
        m = re.match(r"update memory:\s*(.*?)\s*=\s*(.*)", prompt)
        if m:
            name, content = m.groups()
            self.memory_modes[name] = content
            with open("memory_mode.json", "w", encoding='utf-8') as f:
                json.dump(self.memory_modes, f)

    def load_memory_modes(self):
        try:
            with open("memory_mode.json", "r", encoding='utf-8') as f:
                return json.load(f)
        except:
            return {}

    def auto_load_memory_mode(self, name, display):
        if name in self.memory_modes:
            display.insert(tk.END, f"[Auto Memory Loaded: {name}]\n{self.memory_modes[name]}\n")
            display.see(tk.END)

    def run_chunk_resume(self, display, tab_index):
        try:
            chunk_resume_path = os.path.join(os.path.dirname(self.chat_tabs[tab_index]['chunk_file']), "chunk_resume.json")
            with open(chunk_resume_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                display.insert(tk.END, "\n[Chunk Resume Loaded]\n")
                for item in data:
                    display.insert(tk.END, f"AI (Chunk {item['chunk_index']}): {item['content']}\n")
                display.see(tk.END)
        except Exception as e:
            display.insert(tk.END, f"\n[Failed to load chunk_resume.json]: {e}\n")


    def close_tab(self, tab):
        index = self.tab_control.index(tab)
        self.tab_control.forget(index)
        del self.chat_tabs[index]

    def show_settings(self, tab_index):
        current_settings = self.tab_settings.get(tab_index, {
            "max_tokens": "512",
            "temperature": "0.7",
            "top_p": "0.9",
            "repeat_penalty": "1.1"
        })

        settings_window = tk.Toplevel(self.root)
        settings_window.title(f"Settings - Tab {tab_index + 1}")

        tk.Label(settings_window, text="Max Tokens:").grid(row=0, column=0)
        max_tokens_var = tk.StringVar(value=current_settings.get("max_tokens", "512"))
        tk.Entry(settings_window, textvariable=max_tokens_var).grid(row=0, column=1)

        tk.Label(settings_window, text="Temperature:").grid(row=1, column=0)
        temperature_var = tk.StringVar(value=current_settings.get("temperature", "0.7"))
        tk.Entry(settings_window, textvariable=temperature_var).grid(row=1, column=1)

        tk.Label(settings_window, text="Top-p:").grid(row=2, column=0)
        top_p_var = tk.StringVar(value=current_settings.get("top_p", "0.9"))
        tk.Entry(settings_window, textvariable=top_p_var).grid(row=2, column=1)
        
        tk.Label(settings_window, text="Repeat Penalty:").grid(row=3, column=0)
        repeat_penalty_var = tk.StringVar(value=current_settings.get("repeat_penalty", "1.1"))
        tk.Entry(settings_window, textvariable=repeat_penalty_var).grid(row=3, column=1)

        def save_local_settings():
            self.tab_settings[tab_index] = {
                "max_tokens": max_tokens_var.get(),
                "temperature": temperature_var.get(),
                "top_p": top_p_var.get(),
                "repeat_penalty": repeat_penalty_var.get()
            }
            messagebox.showinfo("Saved", f"Settings saved for Tab {tab_index + 1}")
            settings_window.destroy()

        tk.Button(settings_window, text="Save", command=save_local_settings).grid(row=4, columnspan=2)
        
    def edit_system_prompt(self, tab_index):
        current_prompt = self.tab_system_prompts.get(tab_index, "You are a helpful assistant.\n")
        default_prompt = (
            "You are a helpful and intelligent assistant. "
            "Respond clearly, concisely, and follow the user's instructions precisely.\n"
        )

        prompt_win = tk.Toplevel(self.root)
        prompt_win.title(f"Edit System Prompt - Tab {tab_index + 1}")
        prompt_win.geometry("500x300")

        label = ttk.Label(prompt_win, text="Edit system prompt for this chat tab:")
        label.pack(pady=5)

        prompt_text = tk.Text(prompt_win, wrap=tk.WORD)
        prompt_text.insert(tk.END, current_prompt)
        prompt_text.pack(expand=True, fill=tk.BOTH, padx=10, pady=5)

        def save_prompt():
            new_prompt = prompt_text.get("1.0", tk.END).strip()
            self.tab_system_prompts[tab_index] = new_prompt
            messagebox.showinfo("Saved", "System prompt updated successfully.")
            prompt_win.destroy()

        def reset_prompt():
            prompt_text.delete("1.0", tk.END)
            prompt_text.insert(tk.END, default_prompt)

        btn_frame = ttk.Frame(prompt_win)
        btn_frame.pack(pady=5)

        save_btn = ttk.Button(btn_frame, text="💾 Save", command=save_prompt)
        save_btn.pack(side=tk.LEFT, padx=5)

        reset_btn = ttk.Button(btn_frame, text="🔁 Reset Default", command=reset_prompt)
        reset_btn.pack(side=tk.LEFT, padx=5)

    def ctx_settings_dialog(self):
        win = tk.Toplevel(self.root)
        win.title("Pengaturan Ctx Size")

        tk.Label(win, text="Context Size:").grid(row=0, column=0, padx=10, pady=5)
        ctx_var = tk.StringVar(value=str(self.ctx_size))
        tk.Entry(win, textvariable=ctx_var).grid(row=0, column=1, padx=10, pady=5)

        def save_ctx():
            try:
                self.ctx_size = int(ctx_var.get())
                win.destroy()
                self.run_server_with_ctx()
            except ValueError:
                messagebox.showerror("Error", "Ctx size harus angka bulat")

        def reset_ctx():
            ctx_var.set("4096")

        tk.Button(win, text="💾 Save & Run Server", command=save_ctx).grid(row=1, column=0, pady=10)
        tk.Button(win, text="🔁 Reset Default", command=reset_ctx).grid(row=1, column=1, pady=10)
        
    def reset_chat_display_only(self, tab_index):
        try:
            tab_info = self.chat_tabs[tab_index]
            display_widget = tab_info['chat_display']
            display_widget.delete("1.0", tk.END)
            display_widget.insert(tk.END, "[Chat cleared from display only — history & context preserved]\n")
            display_widget.see(tk.END)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to reset chat display: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = MultichatAI(root)
    root.mainloop()
