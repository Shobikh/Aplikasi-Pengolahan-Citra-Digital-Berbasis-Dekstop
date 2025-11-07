import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageEnhance
import cv2 as cv
import numpy as np


class EffectPage:
    def __init__(self, parent):
        self.parent = parent
        self.image_path = None
        self.image_label = None
        self.original_image = None
        self.modified_image = None
        self.modified_image_full = None
        self.contrast_factor = 1
        self.sharpness_factor = 1
        self.noise_reduction_amount = 0
        self.brightness = 1
        self.color = 1

    def show(self):
        self.create_widgets()

    def create_widgets(self):
        # Frame utama
        main_frame = tk.Frame(self.parent)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Frame untuk gambar dengan scrollbar
        self.image_frame = tk.Frame(main_frame)
        self.image_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Canvas untuk menampilkan gambar before
        self.before_canvas = tk.Canvas(self.image_frame, bg="grey")
        self.before_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Canvas untuk menampilkan gambar after
        self.after_canvas = tk.Canvas(self.image_frame, bg="grey")
        self.after_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Frame kontrol
        control_frame = tk.Frame(main_frame, width=200)
        control_frame.pack(side=tk.RIGHT, fill=tk.Y)

        # Tombol upload image
        upload_button = tk.Button(control_frame, text="Upload Image", font=("Bebas Neue", 10, "bold"), command=self.upload_image)
        upload_button.pack(pady=5)

        # Slider contrast
        self.contrast_slider = tk.Scale(control_frame, from_=0.1, to_=3.0, orient=tk.HORIZONTAL, resolution=0.1,
                                        label="Contrast", command=self.adjust_contrast)
        self.contrast_slider.pack(fill=tk.X, pady=5)

        # Slider brightness
        self.brightness_slider = tk.Scale(control_frame, from_=0.1, to_=3.0, orient=tk.HORIZONTAL, resolution=0.1,
                                          label="Brightness", command=self.adjust_brightness)
        self.brightness_slider.pack(fill=tk.X, pady=5)

        # Slider sharpness
        self.sharpness_slider = tk.Scale(control_frame, from_=0.1, to_=3.0, orient=tk.HORIZONTAL, resolution=0.1,
                                         label="Sharpness", command=self.adjust_sharpness)
        self.sharpness_slider.pack(fill=tk.X, pady=5)

        # Slider noise reduction
        self.noise_reduction_slider = tk.Scale(control_frame, from_=1, to_=10, orient=tk.HORIZONTAL,
                                               label="Noice Reduction", command=self.adjust_noise_reduction)
        self.noise_reduction_slider.pack(fill=tk.X, pady=5)

        # Slider saturation
        self.color_slider = tk.Scale(control_frame, from_=0.1, to_=3.0, orient=tk.HORIZONTAL, resolution=0.1,
                                         label="Saturation", command=self.adjust_color)
        self.color_slider.pack(fill=tk.X, pady=5)

        # Tombol save image
        save_button = tk.Button(control_frame, text="Save Image", font=("Bebas Neue", 10, "bold"), command=self.save_image)
        save_button.pack(pady=5)

        # Tombol reset
        reset_button = tk.Button(control_frame, text="Reset", font=("Bebas Neue", 10, "bold"), command=self.reset_image)
        reset_button.pack(pady=5)

    def upload_image(self):
        self.image_path = filedialog.askopenfilename(title="Select Image",
                                                     filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if self.image_path:
            self.original_image = Image.open(self.image_path)
            self.modified_image_full = self.original_image.copy()
            self.modified_image = self.original_image.copy()
            self.display_image()
            print(f"Image uploaded: {self.image_path}")

    def display_image(self):
        if self.original_image and self.modified_image:
            canvas_width = self.before_canvas.winfo_width()
            canvas_height = self.before_canvas.winfo_height()

            # Resize Image namun tetap mempertahankan rasio
            before_image_resized = self.original_image.copy()
            before_image_resized.thumbnail((canvas_width, canvas_height), Image.Resampling.LANCZOS)
            after_image_resized = self.modified_image.copy()
            after_image_resized.thumbnail((canvas_width, canvas_height), Image.Resampling.LANCZOS)

            # Konversi ke PhotoImage
            before_image_tk = ImageTk.PhotoImage(before_image_resized)
            after_image_tk = ImageTk.PhotoImage(after_image_resized)

            # Menghitung posisi tengah canvas
            before_x = (canvas_width - before_image_resized.width) / 2
            before_y = (canvas_height - before_image_resized.height) / 2
            after_x = (canvas_width - after_image_resized.width) / 2
            after_y = (canvas_height - after_image_resized.height) / 2

            # Display image before
            self.before_canvas.create_image(before_x, before_y, anchor="nw", image=before_image_tk)
            self.before_canvas.image = before_image_tk

            # Display image after
            self.after_canvas.create_image(after_x, after_y, anchor="nw", image=after_image_tk)
            self.after_canvas.image = after_image_tk

    def apply_effects(self):
        self.modified_image_full = self.original_image.copy()

        # Apply contrast
        enhancer = ImageEnhance.Contrast(self.modified_image_full)
        self.modified_image_full = enhancer.enhance(self.contrast_factor)

        # Apply brightness
        enhancer = ImageEnhance.Brightness(self.modified_image_full)
        self.modified_image_full = enhancer.enhance(self.brightness)

        # Apply sharpness
        enhancer = ImageEnhance.Sharpness(self.modified_image_full)
        self.modified_image_full = enhancer.enhance(self.sharpness_factor)

        # Apply noise reduction
        image_cv = cv.cvtColor(np.array(self.modified_image_full), cv.COLOR_RGB2BGR)
        valid_size = max(3, min(15, (self.noise_reduction_amount // 2 * 2 + 1)))
        image_cv = cv.medianBlur(image_cv, valid_size)
        self.modified_image_full = Image.fromarray(cv.cvtColor(image_cv, cv.COLOR_BGR2RGB))

        # Apply saturation
        enhancer = ImageEnhance.Color(self.modified_image_full)
        self.modified_image_full = enhancer.enhance(self.color)

        # Deklarasi ulang gambar yang telah dimanipulasi
        self.modified_image = self.modified_image_full.copy() #membedakan gambar yang ditampilkan pada display image after
        canvas_width = self.before_canvas.winfo_width()
        canvas_height = self.before_canvas.winfo_height()
        self.modified_image.thumbnail((canvas_width, canvas_height), Image.Resampling.LANCZOS)

        self.display_image()

    def save_image(self):
        if self.modified_image_full:
            file_path = filedialog.asksaveasfilename(
                defaultextension=".png",
                filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg *.jpeg")],
                title="Save Image"
            )
            if file_path:
                self.modified_image_full.save(file_path)
                messagebox.showinfo("Simpan Gambar", f"Gambar disimpan di {file_path}") # menampilkan pesan berisi direktori tempat gambar disimpan
        else:
            messagebox.showwarning("Simpan Gambar", "Tidak ada gambar yang disimpan.")

    def reset_image(self):
        if self.original_image:
            self.modified_image = self.original_image.copy()
            self.display_image()
            self.contrast_factor = 1
            self.sharpness_factor = 1
            self.noise_reduction_amount = 0
            self.brightness = 1
            self.color = 1
            self.contrast_slider.set(1)
            self.sharpness_slider.set(1)
            self.noise_reduction_slider.set(0)
            self.brightness_slider.set(1)

    def adjust_contrast(self, value):
        self.contrast_factor = float(value)
        self.apply_effects()

    def adjust_brightness(self, value):
        self.brightness = float(value)
        self.apply_effects()

    def adjust_sharpness(self, value):
        self.sharpness_factor = float(value)
        self.apply_effects()

    def adjust_noise_reduction(self, value):
        self.noise_reduction_amount = int(value)
        self.apply_effects()

    def adjust_color(self, value):
        self.color = float(value)
        self.apply_effects()