# import streamlit
import streamlit as st
st.title("Hasil Projek Akhir Pengantar Sains Data A Kelompok 4")

# baca data asli
import pandas as pd
import numpy as np
data = pd.read_csv('marketing_campaign.csv')

if st.checkbox('Tampilkan Data Asli'):
    st.subheader('Data Asli Analisis Customer Personality')
    st.write(data)
    st.write("informasi data : total data = 2240 data, kolom = 29 kolom")

# visualisasi data asli dari image grafik dari colab, jika pake plt banyak errornya
if st.checkbox('Tampilkan Grafik - Grafik Data Asli'):
    # histogram kolom year birth
    st.subheader('Grafik Year Birth (Histogram)')
    st.image("Year Birth.png")
    # histogram kolom income
    st.subheader('Grafik Income (Histogram)')
    st.image("Income.png")
    # pie chart kolom education
    st.subheader('Grafik Education (Pie Chart)')
    st.image("Education.png")
    # pie chart kolom marital status 
    st.subheader("Grafik Marital Status (Pie Chart)")
    st.image("Marital Status.png")
    # bar chart kolom jumlah anak 
    st.subheader("Grafik Jumlah Anak (Bar Chart)")
    st.image("Jumlah Anak.png")
    # bar chart kolom produk - produk 
    st.subheader("Grafik Produk - Produk (Bar Chart)")
    st.image("Products (Wine, dkk).png")
    # bar chart kolom place
    st.subheader("Grafik Purchases (Bar Chart)")
    st.image("Place (Purchases).png")
    # bar chart kolom promosi 
    st.subheader("Grafik Promosi (Bar Chart)")
    st.image("Promotion (Accepted1-5).png")

# baca data sudah diclean dan didrop fitur yang tidak akan dipakai
data_cleandrop = pd.read_csv('data_hasil_cleandrop.csv')
if st.checkbox('Tampilkan Data Hasil Cleaning dari Null dan Fitur yang Digunakan'):
    st.write(data_cleandrop)
    st.write("informasi : jumlah data berkurang dari 2240 jadi 2216 data dan fiturnya bertambah 1 karena total kids dipanggil di data exploratory")

# baca data preprosessing
data_normalisasi = pd.read_csv('data_hasil_preprocessing.csv')
if st.checkbox('Tampilkan Data Hasil Normalisasi Min Max'):
    st.write(data_normalisasi)

# clustering (tampilin tanpa kode)
if st.checkbox("Tampilkan Hasil Optimal untuk Clustering"):
    st.image("optimal cluster.png")
    st.write("n_cluster yang optimal adalah sebanyak 2 cluster")

if st.checkbox('Tampilkan Hasil Clustering serta Hasil Evaluasi K-Means dan Agglomerative Clustering'):
    st.subheader('Hasil K-Means Clustering')
    kmeans = pd.read_csv("data_kmeans_clustering.csv")
    st.write(kmeans)

    st.subheader('Hasil Evaluasi K-Means Clustering')
    st.write("Hasil evaluasi sebesar 40%")

    st.subheader('Hasil Agglomerative Clustering')
    agg = pd.read_csv("data_agglomerative_clustering.csv")
    st.write(agg)

    st.subheader('Hasil Evaluasi Agglomerative Clustering')
    st.write("hasil Evaluasi sebesar 49%")

st.write("*/semua hasil mengikuti dari google colab dan kodingan dari streamlit ini hanya berupa hasil jadi/*")