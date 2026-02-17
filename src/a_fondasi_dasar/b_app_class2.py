from textual.app import App
from textual.widgets import Header, Footer, Static

class BelajarLifecycle(App):
    BINDINGS = [("d", "toggle_dark", "Toggle Dark Mode")]

    def compose(self):
        yield Header()
        yield Static("Halo! saya adalah konten utama aplikasi ini.")
        yield Footer()
    
    def on_mount(self):
        self.title = "Aplikasi Textual Saya"
        self.sub_title = "Belajar Lifecycle bersama Gemini"
        self.notify("Aplikasi berhasil dijalankan!")

app = BelajarLifecycle()
app.run()