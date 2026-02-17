from textual.app import App
from textual.widgets import Header, Footer, Static, Button, Input

class SusunTampilan(App):
    def compose(self):
        yield Header()

        yield Static("Selamat Datang di Aplkasi  Saya!", id="judul")
        yield Input(placeholder="ketik nama kamu di sini...")
        yield Button("Klik Saya!", variant="success")
        yield Button("Hapus", variant="error")

        yield Footer()

app = SusunTampilan()
app.run()