# """
# Mantap! Semangatnya luar biasa. Sekarang kita masuk ke 
# bagian yang paling seru: compose().

# Kalau App adalah gedungnya, maka compose() adalah desainer interiornya. 
# Di sinilah kamu menentukan perabotan (Widget) apa saja yang mau 
# diletakkan di dalam ruangan.
# """


# """
# 1. Apa itu compose()?
# compose() adalah sebuah method khusus di dalam Class App 
# (atau Widget) yang tugasnya "menghasilkan" komponen visual.

# Ciri khas compose() adalah penggunaan kata kunci yield.

# Kenapa pakai yield, bukan return?
# Karena compose() adalah seorang generator. Dia tidak memberikan 
# satu benda lalu selesai, tapi dia memberikan daftar benda satu 
# per satu untuk dipasang oleh Textual ke dalam layar.
# """


# """
# 2. Cara Menyusun Widget
# Bayangkan kamu sedang menumpuk balok. Widget yang kamu yield 
# pertama kali akan berada di paling atas (atau paling awal), 
# dan seterusnya ke bawah.

# Mari kita lihat contoh susunan yang lebih lengkap:
# """


from textual.app import App
from textual.widgets import Header, Footer, Static, Button, Input

class SusunTampilan(App):
    def compose(self):
        # 1. Bagian Atas
        yield Header() 
        
        # 2. Bagian Tengah (Konten)
        yield Static("Selamat Datang di Aplikasi Saya!", id="judul")
        yield Input(placeholder="Ketik nama kamu di sini...")
        yield Button("Klik Saya!", variant="success")
        yield Button("Hapus", variant="error")
        
        # 3. Bagian Bawah
        yield Footer()

if __name__ == "__main__":
    app = SusunTampilan()
    app.run()


# """
# 3. Aturan Main di compose()
# Ada beberapa hal penting yang perlu kamu ingat agar tidak bingung:

# Urutan itu Penting: Jika kamu menaruh Header() di baris terakhir yield, 
# maka kepalanya akan pindah ke bawah (walau secara default Textual mencoba 
# menempatkannya dengan benar, urutan yield tetap menentukan struktur DOM-nya).

# Widget adalah Objek: Setiap yield Button() sebenarnya sedang membuat 
# instance baru dari kelas Button.

# Identitas (ID & Classes): Perhatikan id="judul" pada contoh di atas. 
# Ini sangat penting nanti saat kita masuk ke materi CSS (TCSS) agar 
# kita bisa menghias widget tertentu secara spesifik.
# """


# """
# 4. Bisakah kita pakai Logic di dalam compose()?
# Tentu saja! Karena ini kode Python biasa, kamu bisa pakai if atau for.

# Contohnya, jika kamu ingin membuat 5 tombol sekaligus tanpa mengetik satu-satu:
# ""


def compose(self):
        yield Header()
        # Membuat 5 tombol secara otomatis
        for i in range(1, 6):
            yield Button(f"Tombol Ke-{i}")
        yield Footer()


# """
# Eksperimen Kecil untuk Kamu:
# Coba modifikasi file main.py kamu dengan kode di atas 
# (yang ada Input dan Button).

# Pertanyaan saya:

# Apakah tombol-tombolnya muncul berderet ke bawah secara otomatis?

# Coba klik di dalam kotak Input, apakah kamu bisa mengetik di sana?

# Jika ini sudah terasa matang di kepala, kita akan lanjut ke sub-materi 
# terakhir di bagian Fondasi: Method mount(): Cara menambah widget secara 
# dinamis (saat aplikasi sudah jalan).

# Gimana, lanjut? Hati-hati, jangan sampai berasap ya kepalanya! 😂
# """