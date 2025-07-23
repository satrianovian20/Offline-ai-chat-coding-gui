# GUI Python Tkinter untuk Multichat AI
# Fitur sesuai permintaan: tanpa Gradio/Flask, chat tab hanya aktif setelah model dijalankan dari tab utama
# Author: @chatgpt

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import threading, subprocess, json, os, time, re, requests

class MultichatAI:
    def __init__(self, root):
        self.root = root
        self.root.title("Multichat AI GUI")

        self.model_running = False
        self.server_process = None
        self.chat_tabs = []
        self.contexts = {}
        self.memory_modes = self.load_memory_modes()

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

        run_server_btn = ttk.Button(self.main_tab, text="Run llama-server.exe", command=self.run_server)
        run_server_btn.pack(pady=5)

        new_tab_btn = ttk.Button(self.main_tab, text="New Chat Tab", command=self.create_chat_tab)
        new_tab_btn.pack(pady=5)

    def load_model(self):
        filepath = filedialog.askopenfilename(title="Select GGUF model")
        if filepath:
            messagebox.showinfo("Model Loaded", f"Loaded model: {os.path.basename(filepath)}")
            self.model_path = filepath

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

        run_chunk_btn = ttk.Button(tab, text="Run Chunk Resume", command=lambda: self.run_chunk_resume(chat_display))
        run_chunk_btn.pack(pady=2)

        close_btn = ttk.Button(tab, text="❌", command=lambda: self.close_tab(tab))
        close_btn.pack(anchor='ne')

        mem_mode_var = tk.StringVar()
        mem_dropdown = ttk.Combobox(tab, textvariable=mem_mode_var, values=list(self.memory_modes.keys()))
        mem_dropdown.pack(pady=2)

        auto_mem_chk = tk.BooleanVar()
        mem_auto_cb = ttk.Checkbutton(tab, text="Auto Load Memory Mode", variable=auto_mem_chk, command=lambda: self.auto_load_memory_mode(mem_mode_var.get(), chat_display))
        mem_auto_cb.pack()

        stop_event = threading.Event()
        stop_btn.config(command=stop_event.set)

        send_btn.config(command=lambda: self.send_prompt(prompt_entry, chat_display, chunk_chk.get(), chunk_delay.get(), tab_index, mem_mode_var.get(), stop_event))

        self.tab_control.add(tab, text=f"Chat {tab_index+1}")
        self.tab_control.select(tab)
        self.chat_tabs.append({
            'tab': tab,
            'chat_display': chat_display,
            'prompt_entry': prompt_entry,
            'context': [],
            'context_file': f"chat_context_{tab_index+1}.json",
            'history_file': f"chat_history_{tab_index+1}.txt",
            'chunk_file': f"chunk_{tab_index+1}.txt"
        })

    def send_prompt(self, entry, display, use_chunk, delay, tab_index, memory_mode, stop_event):
        prompt = entry.get()
        if not prompt:
            return

        if prompt.startswith("update memory:"):
            self.update_memory_mode(prompt)

        display.insert(tk.END, f"You: {prompt}\n")
        display.see(tk.END)
        entry.delete(0, tk.END)

        self.save_chat_history(tab_index, f"You: {prompt}\n")

        threading.Thread(target=self.query_server, args=(prompt, display, use_chunk, delay, tab_index, stop_event)).start()

    def query_server(self, prompt, display, use_chunk, delay, tab_index, stop_event):
        try:
            headers = {"Content-Type": "application/json"}
            payload = {"prompt": prompt, "stream": False}
            response = requests.post(self.server_url, json=payload, headers=headers)
            result = response.json()
            output = result.get("content", "[No response]")

            if re.search(r'(\d+)\s*words\s+and\s+(\d+)\s*words\s+per\s+chunk', prompt.lower()):
                use_chunk = True

            if use_chunk:
                words = output.split()
                chunk = 50
                chunk_lines = []
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
                    time.sleep(delay)
                with open(self.chat_tabs[tab_index]['chunk_file'], 'w', encoding='utf-8') as f:
                    f.writelines(chunk_lines)
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

    def run_chunk_resume(self, display):
        try:
            with open("chunk_resume.json", 'r', encoding='utf-8') as f:
                data = json.load(f)
                display.insert(tk.END, "\n[Chunk Resume Loaded]\n")
                display.insert(tk.END, data.get("chunk", "(empty)"))
                display.see(tk.END)
        except:
            display.insert(tk.END, "\n[Failed to load chunk_resume.json]\n")

    def close_tab(self, tab):
        index = self.tab_control.index(tab)
        self.tab_control.forget(index)
        del self.chat_tabs[index]

    def show_settings(self, tab_index):
        win = tk.Toplevel(self.root)
        win.title("Pengaturan Model")

        fields = ["ctx_size", "max_tokens", "temperature", "repeat_penalty", "top_p", "ram"]
        for f in fields:
            ttk.Label(win, text=f).pack()
            ttk.Entry(win).pack(fill='x', padx=5, pady=2)

if __name__ == "__main__":
    root = tk.Tk()
    app = MultichatAI(root)
    root.mainloop()
