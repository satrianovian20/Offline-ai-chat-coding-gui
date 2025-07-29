import tkinter as tk
from tkinter import ttk, messagebox, filedialog, simpledialog
import http.client
import pyperclip
import subprocess

class LlamaPortScannerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("LLaMA Server Port Detector & Launcher")
        self.root.geometry("520x420")

        self.model_path = None
        self.ctx_size = 4096
        self.server_process = None

        # Host
        self.host_var = tk.StringVar(value="127.0.0.1")
        host_frame = ttk.Frame(root)
        host_frame.pack(pady=10)
        ttk.Label(host_frame, text="Host:").pack(side=tk.LEFT, padx=(0, 5))
        self.host_entry = ttk.Combobox(host_frame, textvariable=self.host_var, values=["127.0.0.1", "localhost"], width=20)
        self.host_entry.pack(side=tk.LEFT)

        # Rentang Port
        range_frame = ttk.Frame(root)
        range_frame.pack(pady=(0, 5))
        ttk.Label(range_frame, text="Dari Port:").pack(side=tk.LEFT, padx=2)
        self.start_port = tk.IntVar(value=1234)
        ttk.Entry(range_frame, textvariable=self.start_port, width=6).pack(side=tk.LEFT)

        ttk.Label(range_frame, text="Sampai:").pack(side=tk.LEFT, padx=2)
        self.end_port = tk.IntVar(value=11500)
        ttk.Entry(range_frame, textvariable=self.end_port, width=6).pack(side=tk.LEFT)

        # Timeout
        timeout_frame = ttk.Frame(root)
        timeout_frame.pack(pady=(0, 10))
        ttk.Label(timeout_frame, text="Timeout (detik):").pack(side=tk.LEFT, padx=2)
        self.timeout_var = tk.DoubleVar(value=0.3)
        ttk.Entry(timeout_frame, textvariable=self.timeout_var, width=6).pack(side=tk.LEFT)

        # Port Display
        self.label = ttk.Label(root, text="Port LLaMA Server:")
        self.label.pack(pady=(10, 5))

        self.port_entry = ttk.Entry(root, width=30, justify="center")
        self.port_entry.pack()

        # Tombol Deteksi Otomatis
        self.scan_button = ttk.Button(root, text="🔍 Deteksi Port Otomatis", command=self.detect_port)
        self.scan_button.pack(pady=8)

        # Jalankan Server
        self.launch_button = ttk.Button(root, text="🚀 Jalankan llama-server.exe", command=self.run_llama_server)
        self.launch_button.pack(pady=8)

        # Tombol Copy dan Tes
        button_frame = ttk.Frame(root)
        button_frame.pack()

        self.copy_button = ttk.Button(button_frame, text="📋 Copy Port", command=self.copy_port)
        self.copy_button.pack(side=tk.LEFT, padx=5)

        self.test_button = ttk.Button(button_frame, text="✅ Tes Koneksi", command=self.test_connection)
        self.test_button.pack(side=tk.LEFT, padx=5)

        # Status
        self.status_label = ttk.Label(root, text="")
        self.status_label.pack(pady=12)

    def detect_port(self):
        host = self.host_var.get()
        start = self.start_port.get()
        end = self.end_port.get()
        timeout = self.timeout_var.get()

        self.status_label.config(text=f"🔄 Mendeteksi port dari {start} ke {end}...")
        self.root.update()

        for port in range(start, end + 1):
            try:
                conn = http.client.HTTPConnection(host, port, timeout=timeout)
                conn.request("GET", "/")
                response = conn.getresponse()
                if response.status == 200:
                    self.port_entry.delete(0, tk.END)
                    self.port_entry.insert(0, str(port))
                    self.status_label.config(text=f"✅ Port aktif terdeteksi: {port}")
                    return
            except:
                continue

        self.status_label.config(text="❌ Tidak ada port aktif ditemukan")

    def copy_port(self):
        port = self.port_entry.get()
        if port:
            pyperclip.copy(port)
            self.status_label.config(text=f"📋 Port {port} disalin ke clipboard!")
        else:
            messagebox.showwarning("Peringatan", "Belum ada port yang terdeteksi atau diisi.")

    def test_connection(self):
        host = self.host_var.get()
        port = self.port_entry.get()
        if not port.isdigit():
            messagebox.showerror("Error", "Port tidak valid.")
            return

        try:
            conn = http.client.HTTPConnection(host, int(port), timeout=1)
            conn.request("GET", "/")
            response = conn.getresponse()
            if response.status == 200:
                self.status_label.config(text=f"✅ Koneksi berhasil ke {host}:{port}")
            else:
                self.status_label.config(text=f"⚠️ Gagal: status {response.status}")
        except Exception:
            self.status_label.config(text=f"❌ Tidak bisa terhubung ke {host}:{port}")

    def run_llama_server(self):
        if not self.model_path:
            self.model_path = filedialog.askopenfilename(title="Pilih GGUF Model", filetypes=[("GGUF files", "*.gguf")])
            if not self.model_path:
                messagebox.showwarning("Batal", "Model belum dipilih.")
                return

        ctx_input = simpledialog.askinteger("Context Size", "Masukkan ctx-size (misal 4096):", minvalue=256, maxvalue=65536)
        if ctx_input:
            self.ctx_size = ctx_input

        base_port = 11434
        for port in range(base_port, base_port + 50):
            try:
                with http.client.HTTPConnection("127.0.0.1", port, timeout=0.1) as conn:
                    conn.connect()
            except:
                self.server_process = subprocess.Popen([
                    "llama-server.exe",
                    "--model", self.model_path,
                    "--port", str(port),
                    "--ctx-size", str(self.ctx_size)
                ])
                self.port_entry.delete(0, tk.END)
                self.port_entry.insert(0, str(port))
                self.status_label.config(text=f"🚀 Server dijalankan di port {port}")
                return

        self.status_label.config(text="❌ Tidak ada port bebas tersedia.")

if __name__ == "__main__":
    root = tk.Tk()
    app = LlamaPortScannerGUI(root)
    root.mainloop()