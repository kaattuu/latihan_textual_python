

"""
# 1. Persiapan Lingkungan (Virtual Environment)
# Sangat disarankan untuk selalu menggunakan Virtual Environment 
  agar pustaka (library) Textual tidak bentrok dengan proyek Python 
  lainnya di komputermu.
# Buka terminal atau command prompt.
# Buat folder baru untuk proyekmu: mkdir belajar-textual lalu masuk 
  ke folder tersebut cd belajar-textual.
# Buat virtual environment:
# Windows   : python -m venv venv
# Mac/Linux : python3 -m venv venv
# Aktifkan  :
# Windows   : venv\Scripts\activate
# Mac/Linux : source venv/bin/activate
"""





"""
# 2. Instalasi Textual
# Setelah lingkungan siap, kita akan menginstal dua hal: Textual 
  (library inti) dan Textual-dev (alat bantu pengembangan).
# Ketik perintah ini di terminal:
# Bash
# pip install textual
# pip install textual-dev
"""





"""
# 3. Mengenal textual-dev untuk Debugging
# Ini adalah bagian paling penting yang sering dilewatkan pemula. Dalam 
  aplikasi terminal biasa, jika kode kamu salah, aplikasinya akan langsung 
  tertutup atau error-nya berantakan di layar.
# textual-dev menyediakan fitur Console khusus untuk melihat log (catatan) 
  aplikasi secara real-time di jendela terpisah.
# Cara Menggunakan Console Debugging:
# Buka dua jendela terminal (berdampingan).
# Di Terminal Pertama, jalankan perintah:
# Bash
# textual console
# (Terminal ini akan stand-by menunggu pesan dari aplikasi kamu).
# Di Terminal Kedua, kamu jalankan kode Python kamu menggunakan perintah:
# Bash
# textual run --dev nama_file_kamu.py
"""





"""
# 4. Cek Hasil Instalasi
# Mari kita pastikan semuanya bekerja dengan menjalankan demo bawaan 
  dari Textual. Ketik ini di terminal:
# Bash
# python -m textual
# Jika muncul tampilan berwarna-warni yang interaktif di terminalmu, 
  berarti instalasi berhasil!
"""





"""
# Tugas kecil untukmu:
# Coba jalankan perintah pip install tadi dan pastikan tidak ada 
  pesan error. Jika sudah, beri tahu saya, dan kita akan lanjut ke 
  sub-materi berikutnya: Struktur Utama App Class dan bagaimana 
  cara menampilkan tulisan pertama di layar.
# Sudah siap untuk lanjut atau ada kendala saat instalasi?
"""