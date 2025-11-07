# Image Processing and Enhancement Generator (IMPEG)

Aplikasi ini merupakan proyek akhir dari Mata Kuliah Pengolahan Citra Digital (PCD).
Aplikasi dibangun menggunakan Python, Tkinter untuk GUI, serta OpenCV, Pillow, dan NumPy untuk proses pengolahan citra.


## Anggota Kelompok

Proyek ini dikerjakan oleh 3 orang mahasiswa sebagai tugas akhir mata kuliah PCD
Anggota kelompok:
- Fauzan Afif Lutfiansah / 432022611016
- Mukhammad Shobikh / 432022611047
- Muhammad Rizki Hidayatullah	/ 432022611042


## Fitur Utama

-   **Upload Image**: Mengunggah gambar ke dalam aplikasi.
-   **Contrast**: Mengatur kontras pada gambar menggunakan slider.
-   **Brightness**: Mengatur kecerahan pada gambar menggunakan slider.
-   **Sharpness**: Mengatur ketajaman gambar menggunakan slider.
-   **Noise Reduction**: Mengatur tingkat noise pada gambar.
-   **Saturation**: Mengatur tingkat saturasi warna pada gambar.
-   **Reset**: Berfungsi untuk mengembalikan gambar ke dalam keadaan semula
-   **Save Image**: Menyimpan gambar yang telah dimanipulasi dengan ukuran original


## Cara Menggunakan

1.  **Clone repository ini:**
    ```bash
    git clone https://github.com/Shobikh/Aplikasi-Pengolahan-Citra-Digital-Berbasis-Dekstop.git
    cd Aplikasi-Pengolahan-Citra-Digital-Berbasis-Dekstop
    ```

2.  **Buat dan aktifkan lingkungan virtual (disarankan):**
    ```bash
    python -m venv venv # Buat virtual environtment
    
    .\venv\Scripts\activate # Windows
    
    source venv/bin/activate # Mac/Linux
    ```

3.  **Instal semua library yang dibutuhkan:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Jalankan aplikasi IMPEG:**
    ```bash
    python main.py
    ```


## Tampilan Aplikasi
- **Home Page**

![image](https://github.com/user-attachments/assets/321ae0d6-16f9-45c0-a6fa-8ae153f80b45)

Halaman ini merupakan tampilan awal aplikasi, terdapat tombol start untuk mulai menggunakan aplikasi ini

- **Effect Page**

![image](https://github.com/user-attachments/assets/b0b2ba1e-92b0-4f67-93a8-9ab58cd3513c)

Halaman ini berisi fitur utama dari aplikasi, user dapat mengunggah foto yang akan dimanipulasi. Terdapat 2 kanvas pada halaman ini, dimana kanvas kanan akan menampilkan gambar original, sedangkan kanvas kiri akan menampilkan gammbar yang telah diberi efek

-	**Halaman About**

![image](https://github.com/user-attachments/assets/3d4f6e9f-d568-43a7-a422-9b4a06ad310a)

Halaman About menampilkan deskripsi singkat tentang aplikasi ini, serta nama anggota kelompok dan dosen pengampu mata kuliah PCD
