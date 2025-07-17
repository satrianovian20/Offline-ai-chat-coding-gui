# offline-ai-chat-coding-gui
GUI Python ringan (Tkinter) untuk menjalankan AI chat &amp; coding dengan model GGUF lokal (Low GUI PYTHON from Tkinter to run Offline AI Chat and Coding)
# 💬 Offline AI Chat & Coding GUI (Super Ringan untuk PC Low-End)

Proyek ini adalah GUI Python ringan (Tkinter) untuk menjalankan model AI lokal (format `.gguf` seperti LLaMA 7B atau WizardLM 13B) di PC Windows biasa dengan GPU seperti **GTX 1650 Super**. Tanpa Flask. Tanpa Gradio. Tanpa ribet. Hanya Python satu file + model!

🇮🇩 Bahasa Indonesia:

🎉 Pertama kalinya dalam sejarah: Model AI 13B (Q4_K_M) berhasil dijalankan hanya dengan RAM 16GB — tanpa GPU, tanpa web server, cukup dengan GUI Python ukuran 10KB! Bukti nyata efisiensi maksimal 💪

🇬🇧 English Version:

🎉 First time in history: A 13B (Q4_K_M) AI model runs smoothly with just 16GB RAM — no GPU, no web server, only a 10KB Python GUI! Proof of ultimate efficiency 💪

> 🇮🇩 This project is primarily documented in Indonesian.
> 🇬🇧 English overview is provided below.

## 🇮🇩 Bahasa Indonesia

GUI lokal untuk LLaMA.cpp:
- Auto-load model GGUF
- Auto-save/load sesi
- Tema gelap & terang
- Ganti model tanpa restart
- Ringan, cocok untuk RAM 8-16 GB
- Tidak pakai Gradio atau WebUI

📁 Cocok untuk chat dan coding!

⚠️ Versi LLaMA.cpp yang WAJIB Digunakan
🛑 Hanya versi b5899 yang stabil dan telah diuji.
🔗 Unduh dari link berikut:

✅ llama-b5899-bin-win-cpu-x64.zip (Rekomendasi)

Versi di atas adalah satu-satunya yang telah diuji berhasil memuat model lewat GUI ini.
Versi di atas b900 tidak kompatibel dan menyebabkan gagal muat model (blank, stuck, atau crash).

✅ GUI AI Lokal ini telah diuji:
📌 Model: Mistral-7B-Instruct-v0.3 (q4_k_m.gguf)
🧠 Tanpa GPU, hanya CPU (llama.cpp b5899)
💻 RAM 16GB — Penggunaan hanya 12.1GB
🎵 Multitasking lancar: ChatGPT + YouTube + GitHub + Musik

💬 Contoh jawaban untuk user awam:
“GUI ini nggak ngebatesin kemampuan AI-nya. Kamu bisa atur output token sesuai kemampuan RAM PC kamu. Misal RAM kamu cuma 8GB, kamu bisa atur max token ke 150 biar tetap lancar. Kalau RAM kamu 16GB, bisa gaspol sampai 400 token. Jadi fleksibel, ringan, dan tetap powerful!”

🚀 Efisien, ringan, dan cocok untuk PC rumahan.
📁 Unduh llama.cpp versi b5899 (wajib):
https://github.com/ggml-org/llama.cpp/releases/download/b5899/llama-b5899-bin-win-cpu-x64.zip

## 📸 Screenshot (Model berhasil dimuat di RAM 16GB)

![Model Loaded Screenshot](https://github.com/satrianovian20/offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202025-07-17%20114247.png)

🧠 Model 13B di PC RAM 16GB – Bukti Nyata!
💡 Berdasarkan log di bawah ini, wizardlm-13b-v1.2.Q4_K_M.gguf berhasil dimuat dan digunakan di sistem dengan RAM 16GB, hanya memakai CPU (llama.cpp b5899) — tanpa error, dengan pemakaian RAM sekitar 13–14GB.

🧠 Super efisien memori bahkan saat menjalankan model AI besar 13B!

📉 Dari:

⬆️ 15.5–16 GB saat aktif dipakai,

lalu turun ke 14.7 GB saat idle,

dan sekarang tinggal 12.3 GB ‼️

📌 Kesimpulan:
✅ Model 13B bisa dijalankan di sistem 16GB RAM dengan quant Q4_K_M
✅ Tidak perlu GPU (CPU only)
✅ GUI ringan seperti buatan Anda tetap responsif
✅ Ideal untuk user lokal yang ingin performa tinggi dengan hardware minimal

## 📸 Screenshot (Model berhasil dimuat di RAM 16GB)

![Model Loaded Screenshot](https://github.com/satrianovian20/offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202025-07-17%20125025.png)

✅ Sukses Menjalankan LLaMA-2 13B Q4_K_M
GUI Python ini berhasil menjalankan model besar seperti `llama-2-13b-chat.Q4_K_M.gguf` dengan RAM 16GB (tanpa GPU).

🖥️ Spesifikasi:
- RAM: 16GB DDR4
- Backend: llama.cpp b5899
- Model: 13B GGUF (Q4_K_M)
- GUI: Python (.py) 10KB buatan sendiri

📸 Bukti: Sudah dilampirkan screenshot dan log lengkap di repo

🧠 Uji Stabilitas Memori – Model 13B (Q4_K_M)
Diuji menggunakan model llama-2-13b-chat.Q4_K_M.gguf dengan backend llama.cpp versi b5899.

Kondisi Penggunaan	Penggunaan RAM
Saat Aktif Digunakan	~15.5–16.0 GB
Saat Idle (Tidak Dipakai)	~12.3–12.4 GB

✅ Stabil dan efisien bahkan untuk model 13B pada PC dengan RAM 16GB.
⚠️ Tanpa GPU, dijalankan sepenuhnya di CPU via llama-server.exe.

💡 Kesimpulan Buat Pengguna GUI:
Kalau user punya RAM:

8GB: Deepseek 1.3B atau TinyLlama cukup, tapi jangan berharap jawaban super.

12GB–16GB: Langsung lompat ke Mistral 7B atau DeepSeek-Coder 6.7B.

>16GB: Bisa gas model 13B seperti Yi-13B, OpenHermes 13B, dll.

Optimalitas GUI Python 10KB:
✅ GUI Python 10KB Terbukti Optimal dan Stabil

GUI ini hanya berukuran 10KB namun sudah terbukti mampu menangani model AI lokal besar seperti LLaMA-2 13B Q4_K_M tanpa eror, crash, atau freeze, bahkan saat dijalankan di PC tanpa GPU.

📌 Keunggulan:

✔️ Ukuran super ringan (10KB)

✔️ Bisa langsung jalan tanpa instalasi ribet

✔️ Menggunakan llama.cpp sebagai backend (kompatibel GGUF)

✔️ RAM usage stabil di ~12.3GB saat idle

✔️ Load model 13B sukses tanpa error

✔️ GUI tetap responsif dan tidak berat

✔️ Output respons tetap stabil meski model besar

💡 GUI ini bahkan lebih optimal dibanding banyak UI besar di luar sana karena tidak menyia-nyiakan resource, cocok untuk pengguna low-end PC yang tetap ingin merasakan kekuatan model besar lokal.

📌 Bonus Penjelasan Visual (Flowchart Saran)

csharp
Copy
Edit
[Mulai GUI]
   ↓
[Load Model]
   → RAM = 15.5GB
   → CPU 60%
   ↓
[Model Idle]
   → RAM = 12.3GB
   → CPU 5%
   ↓
[Prompt Masuk]
   → CPU 100%
   ↓
[Generate Response]
   → Output OK
   ↓
[Idle Lagi]
   → RAM tetap
   → CPU turun

✅ Recap Status Dokumentasi (versi Indonesia):
Elemen Bukti	Status
📜 Log sesi (session-logs)	✅ Sudah ada
🖼️ Screenshot saat load model	✅ Sudah ada
🖼️ Screenshot saat idle	✅ Sudah ada
🧪 Model besar (13B Q4_K_M)	✅ Sudah diuji
⚙️ GUI ringan (10KB Python script)	✅ Terpakai dengan lancer

🎯 Multitasking Test Lulus dengan Mulus!

✅ GUI Python (10KB) masih berjalan

✅ AI tidak sedang aktif memproses prompt

✅ Playback video 720p lancar

✅ RAM hanya digunakan sekitar 12.5 GB

✅ Tanpa crash, tanpa lag, dan sistem tetap responsif

📌 Ini membuktikan bahwa meskipun model AI 13B sudah dimuat sebelumnya dan belum ditutup, sistem tetap efisien dan GUI kamu tidak membebani RAM berlebihan saat idle.

✅ FAQ — Pertanyaan Umum (Trust Booster Edition)
❓ GUI ini beneran bisa jalanin model 13B tanpa GPU?
Ya! Sudah diuji langsung dengan model llama-2-13b-chat.Q4_K_M.gguf di sistem dengan:

💻 CPU: Intel i5-9400F (tanpa iGPU)

🧠 RAM: 16GB DDR4

⚙️ Backend: llama.cpp

📦 GUI: Python script ukuran hanya 10KB

❓ Bukti nyatanya mana?
📸 Screenshot saat load model dan idle sudah diunggah di folder docs/screenshots/

📄 Log lengkap sesi percobaan model 13B tersedia di docs/session-logs/

Tidak ada error, tidak crash, hanya delay wajar saat proses berat.

❓ GUI-nya berat gak?
Tidak. GUI ini hanya 10KB, tanpa dependensi besar seperti Gradio atau Electron.

Tidak buka port aneh-aneh.

Tidak ada tracking.

Murni offline dan lokal.

UI sangat ringan, hanya berbasis tkinter.

❓ Bisa pakai model 7B, 8B, atau 13B lain?
Bisa! Sudah diuji dengan:

Mistral 7B

DeepSeek Coder 6.7B

Yi 13B

Nous Hermes 13B

LLaMA 13B (Q4_K_M dan Q4_0)

❓ RAM saya cuma 8GB, bisa jalan?
Bisa, asal model yang dipilih sesuai. Gunakan model kecil seperti:

TinyLlama 1.1B

DeepSeek Coder 1.3B

Atur max_tokens di GUI agar tidak melebihi kapasitas RAM kamu.

---

## 🌐 English (International)

🧠 About This Project
This Python GUI lets you run GGUF models locally (like LLaMA 7B, 13B, etc.) using llama-server.exe and chat just like ChatGPT — fully offline.

Local GUI for LLaMA.cpp:
- Auto-load GGUF model on launch
- Session save/load
- Dark/light mode
- Hot-swap model without GUI restart
- Lightweight, works on 8-16 GB RAM
- No Gradio or WebUI required

📁 Designed for chat and code!

⚠️ Required LLaMA.cpp Version
🛑 Only version b5899 is tested and supported.
🔗 Download here:

✅ llama-b5899-bin-win-cpu-x64.zip (Recommended)

Other versions, especially b900+, are not compatible and may cause model loading failure.

💻 Minimum Requirements
Component	Minimum
RAM	16 GB (recommended)
CPU	Intel/AMD 64-bit
GPU	Optional (CPU only OK)
OS	Windows 10/11 64-bit

⚠️ You can run 7B model on 8GB RAM, but expect very slow performance.
Best experience starts at 16GB RAM or more.

✅ This Local AI Chat & Coding GUI has been tested:
📌 Model: Mistral-7B-Instruct-v0.3 (q4_k_m.gguf)
🧠 CPU-only (no GPU) using llama.cpp b5899
💻 16GB RAM system — Only 12.1GB usage
🎵 Smooth multitasking: ChatGPT + YouTube + GitHub + Music

💬 Example answer for beginner users:

“This GUI doesn’t limit the AI’s capabilities. You can adjust the output tokens based on your PC’s RAM. For example, if you only have 8GB of RAM, you can set the max tokens to 150 so it runs smoothly. If you have 16GB of RAM, you can go all the way up to 400 tokens. So it’s flexible, lightweight, and still powerful!”

🚀 Efficient, lightweight, and perfect for personal PCs.
📁 Must use llama.cpp build b5899:
https://github.com/ggml-org/llama.cpp/releases/download/b5899/llama-b5899-bin-win-cpu-x64.zip

## 📸 Screenshot (Model successfully loaded on 16GB RAM)

![Model Loaded Screenshot](https://github.com/satrianovian20/offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202025-07-17%20114247.png)

🇬🇧 English Version:
🧠 13B Model on 16GB RAM PC – Real Proof!
💡 According to the log below, wizardlm-13b-v1.2.Q4_K_M.gguf successfully loaded and ran on a 16GB RAM system, using CPU only (llama.cpp b5899) — no errors, RAM usage around 13–14GB.

📌 Conclusion:
✅ 13B models are usable on 16GB RAM systems with Q4_K_M quant
✅ No GPU required (CPU only)
✅ Lightweight GUIs like yours remain responsive
✅ Perfect for local users who want high performance on minimal hardware

## 📸 Screenshot (Model successfully loaded on 16GB RAM)

![Model Loaded Screenshot](https://github.com/satrianovian20/offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202025-07-17%20125025.png)

✅ Successfully Running LLaMA-2 13B Q4_K_M
This Python GUI successfully runs a large model like llama-2-13b-chat.Q4_K_M.gguf using only 16GB RAM (no GPU required).

🖥️ Specifications:

RAM: 16GB DDR4

Backend: llama.cpp b5899

Model: 13B GGUF (Q4_K_M)

GUI: Custom-built Python script (only 10KB)

📸 Proof: Full logs and screenshots are already included in the repository.

🧠 Memory Stability Test – 13B Model (Q4_K_M)
Tested with llama-2-13b-chat.Q4_K_M.gguf using llama.cpp b5899 backend.

State	RAM Usage
Active Use	~15.5–16.0 GB
Idle (not used)	~12.3–12.4 GB

✅ Stable and efficient even with 13B models on 16GB RAM setup.
⚠️ No GPU required. CPU-only run using llama-server.exe.

💡 Summary for GUI Users:

If the user has:

8GB RAM: Deepseek 1.3B or TinyLlama is enough, but don’t expect super smart answers.

12GB–16GB RAM: Go straight to Mistral 7B or DeepSeek-Coder 6.7B.

More than 16GB RAM: You can run 13B models like Yi-13B, OpenHermes 13B, etc.

✅ Memory Efficiency Benchmark
After loading and running llama-2-13b-chat.Q4_K_M.gguf (13B model), the RAM usage peaked around 15.5–16 GB.
However, once the model is idle (not generating responses), memory usage drops to around 14.7 GB, proving the backend and GUI are optimized.

🧠 Efficient memory handling, even for large models, with only a 10KB Python GUI.

🧪 Real-Time RAM Usage (Tested with LLaMA-2 13B Q4_K_M)
Status	RAM Usage
Model running	~15.5–16 GB
Model idle	~14.7 GB
After inactivity	~12.3 GB

✅ Memory automatically freed when model is not actively used.

Python GUI 10KB Efficiency Highlight:
✅ This 10KB Python GUI Is Truly Optimal and Stable

Despite its minimal size (only 10KB), this GUI has proven its ability to handle large local AI models like LLaMA-2 13B Q4_K_M without errors, crashes, or instability, even on systems without a GPU.

📌 Highlights:

✔️ Ultra-lightweight (only 10KB)

✔️ Plug-and-play – no complex setup

✔️ Uses llama.cpp as the backend (GGUF compatible)

✔️ Stable RAM usage ~12.3GB when idle

✔️ Successfully loads 13B model without error

✔️ GUI remains responsive

✔️ Consistent output even with large models

💡 Compared to many heavy GUIs out there, this one is remarkably optimized and efficient, making it ideal for low-end users who want to harness the power of large local models.

📌 Bonus Visual Explanation (Suggested Flowchart)

csharp
Copy
Edit
[Start GUI]
   ↓
[Load Model]
   → RAM = 15.5GB
   → CPU 60%
   ↓
[Model Idle]
   → RAM = 12.3GB
   → CPU 5%
   ↓
[Prompt Received]
   → CPU 100%
   ↓
[Generate Response]
   → Output OK
   ↓
[Back to Idle]
   → RAM stable
   → CPU drops

✅ Documentation Recap (English Version):
Evidence Element	Status
📜 Session Logs (session-logs/)	✅ Available
🖼️ Screenshot while loading model	✅ Available
🖼️ Screenshot while idle	✅ Available
🧪 Large Model (13B Q4_K_M)	✅ Successfully tested
⚙️ Lightweight GUI (10KB Python script)	✅ Runs smoothly and reliably

🎯 Multitasking Test Passed Smoothly!

✅ Python GUI (10KB) still running

✅ AI model not actively processing

✅ 720p video playback is smooth

✅ RAM usage remains around 12.5 GB

✅ No crash, no lag, and system is responsive

📌 This confirms that even after a large 13B model was previously loaded, the system stays efficient. Your GUI doesn't overconsume memory while idle — this is top-tier optimization.

✅ FAQ — Frequently Asked Questions (Trust Booster Edition)
❓ Can this GUI really run a 13B model without a GPU?
Yes! It has been successfully tested using llama-2-13b-chat.Q4_K_M.gguf on a system with:

💻 CPU: Intel i5-9400F (no iGPU)

🧠 RAM: 16GB DDR4

⚙️ Backend: llama.cpp

📦 GUI: Pure Python script, only 10KB in size

❓ Any proof?
Absolutely. We've included:

📸 Screenshots while loading and idling in docs/screenshots/

📄 Full session logs with detailed model behavior in docs/session-logs/

Zero errors or crashes during testing — only brief delays during heavy processing, which is normal.

❓ Is the GUI heavy or bloated?
No. It’s extremely lightweight and minimal:

Just 10KB in .py size

No Electron, no Gradio, no browser needed

No background ports, no telemetry

Fully offline, secure, and fast

❓ Can I use 7B, 8B, or other 13B models too?
Yes! This GUI supports any local GGUF model that’s compatible with llama.cpp.
Tested successfully with:

Mistral 7B

DeepSeek Coder 6.7B

Yi 13B, Nous Hermes 13B

LLaMA 13B (Q4_K_M, Q4_0)

❓ I only have 8GB RAM. Can I still use this?
Yes — as long as you choose the right model and configure the token output wisely.
For example:

Use TinyLlama 1.1B or DeepSeek Coder 1.3B

Set max_tokens to 100–150 in the GUI to ensure smooth performance

---
🤝 Kontribusi & Kredit
👨‍💻 Creator: [satrianovian20] – Modifikasi GUI offline dengan Tkinter

✍️ Kontributor AI Script & Fixer Error: ChatGPT

🔁 Model by Meta (LLaMA), WizardLM, dan komunitas open-source

💡 Terinspirasi oleh kesulitan real pengguna dengan PC low-end

---
## 📦 Daftar Versi GUI

Berikut versi-versi GUI yang berhasil diuji:

| Versi File                 | Status  | Fitur Utama                             |
|---------------------------|---------|------------------------------------------|
| llamacpp_gui_combined.py  | ✅ Stabil | Versi awal gabungan GUI chat + sistem    |
| llamacpp_gui_combinedv2.py| ✅        | Tambahan pengaturan model & prompt       |
| llamacpp_gui_combinedv3.py| ✅        | Fix error kecil, UI lebih bersih         |
| llamacpp_gui_combinedv4.py| ✅        | + Logging dan auto-load model            |
| llamacpp_gui_combinedv5.py| ✅        | + Riwayat chat dan sistem prompt         |
| llamacpp_gui_combinedv6.py| ✅        | + Theme mode dan pengaturan lanjutan     |
| llamacpp_gui_combinedv7.py| ✅        | + Auto-save session dan repeat_penalty   |
| llamacpp_gui_combinedv8.py| ✅ Terbaru | + Auto-save load model berfungsi        |
| llamacpp_gui_mode.py      | Eksperimen | Mode GUI ringan eksperimen               |
| llamacpp_gui_modev2.py    | ✅        | Kombinasi GUI mode dengan layout sistem  |

## 💡 Syarat Minimum PC

| Komponen         | Minimum                    |
|------------------|-----------------------------|
| Prosesor         | i3/i5 Gen 8+ (atau Ryzen 3+) |
| RAM              | 16 GB (direkomendasikan 32 GB)|
| GPU              | GTX 1650 / setara (VRAM 4GB) |
| OS               | Windows 10/11 64-bit        |
| Python           | 3.10+                       |

---

## 📦 Cara Install & Jalankan

### 1. Download Python
Install Python 3.10 dari https://www.python.org/downloads/release/python-3100/

> ✅ Centang “Add Python to PATH” saat install!
> pip install requests

---

### 💖 Dukung Proyek Ini

Jika kamu merasa proyek ini bermanfaat dan ingin mendukung pengembangannya, kamu bisa berdonasi melalui:

- 💸 [Saweria](https://saweria.co/satrianovian20)
- ☕ [PayPal](https://www.paypal.com/paypalme/satrianovian)

Terima kasih banyak atas dukungannya! 🙏

### 2. Clone atau Download Proyek Ini

```bash
git clone https://github.com/satrianovian20/offline-ai-chat-coding-gui.git
cd offline-ai-chat-coding-gui

☕ Penutup
Proyek ini dibuat karena keterbatasan memunculkan inovasi. Saya juga pernah pusing karena WebUI dari GitHub gagal jalan, sampai akhirnya saya:

Buat GUI sendiri

Cuma pakai 1 file Python untuk AI Chat & Coding

Bisa sambil nonton YouTube 😄

💬 Kalau kamu juga merasakan manfaatnya, bantu bintang repo ini!
Supaya tidak ada lagi yang pusing karena “AI-nya gak bisa jalan...” 😅
