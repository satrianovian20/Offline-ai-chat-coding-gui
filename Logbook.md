| No | Bahasa Indonesia                                                                                                | English Version                                                                                                   |
| -- | --------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| 1  | Llama.cpp server exe versi lawas tetap bisa jalanin model GGUF v3 di Windows chaotic, bahkan yang 13B Q4\_K\_M. | Old Llama.cpp server exe still ran GGUF v3 models on a chaotic Windows, even 13B Q4\_K\_M worked.                 |
| 2  | Saat Llama.cpp server exe “half dead”, tetap bisa jalan dan kasih respons AI bagus di GUI Mode V1 eksperimen.   | Even when Llama.cpp server exe was “half dead”, it still gave great AI responses in experimental GUI Mode V1.     |
| 3  | Port 5001 berhasil dikunci untuk semua build dan tetap stabil meski gonta-ganti Llama.cpp server exe.           | Port 5001 was locked for all builds and stayed stable despite switching Llama.cpp server exe versions.            |
| 4  | RAM 16GB bisa jalanin model besar tanpa crash, BSOD, atau hang di GUI Tkinter ultra ringan buatan sendiri.      | 16GB RAM handled big models without crash, BSOD, or freeze in self-made ultra-lightweight Tkinter GUI.            |
| 5  | Developer sadar bahwa semua ini jalan di OS yang harusnya udah reinstall total, tapi malah survive dan stabil.  | Developer realized all this ran on an OS that should’ve been reinstalled, but it somehow survived and stabilized. |
| 6  | Setiap error bukan dijadikan alasan menyerah, tapi jadi arena eksperimen ekstrem + nanya ke ChatGPT.            | Every error wasn't a reason to quit, but a lab for extreme experiments + asking ChatGPT.                          |
| 7  | GUI berhasil tundukkan semua build Llama.cpp server exe dari b5899 sampai terbaru tanpa ubah port.              | GUI successfully dominated all Llama.cpp server exe builds from b5899 to latest without port changes.             |
| 8  | Semua cloner bakal bengong: “kok bisa responsif dan jalan terus?”                                               | All cloners would be stunned: “How is it this responsive and stable?”                                             |
| 9  | Bahkan AI Chat modern bisa kalah kalau lihat efisiensi GUI AI Rakyat Edition ini.                               | Even modern AI Chat apps may lose when they see the efficiency of this Rakyat Edition GUI AI.                     |
| 10 | Dev tidak panik saat Llama.cpp server exe tidak bisa jalan—malah dicari akal dan dicoba pakai semua build.      | Dev didn’t panic when Llama.cpp server exe failed—they found tricks and tested with every build possible.         |
 - - -
 | No | Peristiwa Kacau Tapi Epik                               | Detail                                                                                            |
| -- | ------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| 1  | Server `llama.cpp` jalan di sistem Half-Dead            | Windows tanpa keamanan, `server.exe` sering gagal load model GGUF tapi tetap bisa jalan.          |
| 2  | Port 5001 terus dipakai                                 | Semua build `llama.cpp` diuji (b5899 - b6018), tetap pakai port 5001, tidak pernah konflik.       |
| 3  | Stress test multitasking ekstrem                        | RAM 16GB dipaksa jalanin 13B Q4\_K\_M sampai 17B Q5\_K\_M sambil multitasking, no crash, no hang. |
| 4  | GUI Python Tkinter ukuran kilobyte                      | Ringan tapi kuat, tetap responsif bahkan tanpa `Windows Defender`.                                |
| 5  | Debug sambil jalanin model besar                        | Server `llama.cpp` gagal load model? Malah diedit skripnya sambil jalanin model 13B.              |
| 6  | Model tetap responsif walau ctx 4096 + max\_tokens 5000 | Padahal server setengah mati, AI tetap jawab seperti model modern.                                |
| 7  | Reinstall OS bukan karena nyerah, tapi karena menang    | Server akhirnya mati total. Bukan kalah, tapi karena perang sudah selesai.                        |
| 8  | Cloners pasti bengong                                   | GUI AI ini terlihat mustahil: anti hang, responsif, pakai Tkinter, tapi jalanin model besar.      |
---
| No | Epic Yet Chaotic Events                                      | Details                                                                                        |
| -- | ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------- |
| 1  | `llama.cpp` server ran on a half-dead OS                     | Windows without security; `server.exe` kept failing to load GGUF, but somehow still ran.       |
| 2  | Always used port 5001                                        | Tested all builds (b5899 - b6018), never changed port, no conflict ever occurred.              |
| 3  | Extreme multitasking stress test                             | 16GB RAM forced to handle 13B Q4\_K\_M to 17B Q5\_K\_M while multitasking — no crash, no hang. |
| 4  | Kilobyte-sized Tkinter GUI                                   | Lightweight but powerful, responsive even without `Windows Defender`.                          |
| 5  | Debugging while running big models                           | GGUF failed to load? Instead of giving up, edited scripts mid-run with 13B active.             |
| 6  | Models stayed responsive even at ctx 4096 + max\_tokens 5000 | Despite half-dead server, AI responded like a modern chatbot.                                  |
| 7  | OS reinstalled not due to failure, but victory               | Server finally died. Not a loss — the war had been won.                                        |
| 8  | Cloners will be confused                                     | This GUI AI looks impossible: anti-hang, responsive, Tkinter, yet runs big models smoothly.    |
---
| Kategori            | Chaos Dev Indonesia 🇮🇩                                            | Chaos Dev English 🇬🇧                                                           |
| ------------------- | ------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| Mentalitas          | Pantang nyerah walau GGUF gak kebaca dan server exe mogok           | Never give up even when GGUF fails and server exe refuses to boot                |
| Error pertama       | GUI error? Istirahat 5 menit, ngopi, balik lagi coding              | First GUI error? Rest 5 minutes, grab coffee, back to coding                     |
| Modularisasi awal   | Tambah fitur modular satu-satu sambil debug manual                  | Add modular features one by one while debugging manually                         |
| Build environment   | Windows penuh file sisa eksperimen, game bajakan, Python bertumpuk  | Windows filled with leftover experiments, cracked games, tangled Python installs |
| Port stabil         | Tetap pakai port 5001 meski environment seperti kapal pecah         | Still use port 5001 even if the environment is like a sinking ship               |
| Solusi kalau gagal  | Coba install Llama.cpp dari pip, lalu ganti ke exe, lalu oprek lagi | Try installing Llama.cpp via pip, switch to exe, tweak scripts again             |
| Alasan lanjut oprek | Karena sayang sama GUI-nya dan ingin bantu user PC kentang lainnya  | Because I care about my GUI and want to help other potato-PC users               |
---
| No | Kejadian                                                                     | Bahasa Inggris                                                                  | Bahasa Indonesia                                                                  |
| -- | ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| 1  | Awal tanya cara bikin GUI AI chatbot                                         | "How do I make an AI chatbot GUI using Python Tkinter without Gradio or Flask?" | "Gimana cara bikin GUI AI chatbot pakai Python Tkinter tanpa Gradio atau Flask?"  |
| 2  | Awalnya pakai KoboldCPP                                                      | "Started with KoboldCPP, chaotic config everywhere"                             | "Mulai pakai KoboldCPP dulu, konfigurasi kacau total"                             |
| 3  | Coba Llama server exe, awalnya sukses                                        | "Ran llama server exe successfully, cheers and high-five!"                      | "Llama server exe jalan, langsung tos dan sorak-sorai!"                           |
| 4  | PC dimatikan, llama server gak jalan lagi                                    | "After restarting PC, llama server exe just died"                               | "Habis restart PC, llama server exe malah KO total"                               |
| 5  | Otak diputar, skrip dioprek, ganti-ganti build                               | "Script-twisting madness, swapping builds like mad scientists"                  | "Oprek skrip brutal, gonta-ganti build kayak ilmuwan gila"                        |
| 6  | Build b5899 ternyata jalan                                                   | "Build b5899 brought peace... until we found the root cause"                    | "Build b5899 menyelamatkan... sampai ketahuan penyebab aslinya"                   |
| 7  | Penyebab aslinya? Windows Security hilang karena game bajakan                | "Turns out... Windows Security gone due to pirated game. Chaos wins."           | "Ternyata... Windows Security hilang gegara game bajakan. Chaos menang telak."    |
| 8  | README.md dan Logbook.md berisi komedi chaos                                 | "README and Logbook full of satirical chaos dev entries"                        | "README dan Logbook isinya komedi dev yang penuh kekacauan"                       |
| 9  | Instal ulang Windows → semua build jalan normal                              | "Fresh Windows install = everything works. Irony much?"                         | "Setelah install ulang Windows = semua build jalan. Ironi tingkat dewa."          |
| 10 | Bisa load 160k ctx + 10k max tokens di Deepseek Coder v2 Lite 15.7B Q5\_K\_M | "Running 160k context + 10k max tokens on a 16GB RAM pirate Windows = LEGEND"   | "Jalanin 160k konteks + 10k token maksimum di RAM 16GB Windows bajakan = LEGENDA" |
| 11 | GUI bisa jalan di semua OS bajakan dan non-bajakan                           | "Inclusive GUI: runs even on pirated Win10 Home without tantrum"                | "GUI non-diskriminatif: bisa jalan di Win10 Home bajakan tanpa rewel"             |

