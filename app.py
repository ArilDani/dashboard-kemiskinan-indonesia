import streamlit as st
import pandas as pd
import numpy as np  # ✅ Ditambahkan
import plotly.express as px

# Konfigurasi halaman
st.set_page_config(page_title="Analisis Kemiskinan Indonesia", layout="wide")

# Sidebar Navigasi
st.sidebar.title("🏠")
halaman = st.sidebar.radio("Pilih Halaman", ["🏠 home", "📊 Dashboard"])

# ==========================
# 🏠 HALAMAN BERANDA
# ==========================
if halaman == "🏠 home":
    st.title("Selamat Datang di Dashboard Kemiskinan Indonesia")

    st.markdown("""
    ### 📊 Visualisasi & Analisis Kemiskinan Berdasarkan Data BPS

    Website ini menyajikan:
    - **Tren Kemiskinan Antar Provinsi** 📈
    - **Sebaran Kemiskinan per Tahun** 📍
    - **Analisis Spesifik per Provinsi** 🔍
    - **Faktor Penyebab Utama Kemiskinan** 🧠

    💡 Data bersumber dari [Open Data Jabar](https://opendata.jabarprov.go.id/id/dataset/persentase-penduduk-miskin-berdasarkan-provinsi-di-indonesia)

    ---
    """)

    st.markdown("### 🚀 Mulai Analisis")
    st.markdown("Klik menu *Dashboard* di samping kiri untuk mulai eksplorasi data.")

# ==========================
# 📊 DASHBOARD
# ==========================
elif halaman == "📊 Dashboard":
    st.title("📊 Analisis Tren & Sebaran Kemiskinan di Indonesia")

    # 📥 Load data
    DATA_PATH = "data_kemiskinan.xlsx"

    try:
        df = pd.read_excel(DATA_PATH)

        # Rename kolom jika perlu
        if "nama_provinsi" in df.columns:
            df.rename(columns={
                "nama_provinsi": "Provinsi",
                "persentase_penduduk_miskin": "Persentase_Kemiskinan",
                "tahun": "Tahun"
            }, inplace=True)

        df["Persentase_Kemiskinan"] = pd.to_numeric(df["Persentase_Kemiskinan"], errors="coerce")
        df["Tahun"] = pd.to_numeric(df["Tahun"], errors="coerce")
        df = df.dropna(subset=["Tahun", "Provinsi", "Persentase_Kemiskinan"])
        df["Tahun"] = df["Tahun"].astype(int)

        # ✅ Tambahan penggunaan numpy ringan (tanpa mengubah logika utama)
        rata_rata_kemiskinan = np.round(np.mean(df["Persentase_Kemiskinan"]), 2)
        st.markdown(f"📌 **Rata-rata Nasional Persentase Kemiskinan:** {rata_rata_kemiskinan}%")

        # 🗂️ Tampilkan data mentah
        st.subheader("📄 Data Kemiskinan dari BPS")
        st.markdown("Sumber: https://opendata.jabarprov.go.id/id/dataset/persentase-penduduk-miskin-berdasarkan-provinsi-di-indonesia")
        st.dataframe(df)

        # ========================
        # 📈 Tren Kemiskinan
        # ========================
        st.header("📈 Tren Kemiskinan Antar Provinsi")
        fig_tren = px.line(df, x="Tahun", y="Persentase_Kemiskinan", color="Provinsi",
                        markers=True, title="Tren Kemiskinan Antar Provinsi")
        st.plotly_chart(fig_tren, use_container_width=True)

        # ========================
        # 📍 Sebaran Kemiskinan (per Tahun)
        # ========================
        st.header("📍 Sebaran Kemiskinan di Tahun Tertentu")

        tahun_terpilih = st.slider("Pilih Tahun", int(df["Tahun"].min()), int(df["Tahun"].max()), step=1)
        df_tahun = df[df["Tahun"] == tahun_terpilih].sort_values("Persentase_Kemiskinan", ascending=False)

        fig_sebar = px.bar(df_tahun, x="Provinsi", y="Persentase_Kemiskinan",
                        color="Persentase_Kemiskinan",
                        color_continuous_scale="Reds",
                        title=f"Sebaran Kemiskinan per Provinsi Tahun {tahun_terpilih}")
        st.plotly_chart(fig_sebar, use_container_width=True)

        # ========================
        # 🔍 Analisis per Provinsi
        # ========================
        st.header("🔍 Analisis Spesifik Provinsi")
        provinsi_terpilih = st.selectbox("Pilih Provinsi", sorted(df["Provinsi"].unique()))
        df_prov = df[df["Provinsi"] == provinsi_terpilih]

        fig_prov = px.line(df_prov, x="Tahun", y="Persentase_Kemiskinan",
                        markers=True,
                        title=f"Tren Kemiskinan di {provinsi_terpilih}")
        st.plotly_chart(fig_prov, use_container_width=True)

        # ========================
        # 🧠 Faktor Penyebab Kemiskinan
        # ========================
        st.header("🧠 Faktor Penyebab Utama Kemiskinan")
        st.markdown("""
        Berdasarkan data dan publikasi dari **Badan Pusat Statistik (BPS)**, beberapa faktor utama yang menyebabkan kemiskinan di Indonesia antara lain:

        1. **Kurangnya Pendidikan**: Pendidikan yang rendah menghambat akses terhadap pekerjaan yang lebih baik.
        2. **Ketimpangan Ekonomi**: Kekayaan terkonsentrasi pada segelintir orang menyebabkan ketimpangan.
        3. **Akses Terbatas Kesehatan**: Pelayanan kesehatan yang kurang menyebabkan produktivitas rendah.
        4. **Ketidakstabilan Ekonomi**: Krisis dan inflasi memperburuk kemiskinan.
        5. **Faktor Geografis**: Daerah seperti Papua dan Maluku cenderung memiliki tingkat kemiskinan lebih tinggi.

        Sumber: [Dialocal](https://dialocal.com/penyebab-kemiskinan-di-indonesia/)
        """)

    except Exception as e:
        st.error(f"❌ Gagal membaca file data: {e}")
