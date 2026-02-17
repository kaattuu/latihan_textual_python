# """
# Bagus! Sekarang kita masuk ke "Jantung" dari setiap aplikasi Textual: App Class.
# Kalau kamu membayangkan aplikasi sebagai sebuah tubuh, maka App adalah otaknya. 
# Semua yang terjadi di layar diatur dari sini.
# """

# """
# 1. Struktur Minimal App Class
# Untuk membuat aplikasi Textual, kamu harus membuat sebuah Class yang mewarisi 
# (inherit) sifat-sifat dari App. Perhatikan kerangka sederhana ini:
# """

from textual.app import App

class AplikasiPertamaku(App):
    """Sebuah aplikasi Textual dimulai dari sini."""
    pass

if __name__ == "__main__":
    app = AplikasiPertamaku()
    app.run()






# """
# 2. Memahami Siklus Hidup (Lifecycle)
# Aplikasi Textual punya tahapan hidup, mirip seperti manusia: 
# Lahir -> Tumbuh -> Beraksi -> Mati. 
# Di Textual, kita menggunakan metode khusus untuk menangani tahap-tahap ini:

# A. on_mount (Tahap Kelahiran)
# Ini dipanggil tepat setelah aplikasi muncul di layar terminalmu. 
# Biasanya digunakan untuk persiapan awal, seperti mengatur fokus ke tombol 
# tertentu atau memulai timer.

# B. compose (Tahap Pembentukan Tubuh)
# Di sinilah kamu menentukan apa saja yang ada di dalam aplikasi 
# (tombol, teks, input box, dll). Ini adalah tempat kita "menyusun" tampilan.

# C. on_unmount (Tahap Perpisahan)
# Dipanggil sesaat sebelum aplikasi benar-benar tertutup. Berguna untuk 
# menyimpan data atau membersihkan sisa-sisa proses.
# """






# """
# 3. Contoh Kode dengan Lifecycle
# Mari kita gabungkan semuanya agar kamu bisa melihat perbedaannya:
# """


from textual.app import App
from textual.widgets import Header, Footer, Static

class BelajarLifecycle(App):
    # Menambahkan CSS sederhana langsung di dalam kode
    BINDINGS = [("d", "toggle_dark", "Toggle Dark Mode")]

    def compose(self):
        """1. Tahap Membentuk Tubuh (Menyusun Widget)"""
        yield Header()
        yield Static("Halo! Saya adalah konten utama aplikasi ini.")
        yield Footer()

    def on_mount(self):
        """2. Tahap Kelahiran (Aplikasi sudah muncul di layar)"""
        self.title = "Aplikasi Textual Saya"
        self.sub_title = "Belajar Lifecycle bersama Gemini"
        # Di sini kita bisa melakukan sesuatu saat aplikasi pertama buka
        self.notify("Aplikasi berhasil dijalankan!")

if __name__ == "__main__":
    app = BelajarLifecycle()
    app.run()


# """
# Analogi untuk memudahkan:
# App       : Adalah Gedung Bioskopnya.
# compose() : Adalah Denah Kursi dan Layar (menentukan posisi benda).
# on_mount(): Adalah Saat Pintu Bioskop Dibuka (lampu menyala, musik mulai diputar).
# run()     : Adalah Instruksi Buka Bioskop.
# """


# """
# Tantangan Kecil untukmu:
# Coba salin kode di atas ke file main.py kamu, lalu jalankan 
# dengan perintah yang tadi kita pelajari:
# textual run --dev main.py

# Pertanyaan saya:
# Setelah kamu jalankan, apakah kamu melihat tulisan 
# "Halo! Saya adalah konten utama..." di tengah layar? 
# Dan coba tekan tombol "d" di keyboard, apa yang terjadi pada warnanya?

# Kalau sudah berhasil, kita akan lanjut ke sub-materi berikutnya: 
# Method compose() lebih dalam.
# """






