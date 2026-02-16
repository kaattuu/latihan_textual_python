# 1. Fondasi Dasar (The Basics)
# Sebelum masuk ke visual, kamu harus paham kerangka kerja dasarnya.
# Instalasi & Setup   : Cara memasang Textual dan menggunakan textual-dev untuk debugging.
# App Class           : Memahami struktur utama App dan siklus hidupnya (lifecycle).
# Method compose()    : Cara menyusun widget di dalam aplikasi.
# Method mount()      : Cara menambahkan widget secara dinamis saat aplikasi berjalan.

# from src.a_fondasi_dasar import a_instalasi_dan_stup
from src.a_fondasi_dasar import b_app_class
# from src.a_fondasi_dasar import c_method_compose
# from src.a_fondasi_dasar import d_method_mount




# 2. Layout & Design (CSS-like Styling)
# Textual menggunakan sistem yang sangat mirip dengan web development.
# Introduction to TCSS: Mempelajari sintaks CSS khusus Textual.
# Layout Models       : Memahami Vertical, Horizontal, dan Grid layout.
# The Box Model       : Mengatur margin, border, dan padding.
# Positioning         : Memahami perbedaan antara relative, absolute, dan fixed positioning.

# from src.b_layout_dan_desain import a_introduction_to_css
# from src.b_layout_dan_desain import b_layout_models
# from src.b_layout_dan_desain import c_the_box_model
# from src.b_layout_dan_desain import d_positioning




# 3. Widget & Interaktivitas
# Widget adalah komponen pembangun aplikasi kamu.
# Built-in Widgets    : Mempelajari Header, Footer, Button, Input, Static, dan DataTable.
# Reactive Attributes : Cara membuat variabel yang otomatis memperbarui tampilan saat nilainya berubah (sangat krusial!).
# Custom Widgets      : Cara membuat komponen sendiri dengan mewarisi kelas Widget.

# from src.c_widget_dan_interaktivitas import a_built_in_widgets
# from src.c_widget_dan_interaktivitas import b_reactive_attributes
# from src.c_widget_dan_interaktivitas import c_custom_widgets





# 4. Event Handling (Logika Aplikasi)
# Bagaimana aplikasi merespons pengguna.
# Message Handling    : Menggunakan dekorator @on untuk menangkap klik tombol atau input.
# Key Bindings        : Membuat shortcut keyboard (misal: tekan 'q' untuk keluar).
# Watchers            : Memantau perubahan pada atribut tertentu.

# from src.d_event_handling import a_message_handling
# from src.d_event_handling import b_key_binddings
# from src.d_event_handling import c_watchers





# 5. Navigasi & Arsitektur Lanjut
# Screens             : Mengelola perpindahan antar halaman (misal: dari menu utama ke halaman pengaturan).
# Modals              : Membuat dialog pop-up di dalam terminal.
# Workers & Threading : Cara menjalankan proses berat di latar belakang agar UI tidak membeku (freezing).

# from src.e_navigasi_dan_arsitektur_lanjut import a_screens
# from src.e_navigasi_dan_arsitektur_lanjut import b_modals
# from src.e_navigasi_dan_arsitektur_lanjut import c_workers_dan_threading