import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from about import AboutPage
from effect import EffectPage

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("IMPEG")

        # Menjalankan prgram dalam keadaan maximize
        self.state('zoomed')

        # Menyeting mode fullscreen (tidak default)
        self.attributes('-fullscreen', False)
        self.bind("<F11>", self.toggle_fullscreen)  # Tombol F11 untuk toggle fullscreen
        self.bind("<Escape>", self.quit_fullscreen)  # Tombol Escape untuk keluar dari fullscreen

        # Menambahkan penanganan untuk tombol silang (x)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.create_widgets()

        # Inisialisasi halaman
        self.about_page = AboutPage(self.main_frame)
        self.effect_page = EffectPage(self.main_frame)

        self.show_home()

    def create_widgets(self):
        # Navbar
        navbar = tk.Frame(self, bg="lightgray")
        navbar.pack(side="top", fill="x")

        home_button = tk.Button(navbar, text="Home", font=("Bebas Neue", 10, "bold"), command=self.show_home)
        home_button.pack(side="left", padx=10, pady=5)

        effect_button = tk.Button(navbar, text="Effect", font=("Bebas Neue", 10, "bold"), command=self.show_effect)
        effect_button.pack(side="left", padx=10, pady=5)

        about_button = tk.Button(navbar, text="About", font=("Bebas Neue", 10, "bold"), command=self.show_about)
        about_button.pack(side="left", padx=10, pady=5)

        # Main container
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill="both", expand=True)

    def show_home(self):
        self.clear_main_frame()
        # Logo and app name
        img = Image.open("assets/logo.jpg")
        img = img.resize((300, 300), Image.LANCZOS)
        logo = ImageTk.PhotoImage(img)
        logo_label = tk.Label(self.main_frame, image=logo)
        logo_label.image = logo
        logo_label.pack(pady=10)

        app_name_label = tk.Label(self.main_frame, text="IMPEG", font=("Montserrat", 29, "bold"))
        app_name_label.pack(pady=10)

        start_button = tk.Button(self.main_frame, text="Start", font=("Bebas Neue", 10, "bold"), command=self.show_effect)
        start_button.pack(pady=10)

    def show_about(self):
        self.clear_main_frame()  # Clear existing frame
        self.about_page.show()

    def show_effect(self):  # Function to display the effect page
        self.clear_main_frame()
        self.effect_page.show()

    def clear_main_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()  # Remove all widgets in the main frame

    def toggle_fullscreen(self, event=None):
        self.attributes('-fullscreen', not self.attributes('-fullscreen'))

    def quit_fullscreen(self, event=None):
        self.attributes('-fullscreen', False)

    def on_closing(self, event=None):
        # Menambahkan konfirmasi sebelum keluar
        if tk.messagebox.askokcancel("Keluar", "Apakah Anda yakin ingin keluar?"):
            self.destroy()

if __name__ == "__main__":
    app = Application()
    app.mainloop()
