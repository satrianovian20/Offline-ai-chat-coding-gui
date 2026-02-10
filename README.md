# 🧠 Offline AI Chat & Coding GUI (Rakyat Edition)
## 🚧 Project Under Maintenance

This repository is currently under **major refactoring and restructuring**.

Some features, screenshots, and demo videos are **temporarily removed or outdated** while the core engine and architecture are being stabilized.

### What’s happening?
- Internal engine refactor (workers, dispatcher, CLI)
- Improving stability and performance
- Reworking installation and model management flow
- Preparing cleaner documentation and examples

### Current status
- The project **is not abandoned**
- Active development is in progress
- APIs, commands, and behavior may change

Screenshots, demo videos, and detailed usage guides will be re-added once the refactor is complete.

Thank you for your patience 🙏
## 🚧 Proyek Sedang Dalam Perbaikan

Repository ini sedang berada dalam tahap **perombakan dan perbaikan besar-besaran**.

Beberapa fitur, screenshot, dan video demo **sementara dihapus atau belum diperbarui** karena engine dan arsitektur internal sedang distabilkan.

### Apa yang sedang dikerjakan?
- Refactor engine internal (worker, dispatcher, CLI)
- Peningkatan stabilitas dan performa
- Perbaikan alur instalasi dan manajemen model
- Penyiapan dokumentasi dan contoh penggunaan yang lebih rapi

### Status saat ini
- Proyek **tidak ditinggalkan**
- Masih aktif dikembangkan
- Perintah, API, dan perilaku program bisa berubah

Screenshot, video demo, dan panduan lengkap akan ditambahkan kembali setelah proses perbaikan selesai.

Terima kasih atas pengertiannya 🙏

## 🇮🇩 Bahasa Indonesia
⚠️ Repository ini adalah monorepo yang berisi berbagai aplikasi AI offline yang diimplementasikan menggunakan berbagai framework Python dan platform yang berbeda. Repo ini adalah lab + museum hidup. Beberapa project masih eksperimen, beberapa sudah jadi produk.
Fokus utama:

- AI tanpa internet
- GUI ringan & mandiri
- Bisa jalan di PC rakyat tanpa cloud, API key, atau langganan

## 🇬🇧 English
⚠️ This repository is a monorepo containing multiple offline AI applications implemented across different Python frameworks and platforms. This monorepo serves as both an experimental lab and an archive of offline AI GUI projects at various stages of development.
Focused on:

- Offline-first AI
- Lightweight desktop GUIs
- No cloud, no API keys, no subscriptions

-------------------------------

🔥 Moto & Project Philosophy

GUI Rakyat Edition
- Ringan, Garang, Tak Terbendung
- Anti-Bluescreen Framework
- The GUI That Refused to Die
- Born in CPU Hell, Forged by Low-End Desperation
- Stress-Tested Terminator AI GUI
- Powered by Bugs, Sustained by Chaos 🐞💀

⭐ Cloned already?
Don’t forget to ⭐ if this project made your CPU smile 😄

-------------------------------------------

🇮🇩 This project is primarily documented in Indonesian. 🇬🇧 English overview is provided below. “This project is based on the original GUI by Satria Novian

-------------------------------------------  

## 💖 Dukung Proyek Ini

Jika kamu merasa proyek ini bermanfaat dan ingin mendukung pengembangannya, kamu bisa berdonasi melalui:
👉 Untuk mendapatkan source code & file GUI:

- 💸 [Saweria](https://saweria.co/satrianovian20)
- ☕ [PayPal](https://www.paypal.com/paypalme/satrianovian)


**Bayar dulu, baru dapat akses download**
Terima kasih banyak atas dukungannya! 🙏

-------------------------------------------  

## 💖 Support This Project
If this project helped you and you'd like to support its development, you can donate via:
👉 To get the source code, you can donate via:

- 💸 [Saweria](https://saweria.co/satrianovian20)
- ☕ [PayPal](https://www.paypal.com/paypalme/satrianovian)

**Pay first, then receive download access**
Thank you so much for your support! 🙏

-------------------------------------------

# 📌 Model AI yang sudah diuji / Tested AI Model

| No | Nama Model GGUF                                | Ukuran Quant | RAM/VRAM/CPU yang Digunakan         | OS & Kondisi Tambahan                                    | Status GUI            |
|----|------------------------------------------------|--------------|----------------------------|---------------------------------------------------------|-----------------------|
| 1  | luna-ai-llama2-uncensored.Q4_0.gguf            | Q4_0         | ±11.6 GB of 16GB           | Windows 11 pro 24H2 + Office 2024 + music & anime video | Stable & Smooth       |
| 2  | Meta-Llama-3-8B-Instruct.Q8_0.gguf             | Q8_0         | ±10.8 GB of 16GB           | Windows 11 pro 24H2 + Office 2024 + music & anime video | Stable & Smooth       |
| 3  | WizardLM-13B-Uncensored.Q5_K_M.gguf            | Q5_K_M       | 12.6 GB of 16 GB           | Windows 11 pro 24H2 + Office 2024                       | Tested + Stable & Smooth |
| 4  | wizardcoder-python-13b-v1.0.Q5_K_M.gguf        | Q5_K_M       | 12.6 GB of 16 GB           | Windows 11 pro 24H2 + Office 2024                       | Tested + Stable & Smooth |
| 5  | All 7B                                         | Q4_K_M       | ≤11.5 GB of 16GB           | Windows 11 pro 24H2 + Office 2024 + Chrome + music video 720p | Stable & Smooth  |
| 6  | All 13B (Kecuali Yi 13B)                       | Q4_K_M       | ≤15.5 GB of 16GB           | Windows 11 pro 24H2 + Office 2024 + Chrome + music video 720p | Stable & Smooth  |
| 7  | deepseek-coder-7b-instruct-v1.5-Q8_0.gguf      | Q8_0         | 10.8 GB of 16GB            | Windows 11 pro 24H2 + Office 2024                       | Stable & Smooth       |
| 8  | deepseek-coder-1.3b-instruct.Q4_0.gguf         | Q4_0         | 4 GB of 16GB               | Windows 11 pro 24H2 + Office 2024                       | Stable & Smooth       |
| 9  | codellama-13b.Q6_K.gguf                        | Q6_K         | ≤15.4 GB of 16GB           | Windows 11 pro 24H2 + Office 2024 + Chrome + Notepad++  | Stable & Smooth       |
| 10 | starcoder2-15b-Q5_K_M (1).gguf                 | Q5_K_M       | ≤15.5 GB of 16GB           | Windows 11 pro 24H2 + Office 2024 + Chrome + Notepad++  | Stable & Smooth       |
| 11 | DeepSeek-Coder-V2-Lite-Instruct-Q5_K_M.gguf    | Q5_K_M       | ≤15.5 GB of 16GB           | Windows 11 pro 24H2 + Office 2024 + Chrome + Notepad++  | Stable & Smooth       |
| 12 | Llama-3-16B.Q5_K_M.gguf                        | Q5_K_M       | ≤15.5 GB of 16GB           | Windows 11 pro 24H2 + Office 2024 + Chrome + Notepad++  | Stable & Smooth       |
| 13 | orcamaidxl-17b-32k.Q5_K_M.gguf                 | Q5_K_M       | ≤15.5 GB of 16GB           | Windows 11 pro 24H2 + Office 2024 + Chrome              | Stable & Smooth       |
| 14 | llava-v1.5-13b-Q8_0.gguf + mmproj                       | Q8_0         | ≤15.5 GB of 16GB           | Windows 11 pro 24H2 + Office 2024 + Chrome + Notepad + Notepad++ | Stable & Smooth |
| 15 | InternVL3-8B-Instruct-UD-Q8_K_XL.gguf          | Q8_K_XL      | ≤14.2 GB of 16GB           | Windows 11 pro 24H2 + Office 2024 + Chrome + Notepad + Notepad++ | Stable & Smooth |
| 16 | InternVL3-14B-Instruct-Q6_K_XL.gguf               | Q6_K_XL         | ≤15.5 GB of 16GB           | Windows 11 pro 24H2 + Office 2024 + Chrome + Notepad + Notepad++ | Stable & Smooth |
| 17 | mradermacher-InternVL3.5-14BQ6_K.gguf + mmproj               | Q6_K         | ≤15.5 GB of 16GB           | Windows 11 pro 24H2 + Office 2024 + Chrome + Notepad + Sublime text | Stable & Smooth |
| 18 | mradermacher-InternVL3_5-8BQ8_0.gguf + mmproj               | Q8_0         | ≤14.5 GB of 16GB           | Windows 11 pro 24H2 + Office 2024 + Chrome + Notepad + Sublime text | Stable & Smooth |
| 19 | Mistral-Small-3.2-24B-Instruct-2506-UD-Q4_K_XL.gguf + mmproj               | Q4_K_XL         | ≤15.7 GB of 16GB           | Windows 11 pro 24H2 + Office 2024 + Chrome + Notepad + Sublime text | Stable & Smooth |
| 20 | Codestral-22B-v01-Q4_K_M.gguf               | Q4_K_M         | ≤15.7 GB of 16GB           | Windows 11 pro 24H2 + Office 2024 + Chrome + Notepad + Sublime text | Stable & Smooth |
| 21 | Codestral-RAG-19B-Pruned-Q5_K_M.gguf               | Q5_K_M         | ≤15.7 GB of 16GB           | Windows 11 pro 24H2 + Office 2024 + Chrome + Notepad + Sublime text | Stable & Smooth |
| 22 | anything-v4.5-pruned-fp16.safetensors               | SD 1.5 + FP16         | ≤4 GB of 4GB           | Windows 11 pro 24H2 + Office 2024 + Chrome + Notepad + Sublime text | Stable & Smooth |
| 23 | DreamShaper_8_pruned.safetensors               | SD 1.5 + FP16         | ≤4 GB of 4GB           | Windows 11 pro 24H2 + Office 2024 + Chrome + Notepad + Sublime text | Stable & Smooth |
| 23 | realisticVisionV60B1_v51VAE.safetensors               | SD 1.5 + FP16         | ≤4 GB of 4GB           | Windows 11 pro 24H2 + Office 2024 + Chrome + Notepad + Sublime text | Stable & Smooth |
| 23 | level4_v50BakedVAEFp16.safetensors               | SD 1.5 + FP16         | ≤4 GB of 4GB           | Windows 11 pro 24H2 + Office 2024 + Chrome + Notepad + Sublime text | Stable & Smooth |
| 24 | majicmixRealistic_v7.safetensors               | SD 1.5 + FP16         | ≤4 GB of 4GB           | Windows 11 pro 24H2 + Office 2024 + Chrome + Notepad + Sublime text | Stable & Smooth |
| 25 | MeinaPastelV2-bakedVAE-pruned.safetensors               | SD 1.5 + FP16         | ≤4 GB of 4GB           | Windows 11 pro 24H2 + Office 2024 + Chrome + Notepad + Sublime text | Stable & Smooth |
| 26 | meinamix_v12Final.safetensors               | SD 1.5 + FP16         | ≤4 GB of 4GB           | Windows 11 pro 24H2 + Office 2024 + Chrome + Notepad + Sublime text | Stable & Smooth |
| 27 | realisticVisionV60B1_v60B1VAE.safetensors               | SD 1.5 + FP16         | ≤4 GB of 4GB           | Windows 11 pro 24H2 + Office 2024 + Chrome + Notepad + Sublime text | Stable & Smooth |
| 28 | Anything-v4.5-pruned-mergedVae.safetensors.safetensors               | SD 1.5 + FP16         | ≤4 GB of 4GB           | Windows 11 pro 24H2 + Office 2024 + Chrome + Notepad + Sublime text | Stable & Smooth |
| 29 | counterfeitV30_v30.safetensors               | SD 1.5 + FP16         | ≤4 GB of 4GB           | Windows 11 pro 24H2 + Office 2024 + Chrome + Notepad + Sublime text | Stable & Smooth |
| 30 | AnythingXL_xl.safetensors               | SD XL + FP16         | Intel I5-9400F           | Windows 11 pro 24H2 + Office 2024 + Chrome + Notepad + Sublime text | Stable & Smooth |
| 31 | realvisxlV50_v50Bakedvae.safetensors               | SD XL + FP16         | Intel I5-9400F           | Windows 11 pro 24H2 + Office 2024 + Chrome + Notepad + Sublime text | Stable & Smooth |
| 32 | dreamshaperXL_alpha2Xl10.safetensors               | SD XL + FP16         | Intel I5-9400F           | Windows 11 pro 24H2 + Office 2024 + Chrome + Notepad + Sublime text | Stable & Smooth |
| 33 | aniverseXL_v40.safetensors               | SD XL + FP16         | Intel I5-9400F           | Windows 11 pro 24H2 + Office 2024 + Chrome + Notepad + Sublime text | Stable & Smooth |
| 33 | aniversePonyXL_v60.safetensors               | SD XL + FP16         | Intel I5-9400F           | Windows 11 pro 24H2 + Office 2024 + Chrome + Notepad + Sublime text | Stable & Smooth |
| 34 | animagineXLV31_v31.safetensors               | SD XL + FP16         | Intel I5-9400F           | Windows 11 pro 24H2 + Office 2024 + Chrome + Notepad + Sublime text | Stable & Smooth |
| 35 | hyper3dHighlyDetailed3D_v1.safetensors               | SD XL + FP16         | Intel I5-9400F           | Windows 11 pro 24H2 + Office 2024 + Chrome + Notepad + Sublime text | Stable & Smooth |
| 36 | counterfeitV30_v30.safetensors               | SD 1.5 + FP32         | ≤4 GB of 4GB           | Windows 11 pro 24H2 + Office 2024 + Chrome + Notepad + Sublime text | Stable & Smooth |
| 37 | revAnimated_v2RebirthVAE.safetensors               | SD 1.5 + FP32         | ≤4 GB of 4GB           | Windows 11 pro 24H2 + Office 2024 + Chrome + Notepad + Sublime text | Stable & Smooth |

-------------------------------------------

# Portfolio Showcase (Full Production Ready & R&D Lineage)
# 📸 Screenshot:

## Installed Portfolio
![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-02-02%20201410.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-02-02%20201419.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-02-02%20201428.png)

ChatCPP Template

Get it here 👉 [Kilashare](https://kilashare.blogspot.com/)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-01-18%20201817.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-01-18%20201832.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-01-22%20191834.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-01-22%20192449.png)

ChatCPP Multi Engine Worker

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-02-06%20091216.png)

ChatCPP Audio To Text Generator Worker

ChatCPP Video To Text Generator Worker

ChatCPP Huggingface OCR Worker

ChatCPP Mask Generator Worker

ChatCPP Image Inpainting Worker

ChatCPP Huggingface Gated Model Downloader Worker

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-02-08%20165051.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-02-08%20165109.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-02-08%20173143.png)

ChatCPP Huggingface Gated Model Folder Builder

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-02-04%20193917.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-02-04%20193936.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-02-06%20105517.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-02-07%20105411.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-02-07%20111452.png)

ChatCPP Offline HuggingFace Model Loader Worker

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-02-02%20213448.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-02-02%20201034.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-02-02%20201656.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-02-02%20201949.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-02-02%20205928.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-02-02%20210304.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-02-02%20210420.png)

ChatCPP Microsoft SAPI Text To Speech Worker

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-01-31%20130625.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-01-31%20130642.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-01-31%20132720.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-02-09%20191314.png)

ChatCPP Microsoft SAPI Text To Speech Manager

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-01-31%20164846.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-01-31%20164902.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-01-31%20165945.png)

ChatCPP Text To Speech With Translation Worker

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-02-02%20210857.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-01-31%20112105.png)

ChatCPP Text To Speech Worker

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-02-02%20205928.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-01-31%20112524.png)

ChatCPP Multimodal Video Frame to Text Caption Worker

ChatCPP Multimodal Image to Text Caption Worker

ChatCPP Multimodal Image to Text Generator Worker

ChatCPP Text Generator Worker 

ChatCPP SD 1.5 Video Generator Worker (SD 1.5 Only)
![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-01-27%20080224.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/output.gif)

ChatCPP Translator Suite Ttkbootstrap (CLI Worker)
![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-01-20%20194151.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-01-20%20194200.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-01-20%20194209.png)

ChatCPP Translator Worker
![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-02-02%20210304.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-02-02%20210420.png)

ChatCPP Image Converter Worker
![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-01-23%20110756.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-01-23%20163158.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-02-01%20092857.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-02-01%20092951.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-02-01%20102314.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-02-01%20102323.png)

ChatCPP SD 1.5 Image Generator Worker (SD 1.5 Only)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-01-30%20183544.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-01-30%20183518.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-01-30%20195906.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-01-30%20195924.png)

ChatCPP SD Image Generator Worker (SD 1.5, SD XL 1.0, Pony XL, Illustrious)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-01-30%20201539.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-01-30%20201552.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-01-31%20085101.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-01-31%20085147.png)

ChatCPP OCR Worker
![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-01-03%20180118.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-01-03%20180509.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-01-11%20112152.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-01-11%20112256.png)

ChatCPP Argos Worker
![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-01-05%20205132.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-01-05%20205230.png)

ChatCPP Argos Manager Engine
![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-01-02%20134944.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-01-02%20135110.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-01-02%20140041.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-01-02%20140041.png)

ChatCPP Whisper Worker

Get it here 👉 [Kilashare](https://kilashare.blogspot.com/2026/01/chatcpp-whisper-worker.html)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-02-01%20091012.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-01-09%20172132.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-01-09%20172151.png)

ChatCPP SuperAPP (Ttkbootstrap Edition)


ChatCPP Translator (Flask Edition)


ChatCPP Translator (Ttkbootstrap Edition)


ChatCPP Translator (Pywebview Edition)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-01-11%20133351.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-01-11%20133401.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-01-11%20133409.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-01-11%20133428.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-01-11%20133417.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-02-03%20214844.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-02-03%20215505.png)

ChatCPP Translator (FastAPI Edition)


ChatCPP Llama MultiCode Editor (Tkinter Edition)

Get it here 👉 [Kilashare](https://kilashare.blogspot.com/2025/11/chatcpp-llama-multicode-editor-tkinter.html)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-02-10%20115723.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-02-10%20115808.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-02-10%20115830.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-02-10%20115905.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-02-10%20115921.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-02-10%20115946.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-02-10%20120001.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-02-10%20120011.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-02-10%20120027.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-02-10%20120038.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-02-10%20120128.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-02-10%20120336.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-02-10%20120406.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-02-10%20120455.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-02-10%20120543.png)

ChatCPP LlamArgos Tkinter GUI


ChatCPP LlamArgos Ttkbootstrap GUI
![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-01-22%20201055.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-01-22%20201108.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-01-22%20201529.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-01-22%20201719.png)

ChatCPP Chatbot Ttkbootstrap Multichat AI GUI - Multitab


ChatCPP Chatbot Tkinter SIngle Chat AI GUI
![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-01-20%20151608.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-01-20%20151622.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-01-20%20151632.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-01-20%20151646.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-01-20%20151704.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-01-20%20153258.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-01-20%20153320.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-02-05%20160003.png)

ChatCPP Chatbot Tkinter MultiChat AI GUI

ChatCPP Chatbot Tkinter Multimodal AI GUI

ChatCPP Phask (Flask + Php) Multichat AI WebUI

Get it here 👉 [Kilashare](https://kilashare.blogspot.com/2025/09/llamacpp-server-multichat-flask-webui-v3.html)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-01-05%20191526.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-01-05%20191548.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-01-05%20191610.png)

ChatCPP Phask (Flask + Php) Chatbot Single Tab AI WebUI
![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-01-06%20092934.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-01-06%20095719.png)

![Screenshot](https://github.com/satrianovian20/Offline-ai-chat-coding-gui/blob/main/doc/Screenshot%202026-01-06%20100502.png)

ChatCPP GradioWeb (Gradio) Multichat AI WebUI


ChatCPP TkinterWeb Multisession AI GUI


ChatCPP TkinterWeb Multitab + Multisession AI GUI - Ttkbootstrap


ChatCPP Multichat (Multitab + Multisession) TkBootstrapWeb - tkinter + ttkbootstrap + tkinterweb


# 🎥 Video :
ChatCPP Ttkbootstrap Multichat AI GUI Demo


ChatCPP GradioWeb (Gradio) Multichat AI WebUI Demo


ChatCPP Tkinter Multisession AI GUI Demo
 

---

## 🇮🇩 **Versi Bahasa Indonesia**

# 🧠 offline-ai-chat-coding-gui (Change Log)

## CHANGELOG RETRO CHAOS DEVELOPER EDITION

### Added

🖼️ Cek screenshot di repo, semua fitur baru kelihatan kok 😎

### Fixed

🐞 Bug fix? Pasti dong. Kayak biasa, tiap update makin cepat & stabil 💪
(Gak percaya? Jalankan aja, kalau gak error berarti udah fix 😎)

### Changed

⚙️ Tambah fitur baru sambil nambal bug di fitur barunya.
Jangan tanya lagi ada bug atau enggak — ini gaya klasik Retro Developer 🤣

---

## 🇬🇧 **English Version**

# 🧠 offline-ai-chat-coding-gui (Change Log)

## CHANGELOG RETRO CHAOS DEVELOPER EDITION

### Added

🖼️ Check the screenshots in the repo — all new features are clearly visible 😎

### Fixed

🐞 Bug fixes? Of course! As always, every update runs faster and smoother 💪
(Don’t believe it? Just run it — if it doesn’t crash, it’s fixed 😎)

### Changed

⚙️ Added new features while patching the new feature’s own bugs.
Don’t even ask if there are more bugs — this is the classic Retro Developer style 🤣

----------------------

# 💡 Catatan:  
> Repo ini hanya berisi **kode eksperimen Tkinter**.  
> Versi **production-ready** (Tkinter Pro, TTKBootstrap mirip ChatGPT, Gradio WebUI, Pywebview, FastAPI, Flask+PHP Multitab) **tidak dipublikasikan di sini**.  
> Screenshot & video demo di repo menunjukkan fitur lengkap dari berbagai versi yang sudah production ready.

----------------------

## 💡 About This Project
This repository contains **experimental open-source code** for the multi-tab AI Chatbot GUI,  
along with a **fully working .exe demo** for public showcase.

> ⚠️ Note: The `.exe` release represents the **production-ready build**,  
> while the source code here is **an experimental framework prototype**.
