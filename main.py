import streamlit as st
import pandas as pd
import kagglehub as kh
import os

# Download dataset from Kaggle using kagglehub
path = kh.dataset_download("hamjashaikh/mental-health-detection-dataset")
st.write("Dataset berhasil diunduh. Path ke file dataset:", path)

# Load dataset
file_path = os.path.join(path, "Deepression.csv")  # Sesuaikan dengan nama file di dataset
data = pd.read_csv(file_path)

# Ubah nama kolom untuk menyamakan dengan indikator di deskripsi
data.columns = [
    "ID", "Sleep Disturbance", "Appetite Change", "Loss of Interest",
    "Fatigue", "Worthlessness", "Concentration Issues", "Agitation",
    "Suicidal Ideation", "Sleep Issues", "Aggression", "Panic Attacks",
    "Hopelessness", "Restlessness", "Low Energy", "Depression State"
]

# Title dan deskripsi aplikasi
st.title("Alat Penilaian Kesehatan Mental di Kampus")
st.markdown("""
Aplikasi ini menganalisis data kesehatan mental berdasarkan indikator tertentu.
Tujuannya adalah memberikan gambaran mengenai kondisi kesehatan mental mahasiswa.
""")

# Tampilkan data sampel
st.subheader("Data Sampel")
st.write(data.head())

# Filter data berdasarkan kebutuhan
st.subheader("Analisis Data")
depression_state = st.selectbox(
    "Pilih kategori tingkat depresi yang ingin dianalisis:",
    options=["No depression", "Mild", "Moderate", "Severe"]
)
filtered_data = data[data["Depression State"] == depression_state]
st.write(f"Menampilkan data untuk kategori: **{depression_state}**")
st.write(filtered_data)

# Fitur pencarian data berdasarkan ID
st.subheader("Cari Data Berdasarkan ID")
search_id = st.text_input("Masukkan ID yang ingin dicari:")
if search_id:
    search_result = data[data["ID"].astype(str) == search_id]
    if not search_result.empty:
        st.write("Data ditemukan:")
        st.write(search_result)
    else:
        st.warning("Data dengan ID tersebut tidak ditemukan.")

# Visualisasi Data
st.subheader("Visualisasi Data")
visualize_column = st.selectbox(
    "Pilih indikator untuk divisualisasikan:",
    options=data.columns[1:-1]  # Menghindari ID dan Depression State
)

# Buat histogram
st.bar_chart(filtered_data[visualize_column].value_counts())

# Unduh dataset hasil filter
st.subheader("Unduh Dataset")
csv = filtered_data.to_csv(index=False)
st.download_button(
    label="Unduh Dataset",
    data=csv,
    file_name="filtered_mental_health_data.csv",
    mime="text/csv"
)

# Layanan yang dapat dihubungi
st.subheader("Layanan yang Dapat Dihubungi")
st.markdown("""
Berikut adalah beberapa nomor yang dapat dihubungi untuk masalah kesehatan mental di Indonesia:
- **119**: Nomor darurat untuk menghubungi ambulans atau Kementerian Kesehatan (Kemenkes). Nomor ini juga dapat digunakan untuk konseling psikologi SEJIWA dengan menekan ekstensi 8.
- **(021) 500-454**: Hotline Kesehatan Jiwa Kemenkes yang dapat dihubungi untuk konsultasi pencegahan bunuh diri.
- **(021) 9696 9293**: Nomor telepon LSM Jangan Bunuh Diri yang dapat dihubungi untuk mengubah perspektif masyarakat terhadap mental illness.
- **(0251) 8310611**: Nomor telepon RSJ Marzoeki Mahdi, Bogor yang dapat dihubungi untuk layanan krisis terpadu 24 jam.
- **(021) 7207372**: Nomor telepon Perkumpulan Keluarga Berencana Indonesia (PKBI) yang dapat dihubungi untuk bantuan.
- **intothelight.email@gmail.com**: Email Into The Light Indonesia yang dapat dihubungi untuk bantuan.

Selain itu, Anda juga dapat mengunjungi puskesmas terdekat untuk mendapatkan layanan kesehatan mental. Tidak semua puskesmas menyediakan layanan poliklinik jiwa, namun Anda dapat menghubungi puskesmas terdekat untuk mengetahui apakah mereka melayani kesehatan jiwa.
""")
