# offline-ai-chat-coding-gui
GUI Python ringan (Tkinter) untuk menjalankan AI chat &amp; coding dengan model GGUF lokal (Low GUI PYTHON from Tkinter to run Offline AI Chat and Coding)
# 💬 Offline AI Chat & Coding GUI (Super Ringan untuk PC Low-End)

Proyek ini adalah GUI Python ringan (Tkinter) untuk menjalankan model AI lokal (format `.gguf` seperti LLaMA 7B atau WizardLM 13B) di PC Windows biasa dengan GPU seperti **GTX 1650 Super**. Tanpa Flask. Tanpa Gradio. Tanpa ribet. Hanya Python satu file + model!

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

💡 Kesimpulan Buat Pengguna GUI:
Kalau user punya RAM:

8GB: Deepseek 1.3B atau TinyLlama cukup, tapi jangan berharap jawaban super.

12GB–16GB: Langsung lompat ke Mistral 7B atau DeepSeek-Coder 6.7B.

>16GB: Bisa gas model 13B seperti Yi-13B, OpenHermes 13B, dll.

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

💡 Summary for GUI Users:

If the user has:

8GB RAM: Deepseek 1.3B or TinyLlama is enough, but don’t expect super smart answers.

12GB–16GB RAM: Go straight to Mistral 7B or DeepSeek-Coder 6.7B.

More than 16GB RAM: You can run 13B models like Yi-13B, OpenHermes 13B, etc.

---
🤝 Kontribusi & Kredit
👨‍💻 Creator: [satrianovian20] – Modifikasi GUI offline dengan Tkinter

✍️ Kontributor AI Script & Fixer Error: ChatGPT

🔁 Model by Meta (LLaMA), WizardLM, dan komunitas open-source

💡 Terinspirasi oleh kesulitan real pengguna dengan PC low-end

## 🔥 Fitur Unggulan

- ✅ Kompatibel dengan model GGUF 7B dan 13B (seperti WizardLM)
- ✅ Chat dan Coding AI dalam 1 GUI
- ✅ Tanpa Flask, Tanpa Gradio, hanya `tkinter`
- ✅ Bisa jalan di GTX 1650 Super + RAM 16GB Windows
- ✅ Otomatis hemat token (maks 150-1000 token per respons)
- ✅ Lancar walau sambil nonton YouTube 😎
- ✅ Tidak butuh internet setelah model tersedia (AI Lokal)

---

## 🧠 Model yang Sudah Diuji Jalan Lancar

- `llama-2-7b-chat.Q4_K_M.gguf` ✅ (maks 1000 token per respons)
- `deepseek-coder-6.7b-instruct.Q4_K_M.gguf` ✅ (maks 1000 token per respons)
- `openhermes-2.5-mistral-7b.Q4_K_M.gguf` ✅ (maks 1000 token per respons)
- `mythomist-7b.Q4_K_M.gguf` ✅ (maks 1000 token per respons)
- `wizardlm-13b-v1.2.Q4_K_M.gguf` ✅ (agak berat saat loading karena ram saya 16gb, tapi jalan (maks 150 token)
- Semua model dijalankan dengan backend `llama.cpp`
- Link: (https://github.com/ggml-org/llama.cpp/releases/download/b5899/llama-b5899-bin-win-cpu-x64.zip)

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
