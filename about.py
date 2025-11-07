import tkinter as tk

class AboutPage:
    def __init__(self, parent):
        self.parent = parent

    def show(self):
        about_label = tk.Label(self.parent, text="About IMPEG", font=("Montserrat", 24, "bold"))
        about_label.pack(pady=20)

        about_text = (
            "Image Processing and Enhancement Generator (IMPEG) adalah aplikasi desktop sederhana yang dapat digunakan untuk melakukan peningkatan gambar dengan berbagai teknik\n"
            "Aplikasi ini dibuat guna memenuhi tugas akhir mata kuliah Pengelohan Citra Digital\n"
            "\n"
            "Credit\n"
            "\n"
            "Fauzan Afif Lutfiansah\n"
            "Muhammad Rizki Hidayatullah\n"
            "Mukhammad Shobikh\n"
            "\n"
            "Thanks to\n"
            "\n"
            "Oddy Virgantara Putra, S.Kom., M.T.\n"
        )
        about_message = tk.Label(self.parent, text=about_text, wraplength=700, justify="center", font=("Bebas Neue", 13))
        about_message.pack(pady=10)

        back_button = tk.Button(self.parent, text="Back to Home", font=("Bebas Neue", 10, "bold"), command=self.parent.master.show_home)
        back_button.pack(pady=10)
