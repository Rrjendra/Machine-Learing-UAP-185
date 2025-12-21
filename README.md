# Klasifikasi Sentimen Komentar Game Genshin Impact (UAP)

---

## 📑 Table of Content
1. [Deskripsi Proyek](#deskripsi-proyek)
2. [Dataset](#dataset)
3. [Preprocessing](#preprocessing)
4. [Model yang Digunakan](#model-yang-digunakan)
5. [Evaluasi Model](#evaluasi-model)
6. [Analisis Hasil](#analisis-hasil)
7. [Sistem Website (Streamlit)](#sistem-website-streamlit)
8. [Cara Menjalankan Aplikasi (Lokal)](#cara-menjalankan-aplikasi-lokal)

---

## 📌 Deskripsi Proyek

Proyek ini merupakan tugas **Ujian Akhir Praktikum (UAP)** yang bertujuan untuk melakukan **klasifikasi sentimen terhadap komentar pemain game Genshin Impact** berbahasa Indonesia.  
Analisis sentimen dilakukan menggunakan pendekatan **Machine Learning**, dengan membandingkan model **non-pretrained** dan **pretrained (transfer learning)** berbasis **Deep Learning**.

Selain itu, proyek ini dilengkapi dengan **sistem website sederhana berbasis Streamlit** untuk mendemonstrasikan hasil prediksi sentimen secara interaktif.

---

## 📊 Dataset

- **Jenis Data**: Data teks (komentar pemain)
- **Bahasa**: Bahasa Indonesia (dengan campuran istilah game dan bahasa Inggris)
- **Sumber Data**: Hasil scraping komentar pemain game Genshin Impact
- **Jumlah Data**: ±15.000 komentar

### Label Sentimen
- Negatif  
- Netral (Others)  
- Positif  

Karena ukuran dataset cukup besar, dataset **tidak diunggah langsung ke repository GitHub**.

📊 **Dataset dapat diunduh melalui Google Drive:**  
👉 **[Link Dataset](https://drive.google.com/drive/folders/1XkfMcM0EVBMt7h1sIF6AGkisJ5mdnME9?usp=sharing)**

Dataset merupakan **hasil scraping dan pelabelan mandiri**, digunakan **khusus untuk keperluan akademik**.

---

## Preprocessing

Tahapan preprocessing yang dilakukan meliputi:

- Case folding (mengubah teks menjadi huruf kecil)
- Menghapus URL dan karakter non-alfabet
- Menghapus data kosong
- Pelabelan sentimen otomatis berdasarkan rating pengguna
- Encoding label menggunakan `LabelEncoder`
- Pembagian data latih dan data uji dengan rasio **80:20**

**Catatan:**  
Pada proyek ini **tidak diterapkan data augmentation**, karena dataset yang digunakan sudah mencukupi dan augmentasi pada data teks berpotensi mengubah makna serta label sentimen.

---

## Model yang Digunakan

### 1️⃣ LSTM (Non-Pretrained)
- Arsitektur: **Embedding + LSTM + Dense**
- Digunakan sebagai **baseline model**
- Dilatih dari awal tanpa bobot pretrained

### 2️⃣ BERT (Pretrained)
- Model: `bert-base-uncased`
- Pendekatan: **Transfer Learning**
- Memberikan peningkatan performa signifikan dibandingkan LSTM

### 3️⃣ DistilBERT (Pretrained)
- Versi ringan dari BERT
- Lebih efisien secara komputasi
- Memberikan performa yang kompetitif

### 4️⃣ IndoBERT (Pretrained)
- Model: `indobenchmark/indobert-base-p1`
- Dirancang khusus untuk Bahasa Indonesia
- Menjadi **model dengan performa terbaik** pada proyek ini

📦 Model hasil pelatihan **tidak diunggah langsung ke GitHub** karena keterbatasan ukuran file.  
📥 Model dapat diunduh melalui Google Drive (tautan sama dengan dataset).

---

## 📈 Evaluasi Model

Evaluasi model dilakukan menggunakan metrik berikut:
- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix
- Learning Curve (Loss & Accuracy)

### Tabel Perbandingan Performa Model

| Model       | Accuracy | Precision (Macro) | Recall (Macro) | F1-score (Macro) |
|-------------|----------|-------------------|----------------|------------------|
| LSTM        | 0.33     | 0.11              | 0.33           | 0.17             |
| BERT        | 0.63     | 0.63              | 0.63           | 0.63             |
| DistilBERT  | 0.62     | 0.62              | 0.62           | 0.62             |
| **IndoBERT**| **0.64** | **0.65**          | **0.64**       | **0.64**         |


### Confusion Matrix 

## Confusion Matrix 🔴🟢

| LSTM | IndoBERT | 
|------|----------|
| ![CM LSTM](Images/MAT_LSTM.png) | ![CM IndoBERT](Images/MAT_IND.png) | 

| DistilBERT | BERT |
|------------|------|
| ![CM DistilBERT](Images/MAT_DISB.png) | ![Confusion Matrix BERT](Images/MAT_BERT.png) |


### Learning Curves 📈

| LSTM | IndoBERT |
|------|----------|
| ![Learning Curve LSTM](Images/LC_LSTM.png) | ![Learning Curve IndoBERT](Images/LC_IND.png) |

---

## 🔍 Analisis Hasil

Berdasarkan hasil evaluasi, **model pretrained berbasis Transformer** secara konsisten menunjukkan performa yang lebih baik dibandingkan model **LSTM non-pretrained**.  

Model **IndoBERT** menghasilkan performa terbaik karena:
- Menggunakan pretraining khusus Bahasa Indonesia
- Lebih mampu menangkap konteks kalimat informal dan campuran istilah game
- Memberikan keseimbangan antara akurasi dan stabilitas prediksi

Hal ini menunjukkan bahwa **Transfer Learning sangat efektif** untuk tugas klasifikasi sentimen teks Bahasa Indonesia.

---

## 🌐 Sistem Website (Streamlit)

Sistem website sederhana dibangun menggunakan **Streamlit** untuk mendemonstrasikan hasil klasifikasi sentimen secara interaktif.  
Aplikasi dijalankan **secara lokal** menggunakan model hasil pelatihan.

### Fitur Website
- Input teks komentar dari pengguna
- Pilihan model (LSTM / BERT / DistilBERT / IndoBERT)
- Prediksi label sentimen secara langsung

---

## ▶️ Cara Menjalankan Aplikasi (Lokal)

### 1️⃣ Install Dependensi

pip install streamlit tensorflow transformers torch scikit-learn

### 2️⃣ Jalankan Aplikasi Streamlit

Pastikan berada di folder project, lalu jalankan: streamlit run app.py
Aplikasi akan berjalan pada browser melalui : http://localhost:8501



