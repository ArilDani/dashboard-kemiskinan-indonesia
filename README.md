# Dashboard Analisis Kemiskinan Indonesia

## Deskripsi
Dashboard ini dibuat menggunakan Streamlit untuk melakukan visualisasi dan analisis data kemiskinan di Indonesia berdasarkan data dari Badan Pusat Statistik (BPS). Tujuannya adalah untuk memberikan wawasan mengenai tren kemiskinan antar provinsi, sebaran kemiskinan per tahun, analisis spesifik per provinsi, serta faktor-faktor penyebab utama kemiskinan.

## Sumber Data
Data kemiskinan diambil dari dataset [Open Data Jabar](https://opendata.jabarprov.go.id/id/dataset/persentase-penduduk-miskin-berdasarkan-provinsi-di-indonesia) yang berisi persentase penduduk miskin berdasarkan provinsi dan tahun.

## Proses Analisis
1. **Pemuatan Data**  
   Data dimuat dari file Excel `data_kemiskinan.xlsx` menggunakan pandas.

2. **Pembersihan dan Persiapan Data**    
   - Kolom-kolom diubah namanya agar lebih mudah dipahami (misal: `nama_provinsi` menjadi `Provinsi`).
   - Data dikonversi ke tipe numerik untuk kolom persentase kemiskinan dan tahun.  
   - Data yang memiliki nilai kosong pada kolom penting dihapus.  

3. **Perhitungan Statistik Dasar**  
   Menghitung rata-rata nasional persentase kemiskinan sebagai gambaran umum.

4. **Visualisasi Data**  
   - Tren kemiskinan antar provinsi ditampilkan menggunakan grafik garis.  
   - Sebaran kemiskinan pada tahun tertentu divisualisasikan dengan grafik batang.  
   - Analisis tren kemiskinan spesifik per provinsi juga disediakan.  

5. **Analisis Faktor Penyebab**  
   Menyajikan faktor-faktor utama penyebab kemiskinan berdasarkan data dan publikasi BPS.

## Cara Menjalankan
1. Pastikan Python dan Streamlit sudah terinstall.  
2. Letakkan file `data_kemiskinan.xlsx` di direktori yang sama dengan `app.py`.  
3. Jalankan perintah berikut di terminal:  
   ```
   streamlit run app.py
   ```  
4. Buka browser dan akses URL yang diberikan oleh Streamlit (biasanya http://localhost:8501).

## Referensi
- [Open Data Jabar - Data Kemiskinan](https://opendata.jabarprov.go.id/id/dataset/persentase-penduduk-miskin-berdasarkan-provinsi-di-indonesia)  
- [Dialocal - Penyebab Kemiskinan di Indonesia](https://dialocal.com/penyebab-kemiskinan-di-indonesia/)

---

Dokumentasi ini dibuat untuk membantu memahami proses analisis kemiskinan yang dilakukan dalam aplikasi dashboard ini.

## Penjelasan Sintaks di app.py

Berikut adalah penjelasan singkat mengenai sintaks dan struktur kode utama yang digunakan dalam `app.py`:

- **Import Library**  
  Mengimpor library utama seperti `streamlit` untuk UI, `pandas` untuk manipulasi data, `numpy` untuk perhitungan numerik, dan `plotly.express` untuk visualisasi grafik.

- **Konfigurasi Halaman**  
  `st.set_page_config()` digunakan untuk mengatur judul halaman dan layout aplikasi Streamlit.

- **Sidebar Navigasi**  
  Menggunakan `st.sidebar.radio()` untuk membuat menu navigasi antara halaman "home" dan "dashboard".

- **Kontrol Alur Program dengan Kondisi**  
  Struktur `if-elif` digunakan untuk menampilkan konten berbeda berdasarkan pilihan halaman pengguna.

- **Pemuatan dan Pembersihan Data**  
  Membaca file Excel dengan `pd.read_excel()`, mengganti nama kolom, mengkonversi tipe data, dan menghapus data yang tidak lengkap.

- **Perhitungan Statistik**  
  Menggunakan `numpy` untuk menghitung rata-rata persentase kemiskinan nasional.

- **Visualisasi Data**  
  Membuat grafik garis dan batang menggunakan `plotly.express` dan menampilkannya dengan `st.plotly_chart()`.

- **Interaksi Pengguna**  
  Slider dan dropdown (`st.slider()`, `st.selectbox()`) digunakan untuk memilih tahun dan provinsi yang ingin dianalisis.

- **Penanganan Error**  
  Blok `try-except` digunakan untuk menangani kesalahan saat membaca file data dan menampilkan pesan error dengan `st.error()`.

