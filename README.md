# Mental Health Assessment Tool

## Deskripsi
Aplikasi Streamlit ini bertujuan untuk menganalisis data kesehatan mental berdasarkan indikator tertentu, khususnya untuk mahasiswa. Aplikasi ini memungkinkan pengguna untuk:

- Menampilkan sampel data kesehatan mental.
- Memfilter data berdasarkan tingkat depresi tertentu.
- Mencari data berdasarkan ID individu.
- Melakukan visualisasi data menggunakan histogram.
- Mengunduh dataset hasil filter.
- Memberikan informasi kontak layanan kesehatan mental di Indonesia.

## Fitur Utama
1. **Analisis Data**: Memfilter data berdasarkan kategori tingkat depresi.
2. **Pencarian Data**: Mencari data individu berdasarkan ID.
3. **Visualisasi Data**: Menampilkan histogram untuk indikator kesehatan mental tertentu.
4. **Unduh Dataset**: Mengunduh data yang sudah difilter dalam format CSV.
5. **Informasi Kontak Layanan**: Menyediakan daftar layanan yang dapat dihubungi terkait masalah kesehatan mental.

## Prasyarat
Sebelum menjalankan aplikasi, pastikan Anda sudah menginstal:

- Python 3.7 atau versi lebih baru.
- Streamlit: `pip install streamlit`
- Pandas: `pip install pandas`
- KaggleHub: `pip install kagglehub`

## Cara Menjalankan Aplikasi

1. **Clone Repository**
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Konfigurasi Kaggle API**
   - Pastikan Anda sudah memiliki API Key dari Kaggle.
   - Simpan file `kaggle.json` ke direktori `~/.kaggle/`.

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Jalankan Aplikasi**
   ```bash
   streamlit run main.py
   ```

5. **Akses Aplikasi**
   - Buka browser dan akses [http://localhost:8501](http://localhost:8501).

## Struktur Dataset
Dataset yang digunakan diperoleh dari Kaggle dan memiliki kolom-kolom berikut:

- `Sleep Disturbance`
- `Appetite Change`
- `Loss of Interest`
- `Fatigue`
- `Worthlessness`
- `Concentration Issues`
- `Agitation`
- `Suicidal Ideation`
- `Sleep Issues`
- `Aggression`
- `Panic Attacks`
- `Hopelessness`
- `Restlessness`
- `Low Energy`
- `Depression State`

## Kontak Layanan Kesehatan Mental
Aplikasi ini juga menyediakan daftar kontak layanan kesehatan mental di Indonesia, termasuk:

- **119**: Konseling psikologi SEJIWA.
- **(021) 500-454**: Hotline Kesehatan Jiwa Kemenkes.
- **(021) 9696 9293**: LSM Jangan Bunuh Diri.
- **intothelight.email@gmail.com**: Email Into The Light Indonesia.

## Kontribusi
Kami terbuka untuk kontribusi dari komunitas! Silakan buat Pull Request atau buka issue jika menemukan masalah atau memiliki ide untuk pengembangan lebih lanjut.

## Lisensi
Proyek ini dilisensikan di bawah [MIT License](LICENSE).

