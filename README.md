# 🧠 Offline AI Chat & Coding GUI (Rakyat Edition)
GUI Python ringan (Tkinter) untuk menjalankan AI chat &amp; coding dengan model GGUF lokal (Low GUI PYTHON from Tkinter to run Offline AI Chat and Coding)

🇮🇩 Bahasa Indonesia:

🎉 Pertama kalinya dalam sejarah: Model AI 13B (Q4_K_M) berhasil dijalankan hanya dengan RAM 16GB — tanpa GPU, tanpa web server, cukup dengan GUI Python ukuran 10KB! Bukti nyata efisiensi maksimal 💪
⚠️ Catatan RAM 16GB:

Meskipun sistem Anda 16GB, Windows dan Office 2024 bisa menyita 3–5 GB di background. Namun, GUI ini tetap dapat menjalankan model 7B - 13B Q4_K_M. Tanpa GPU, tanpa swap besar.

## ⚖️ Perbandingan GUI Python 6KB-16kb vs WebUI Berat

| **Fitur / Aspek**                | 🐍 **GUI Python 6KB-16KB (tkinter)** | 🌐 **WebUI (Gradio/Oobabooga dll.)** |
|----------------------------------|----------------------------------|--------------------------------------|
| ✅ Ukuran File GUI               | **10 KB**                        | > **100 MB**                         |
| ⚙️ Bahasa Pemrograman            | Python (tkinter native)          | Python + Gradio + JS + HTML          |
| 🧠 Model yang Diuji              | 7B, 13B (Q4_K_M)                 | 7B, 13B                               |
| 🧮 RAM Minimum (7B - 13B Q4_K_M)      | **12.3 – 15.5 GB**               | **> 18 – 20 GB**                      |
| 🖥️ CPU Pengujian                | i5-9400F (no GPU)                | Biasanya pakai GPU / CPU kuat        |
| 🚀 Waktu Load Model 13B         | **35 – 40 detik**                | Bisa > 1 menit                       |
| 🟢 RAM Saat Idle                | 12.1 – 12.4 GB                   | > 15 GB                               |
| 🛠️ Konfigurasi Awal            | Hanya 1 file `.py`               | Banyak dependensi dan setup venv     |
| 📉 Risiko Error/Crash           | **Sangat rendah / stabil**       | Kadang freeze / error token          |
| 🪄 Token yang Diuji Lancar      | 5000 token                | Bergantung setting/model             |
| 📡 Server Web                   | **Tidak perlu**                  | Wajib buka server (http/websocket)   |
| 🧩 Dukungan Plugin              | Manual (custom)                  | Banyak tapi berat                    |
| 💬 Chat & Coding Mode           | ✅ Sangat cocok                  | ✅ Cocok, tapi lebih berat            |
| 🤯 Respons Not Responding?     | Hanya saat proses berat dan tanpa crash         | Sering delay jika RAM kritis         |

🇬🇧 English Version:

🎉 First time in history: A 13B (Q4_K_M) AI model runs smoothly with just 16GB RAM — no GPU, no web server, only a 6KB - 16kb Python GUI! Proof of ultimate efficiency 💪

⚠️ 16GB RAM Note:

Even if your system has 16GB, Windows and Office 2024 can take up 3–5GB in the background. However, this GUI can still run the 7B - 13B Q4_K_M model efficiently. No GPU, no large swap requirements.

> 🇮🇩 This project is primarily documented in Indonesian.
> 🇬🇧 English overview is provided below.

## ⚖️ Comparison: Python GUI (6–16KB) vs Heavy WebUIs

| **Feature / Aspect**             | 🐍 **Python GUI 6KB-16KB (Tkinter)**       | 🌐 **WebUIs (Gradio/Oobabooga, etc.)**     |
|:----------------------------------|:----------------------------------------|:--------------------------------------------|
| ✅ **GUI File Size**              | **10 KB**                               | > **100 MB**                                 |
| ⚙️ **Programming Language**       | Native Python (Tkinter)                 | Python + Gradio + JS + HTML                  |
| 🧠 **Tested Model Types**         | 7B, 13B (Q4_K_M)                        | 7B, 13B                                       |
| 🧮 **Minimum RAM (7B–13B Q4_K_M)**| **12.3 – 15.5 GB**                      | **> 18 – 20 GB**                              |
| 🖥️ **Test CPU**                   | i5-9400F (no GPU)                       | Typically uses GPU or high-end CPU           |
| 🚀 **Model Load Time (13B)**      | **35 – 40 seconds**                     | Can take > 1 minute                          |
| 🟢 **Idle RAM Usage**             | 12.1 – 12.4 GB                          | > 15 GB                                       |
| 🛠️ **Initial Setup**             | Single `.py` file only                  | Many dependencies and venv setup             |
| 📉 **Error / Crash Risk**         | **Very low / stable**                   | Sometimes freezes or token errors            |
| 🪄 **Smooth Token Output Tested** | 5000 tokens                             | Varies by settings/model                     |
| 📡 **Web Server Required**        | **Not needed**                          | Required (HTTP/websocket server)             |
| 🧩 **Plugin Support**             | Manual (customizable)                   | Many, but resource-heavy                     |
| 💬 **Chat & Coding Mode**         | ✅ Highly suitable                      | ✅ Suitable, but heavier                      |
| 🤯 **"Not Responding" Behavior**  | Only during heavy loads, no crash       | Frequent delays when RAM is low              |


## 📸 Screenshot GUI From llamacpp_gui_combinedv9.py

![Model Loaded Screenshot](https://github.com/satrianovian20/offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202025-07-18%20160408.png)

## 📸 Screenshot GUI From llamacpp_gui_mode.py (Experiment GUI)

![Model Loaded Screenshot](https://github.com/satrianovian20/offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202025-07-19%20110119.png)

## 📸 Screenshot Chat From GUI
![Model Loaded Screenshot](https://github.com/satrianovian20/offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202025-07-18%20170753.png)

## 📸 Second Screenshot Chat From GUI
![Model Loaded Screenshot](https://github.com/satrianovian20/offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202025-07-18%20170809.png)

---

## 🇮🇩 Bahasa Indonesia

GUI lokal untuk LLaMA.cpp:

📁 Cocok untuk chat dan coding!

💬 Contoh jawaban untuk user awam:
“GUI ini nggak ngebatesin kemampuan AI-nya. Kamu bisa atur output token sesuai kemampuan RAM PC kamu. Misal RAM kamu cuma 8GB, kamu bisa atur max token ke 150 biar tetap lancar. Kalau RAM kamu 16GB, bisa gaspol sampai 10.000 token. Jadi fleksibel, ringan, dan tetap powerful!”

## 📸 Screenshot (Model berhasil dimuat di RAM 16GB)

![Model Loaded Screenshot](https://github.com/satrianovian20/offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202025-07-17%20114247.png)

## 📸 Screenshot (Model berhasil dimuat di RAM 16GB)

![Model Loaded Screenshot](https://github.com/satrianovian20/offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202025-07-17%20125025.png)

📸 Bukti: Sudah dilampirkan screenshot dan log lengkap di repo

💡 Kesimpulan Buat Pengguna GUI:
Kalau user punya RAM:

8GB: Deepseek 1.3B atau TinyLlama cukup, tapi jangan berharap jawaban super.

12GB–16GB: Langsung lompat ke Mistral 7B atau DeepSeek-Coder 6.7B.

>16GB: Bisa gas model 13B seperti Yi-13B, OpenHermes 13B, dll.

Optimalitas GUI Python 6KB-10kb:
✅ GUI Python 10KB Terbukti Optimal dan Stabil

GUI ini hanya berukuran 10KB namun sudah terbukti mampu menangani model AI lokal besar seperti 7B dan 13B tanpa eror, crash, atau freeze, bahkan saat dijalankan di PC tanpa GPU.

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
⚙️ GUI ringan (6KB-16kb Python script)	✅ Terpakai dengan lancar dan tanpa crash karena adanya fitur otomatis yang melakukan optimaliasi ram dan cpu

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

DeepSeek Coder 7B

Nous Hermes 13B (Q4_K_M)

LLaMA 13B (Q4_K_M)

❓ RAM saya cuma 8GB, bisa jalan?
Bisa, asal model yang dipilih sesuai. Gunakan model kecil seperti:

TinyLlama 1.1B

DeepSeek Coder 1.3B

Atur max_tokens di GUI agar tidak melebihi kapasitas RAM kamu.

❓“Saya masih nggak percaya GUI ini bisa jalanin model 13B cuma dengan RAM 16GB. Beneran bisa?”
💬 “Coba sendiri aja bro, repo udah public kok 😎”

❓“Emang GUI-nya ringan banget ya?”
✅ Iya. Ukuran file .py cuma 10KB. Gak ada embel-embel web server, backend rumit, atau library berat.

❓“Bisa crash gak pas load model besar?”
🚫 Selama sistem kamu stabil dan swap file aktif, hampir nggak pernah crash. Bahkan log menunjukkan performa tetap normal walau RAM di atas 15GB pas awal load.

❓“Ada buktinya?”
📸 Sudah ada screenshot dan log di folder docs/session-logs/ dan docs/screenshots/.

❓“Kalau saya nggak percaya tetap?”
😎 Silakan buktikan sendiri. Semuanya open source. Mau test sendiri? Silakan kloning repo-nya sekarang.

Catatan Jujur (untuk README atau FAQ)
💡 Saat ini, pengujian terbatas pada model hingga 13B (Q4_K_M) karena sistem hanya memiliki RAM 16GB tanpa GPU.
Namun, GUI Python 6KB-16KB ini berhasil menangani model besar tersebut secara stabil dan efisien, yang biasanya tidak mungkin dilakukan tanpa sistem high-end.
Untuk model 33B ke atas, uji coba akan dilakukan jika tersedia perangkat dengan RAM lebih besar. Ditambah bisa melakukan optimaliasi ram dan cpu.

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
| llamacpp_gui_combinedv8.py| ✅       | + Auto-save load model berfungsi        |
| llamacpp_gui_combinedv9.py| ✅ Terbaru       | + Fitur Rakyat Mode di menu pengaturan dan prompt hemat ram di samping mulai Llama Server        |
| llamacpp_rakyatmode.py| ✅ Terbaru | + --ctx-size default ke 1024 + Lowram        |
| llamacpp_gui_mode.py      | ✅ Eksperimen + Stabil | Mode GUI ringan eksperimen + load model 13 Q4_K_M               |
| llamacpp_gui_modev2.py    | ✅        | Kombinasi GUI mode dengan layout sistem  |

## 💡 Syarat Minimum PC

| Komponen         | Minimum                    |
|------------------|-----------------------------|
| Prosesor         | i3/i5 Gen 8+ (atau Ryzen 3+) |
| RAM              | 8-16 GB (direkomendasikan 32 GB - 64 gb)|
| GPU              | GTX 1650 / setara (VRAM 4GB) |
| OS               | Windows 10/11 64-bit        |
| Python           | 3.10+                       |

---

## 📦 Cara Install & Jalankan

### 1. Download Python
Install Python 3.10 dari https://www.python.org/downloads/release/python-3100/

> ✅ Centang “Add Python to PATH” saat install!
> pip install requests
> Jalankan gui python dengan klik dua kali

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

Bisa sambil nonton YouTube dan nonton video musik 720p 😄

💬 Kalau kamu juga merasakan manfaatnya, bantu bintang repo ini!
Supaya tidak ada lagi yang pusing karena “AI-nya gak bisa jalan...” 😅

---

## 🌐 English (International)

🇬🇧 English Version:

🖥️ Local GUI for LLaMA.cpp:

📁 Perfect for Chat and Coding!

💬 Example Explanation for Non-Technical Users:

"This GUI doesn’t limit the AI’s capabilities. You can adjust the output tokens according to your PC’s RAM capacity. For example, if you only have 8GB RAM, set max tokens to 150 to stay smooth. If you have 16GB RAM, you can go all out up to 10,000 tokens. So it’s flexible, lightweight, and still powerful!"

📸 Screenshot (Model successfully loaded in 16GB RAM)





📸 Proof: Screenshots and complete logs are provided in the repo

💡 Summary for GUI Users:

If you have RAM:

8GB: Deepseek 1.3B or TinyLlama is enough (basic answers)

12GB–16GB: Jump directly to Mistral 7B or DeepSeek-Coder 6.7B



16GB: Run 13B models like Yi-13B, OpenHermes 13B, etc.

✅ Python GUI 6KB–10KB Optimization:

✅ Proven optimal and stable even for large local AI models (7B, 13B)

✅ No GPU needed

✅ No crashes or freezes during usage

📌 Highlights:

✔️ Ultra lightweight (10KB only)

✔️ No complicated installation required

✔️ Uses llama.cpp as backend (GGUF compatible)

✔️ Stable RAM usage (~12.3GB idle)

✔️ 13B model loads without error

✔️ Responsive GUI

✔️ Stable output even for large models

💡 This GUI is even more optimized than many popular UIs out there. It makes smart use of resources and is ideal for low-end PC users wanting to use large local models.

📌 Bonus Visual Explanation (Suggested Flowchart)

[Start GUI]
  -> [Load Model]
       -> RAM = 15.5GB
       -> CPU = 60%
  -> [Model Idle]
       -> RAM = 12.3GB
       -> CPU = 5%
  -> [Prompt Received]
       -> CPU = 100%
  -> [Generate Response]
       -> Output OK
  -> [Idle Again]
       -> RAM steady
       -> CPU low

✅ Documentation Status (Indonesian Version):

Evidence Element

Status

📜 Session logs

✅ Available

🖼️ Screenshot model loaded

✅ Available

🖼️ Screenshot idle

✅ Available

🧪 13B Model (Q4_K_M) Tested

✅ Yes

⚙️ Lightweight GUI (6KB-16KB)

✅ Works well with auto RAM/CPU optimization

✅ FAQ — General Questions (Trust Booster Edition)

Q: Can this GUI really run 13B models without GPU?

A: Yes! Tested with llama-2-13b-chat.Q4_K_M.gguf on:

💻 CPU: Intel i5-9400F (no iGPU)

🧠 RAM: 16GB DDR4

⚙️ Backend: llama.cpp

📦 GUI: 10KB Python script

Q: Is there any real proof?

A: ✅ Screenshots and logs in docs/screenshots/ and docs/session-logs/

Q: Is the GUI heavy?

A: 🚫 No. It’s only 10KB. No heavy dependencies like Gradio or Electron.

Q: Is it offline and secure?

A: ✅ Yes. No servers, no tracking. 100% local and offline.

Q: Can I use other models (7B, 8B, 13B)?

A: ✅ Yes! Tested with:

Mistral 7B

DeepSeek Coder 6.7B / 7B

Nous Hermes 13B (Q4_K_M)

LLaMA 13B (Q4_K_M)

Q: I only have 8GB RAM. Can I still use it?

A: ✅ Yes, just use smaller models like TinyLlama 1.1B or DeepSeek 1.3B.

Q: I still don’t believe 13B can run on 16GB RAM!

A: 😎 Try it yourself. The repo is public!

Q: Is the GUI really that light?

A: ✅ Yep. Just 10KB .py file. No web server, no backend, no bloat.

Q: Will it crash with big models?

A: 🚫 Rarely. As long as your system is stable and has swap active, it's fine.

Q: Is there proof?

A: 📸 Yes. Logs and screenshots included.

Q: Still not convinced?

A: 😎 Clone it and prove it yourself. It’s all open source.

📌 Honest Note (README or FAQ Section)

💡 So far, tests have been conducted up to 13B (Q4_K_M) because the system has only 16GB RAM and no GPU.
But this 6–16KB Python GUI has proven to run large models efficiently without crashes.

Tests for 33B models will be done when more RAM is available.

🤝 Contributions & Credits

👨‍💻 Creator: [satrianovian20] — Offline GUI with Tkinter

✍️ AI Scripting & Bug Fixing: ChatGPT

🔁 Models: Meta (LLaMA), WizardLM, open-source community

💡 Inspired by real low-end PC users struggling with bloated UIs

📦 Tested GUI Versions

GUI File Version

Status

Key Features

llamacpp_gui_combined.py

✅ Stable

Initial combined Chat + System GUI

llamacpp_gui_combinedv2.py

✅

Model & prompt settings added

llamacpp_gui_combinedv3.py

✅

Minor bug fixes, cleaner UI

llamacpp_gui_combinedv4.py

✅

+ Logging and auto model load

llamacpp_gui_combinedv5.py

✅

+ Chat history + system prompt

llamacpp_gui_combinedv6.py

✅

+ Theme mode & advanced settings

llamacpp_gui_combinedv7.py

✅

+ Auto-save sessions, repeat_penalty config

llamacpp_gui_combinedv8.py

✅

+ Auto-load model fix

llamacpp_gui_combinedv9.py

✅ Latest

+ Rakyat Mode menu + memory-saving prompt

llamacpp_rakyatmode.py

✅ Latest

+ --ctx-size default 1024 + LowRAM mode

llamacpp_gui_mode.py

✅ Stable

Experimental GUI Mode, loads 13B Q4_K_M

llamacpp_gui_modev2.py

✅

GUI Mode + layout integration

💡 Minimum System Requirements

Component

Minimum Specs

Processor

i3/i5 Gen 8+ or Ryzen 3+

RAM

8–16 GB (32GB–64GB recommended)

GPU

GTX 1650 or equivalent (VRAM 4GB)

OS

Windows 10/11 64-bit

Python

Version 3.10+

🚀 How to Install & Run

1. Download Python

Install Python 3.10 from: https://www.python.org/downloads/release/python-3100/

✅ Check "Add Python to PATH" during installation!

Install required dependency:

pip install requests

Run the Python GUI by double-clicking the .py file.

💖 Support This Project

If this project helps you and you'd like to support its development:

- 💸 [Saweria](https://saweria.co/satrianovian20)
- ☕ [PayPal](https://www.paypal.com/paypalme/satrianovian)

Thank you so much for your support! 🙏

☕ Final Words

This project was born out of frustration and turned into innovation.

I used to struggle with WebUIs that refused to run...

So I:

Built my own GUI

Only used 1 Python file for AI Chat & Coding

Still watch YouTube and 720p music videos while it's running 😄

💬 If this project helps you too, please star the repo!
So nobody ever says again, "My AI won’t run..." 😅
