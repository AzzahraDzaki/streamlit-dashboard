import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import calendar

# Mengimpor data yang telah disiapkan
hour_df = pd.read_csv("hour.csv")  
day_df = pd.read_csv("day.csv")    

# Mengubah tipe data kolom 'dteday' menjadi datetime
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])
day_df['dteday'] = pd.to_datetime(day_df['dteday'])

# Judul Dashboard
st.title('Dashboard Data Penyewaan Sepeda')

# Menambahkan Sidebar untuk memilih filter
st.sidebar.title('Pilih Filter Data')

# Filter untuk memilih visualisasi
visualization_option = st.sidebar.selectbox(
    'Pilih Visualisasi:',
    ('Pengaruh Cuaca terhadap Penyewaan Sepeda', 'Total Penyewaan Sepeda per Bulan', 'Distribusi Penyewaan Sepeda per Jam')
)

# Fungsi untuk menampilkan visualisasi pertama (Pengaruh Cuaca terhadap Jumlah Penyewa Sepeda)
def plot_weather_impact(filtered_df):
    plt.figure(figsize=(10, 6))
    palette = sns.color_palette("muted")
    sns.barplot(x='weathersit', y='cnt', data=filtered_df, errorbar=None, palette=palette, hue='weathersit', legend=False)
    plt.title('Pengaruh Cuaca terhadap Jumlah Penyewa Sepeda', fontsize=16, fontweight='bold')
    plt.xlabel('Kondisi Cuaca', fontsize=12)
    plt.ylabel('Rata-rata Penyewaan Sepeda', fontsize=12)
    plt.xticks(ticks=[0, 1, 2, 3], labels=['Cerah', 'Berawan', 'Hujan ringan', 'Hujan berat'], fontsize=11)
    st.pyplot(plt)  # Menampilkan plot

# Fungsi untuk menampilkan visualisasi kedua (Total Penyewaan Sepeda per Bulan)
def plot_monthly_rentals(filtered_df):
    plt.figure(figsize=(12, 6))
    monthly_rentals = filtered_df.groupby('mnth')['cnt'].sum()
    monthly_rentals.plot(kind='bar', color='mediumseagreen', edgecolor='black')
    plt.xticks(ticks=range(12), labels=[calendar.month_name[i] for i in range(1, 13)], rotation=45, fontsize=11)
    plt.title('Total Penyewaan Sepeda per Bulan', fontsize=16, fontweight='bold')
    plt.xlabel('Bulan', fontsize=12)
    plt.ylabel('Total Penyewaan Sepeda', fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    st.pyplot(plt)  # Menampilkan plot

# Fungsi untuk menampilkan visualisasi ketiga (Distribusi Penyewaan Sepeda per Jam)
def plot_hourly_rentals(filtered_df):
    plt.figure(figsize=(10, 6))
    hourly_rentals = filtered_df.groupby('hr')['cnt'].mean()
    plt.plot(hourly_rentals.index, hourly_rentals.values, marker='o', color='purple', linewidth=2)
    plt.title('Distribusi Penyewaan Sepeda per Jam', fontsize=16, fontweight='bold')
    plt.xlabel('Jam', fontsize=12)
    plt.ylabel('Rata-rata Penyewaan Sepeda', fontsize=12)
    plt.xticks(range(0, 24))
    plt.grid(True)
    plt.tight_layout()
    st.pyplot(plt)  # Menampilkan plot

# Menampilkan visualisasi berdasarkan pilihan pengguna
if visualization_option == 'Pengaruh Cuaca terhadap Penyewaan Sepeda':
    plot_weather_impact(hour_df)
elif visualization_option == 'Total Penyewaan Sepeda per Bulan':
    plot_monthly_rentals(hour_df)
elif visualization_option == 'Distribusi Penyewaan Sepeda per Jam':
    plot_hourly_rentals(hour_df)
