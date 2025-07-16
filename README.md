# offline-ai-chat-coding-gui
GUI Python ringan (Tkinter) untuk menjalankan AI chat &amp; coding dengan model GGUF lokal (Low GUI PYTHON from Tkinter to run AI Chat and Coding)
# 💬 Offline AI Chat & Coding GUI (Super Ringan untuk PC Low-End)

Proyek ini adalah GUI Python ringan (Tkinter) untuk menjalankan model AI lokal (format `.gguf` seperti LLaMA 7B atau WizardLM 13B) di PC Windows biasa dengan GPU seperti **GTX 1650 Super**. Tanpa Flask. Tanpa Gradio. Tanpa ribet. Hanya Python satu file + model!

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
- `wizardlm-13b-v1.2.Q4_K_M.gguf` ✅ (agak berat saat loading, tapi jalan (maks 150 token)
- Semua model dijalankan dengan backend `llama.cpp`
- Link: https://github.com/ggml-org/llama.cpp/releases/download/b5904/llama-b5904-bin-win-cpu-x64.zip

---

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
