🇮🇩 Versi Bahasa Indonesia
# LLaMA.cpp GUI Mode - Python Tkinter Ringan (Kilobyte)

**GUI AI Chat & Coding Offline** berbasis `Llama.cpp` untuk pengguna **low-end PC**. Ringan, cepat, dan tidak membutuhkan Gradio atau Flask.

---

## 🛤️ Perjalanan Proyek

Awalnya, proyek ini dinamai **KoboldCpp GUI Mode**, dirancang untuk mengontrol `koboldcpp.exe` lewat antarmuka Python Tkinter. Namun...

> 😵 **Masalah:** `koboldcpp.exe` tidak stabil di Windows 11 Pro 24H2.  
> 🛠️ **Solusi:** Proyek dialihkan ke backend `llama.cpp`.

Namun menggunakan `llama.cpp` dari source GitHub juga bukan hal mudah:

- Harus **build manual** lewat `cmake`/`ninja`
- CLI `main.exe` hanya bekerja lewat terminal
- Server API belum stabil pada awalnya

💡 **Akhirnya... ditemukan `llama-server.exe`** dari rilis resmi LLaMA.cpp.

---

## ✅ Kenapa Pakai `llama-server.exe`?

- REST API yang stabil (`/completion`, `/healthz`)
- Bisa dipanggil lewat `subprocess` dari GUI Python
- Kompatibel dengan format model `.gguf`
- Cocok untuk multi-tab AI chat dan coding

---

## ✨ Fitur Unggulan GUI Ini

- Ukuran kecil (kilobyte)
- Berbasis Python Tkinter
- Tanpa Gradio / Flask / Streamlit
- Bisa multi-tab chat (Multichat GUI)
- Bisa ganti model `.gguf` secara dinamis
- Bisa integrasi dengan llama-server untuk chat dan assistant coding offline

---

## 🧠 Dibuat Untuk Siapa?

- Pengguna PC kentang / low-end
- Eksperimen AI lokal tanpa internet
- Developer yang ingin GUI AI offline
- Edukasi dan riset AI ringan

---

## 🤝 Kontribusi dan Lisensi

Proyek ini open-source dan dirancang untuk memudahkan publik dalam menjelajahi AI lokal tanpa repot.

Silakan kontribusi, fork, atau laporkan isu. ❤️

---

🇬🇧 English Version
# LLaMA.cpp GUI Mode - Lightweight Python Tkinter (Kilobyte Edition)

An **Offline AI Chat & Coding GUI** built using `Llama.cpp` for **low-end PC users**. Fast, minimal, and free from Gradio or Flask dependencies.

---

## 🛤️ Project Journey

Originally named **KoboldCpp GUI Mode**, this project was intended to interface with `koboldcpp.exe` via a custom Python Tkinter GUI. However...

> 😵 **Problem:** `koboldcpp.exe` refused to work on Windows 11 Pro 24H2  
> 🛠️ **Solution:** Switched backend to `llama.cpp`

But using `llama.cpp` from source wasn’t easy either:

- Required **manual builds** via `cmake`/`ninja`
- `main.exe` worked only via CLI
- Early versions of `server` lacked stable API

💡 **Eventually... `llama-server.exe` was discovered** from official LLaMA.cpp releases.

---

## ✅ Why `llama-server.exe`?

- Stable REST API (`/completion`, `/healthz`, etc.)
- Easy subprocess call from Python
- Compatible with `.gguf` model format
- Supports multitab AI chat and code assistant features

---

## ✨ Highlighted Features

- Tiny file size (kilobyte)
- Built with Python Tkinter
- No Gradio / Flask / Streamlit
- Multitab chat (Multichat GUI)
- Dynamic `.gguf` model loading
- Full offline AI chat & coding assistant

---

## 🧠 Who’s It For?

- Low-end / potato PC users
- Offline AI experiments
- Devs who want simple AI GUI
- Educational and lightweight research purposes

---

## 🤝 Contributions & License

This project is open-source and built to empower public access to lightweight local AI.

Feel free to fork, contribute, or report issues. ❤️
