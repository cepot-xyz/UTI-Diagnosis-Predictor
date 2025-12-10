# Studi Kasus Data Mining: Klasifikasi Diagnosis Infeksi Saluran Kemih Menggunakan Algoritma C4.5

## 1. Pendahuluan

Infeksi Saluran Kemih (ISK) adalah diagnosis umum yang memerlukan penentuan lokasi infeksi (ISK Bawah atau ISK Atas) untuk manajemen klinis yang optimal. ISK Bawah (radang kandung kemih/sistitis) dan ISK Atas (nefropati origin pelvis ginjal/pielonefritis) memiliki risiko dan protokol penanganan yang berbeda.

Studi kasus ini berfokus pada pengembangan **model prediktif** menggunakan teknik **Data Mining** untuk membedakan kedua kondisi tersebut. Model akan memanfaatkan gejala klinis spesifik—seperti **Suhu Tubuh**, **Nyeri Lumbar**, dan **Nyeri saat Berkemih (Micturition Pains)**—sebagai fitur masukan utama.

## 2. Tujuan Analisis dan Pemodelan C4.5

Tujuan utama studi ini adalah:

1.  **Implementasi C4.5:** Menerapkan algoritma **Pohon Keputusan (Decision Tree) C4.5** pada dataset rekam medis pasien (`UTI.csv`) untuk tugas klasifikasi.
2.  **Identifikasi Fitur Kunci:** Menilai seberapa informatif setiap fitur/gejala terhadap target menggunakan metrik **Gain Ratio** dari C4.5, sehingga dapat menentukan prediktor yang paling berpengaruh.
3.  **Evaluasi Kinerja:** Menilai kinerja model C4.5 menggunakan metrik standar (Akurasi, Presisi, Recall, dan F1-Score) untuk prediksi target yang ditentukan.

## 3. Sumber Data dan Rincian Algoritma

| Detail | Deskripsi |
| :--- | :--- |
| **Nama Dataset** | `UTI.csv` |
| **Metode Pembelajaran** | *Supervised Learning* (Klasifikasi) |
| **Algoritma Utama** | **C4.5 (Pohon Keputusan)** |
| **Fitur Utama (Variabel Independen)** | `Temperature of patient`, `Lumbar pain`, `Micturition pains` (serta fitur gejala biner lainnya dalam dataset). |
| **Kelas Target (Variabel Dependen)** | `Inflammation of urinary bladder` (Inflamasi kandung kemih / ISK Bawah). |

## 4. Metodologi Pemodelan C4.5

Implementasi algoritma C4.5 akan mengikuti langkah-langkah berikut:

1.  **Preprocessing Data:** Membersihkan data, menangani nilai yang hilang (jika ada), dan mengubah variabel kontinu seperti `Temperature of patient` menjadi diskrit (binning) jika implementasi C4.5 yang digunakan memerlukannya.
2.  **Pembentukan Pohon:** C4.5 membangun pohon keputusan dengan memilih atribut pada tiap node yang menghasilkan *Gain Ratio* tertinggi terhadap target `Inflammation of urinary bladder`.
3.  **Pruning:** Melakukan pemangkasan pada pohon untuk mengurangi overfitting dan meningkatkan kemampuan generalisasi.
4.  **Validasi:** Menguji model yang telah dipangkas menggunakan cross-validation atau holdout set, lalu menyajikan **Matriks Kebingungan (Confusion Matrix)** dan metrik performa.

## 5. Hasil yang Diharapkan dan Implikasi Klinis

### Hasil yang Diharapkan

- Model C4.5 diharapkan menghasilkan pohon keputusan yang ringkas, mudah dibaca, dan dapat dijelaskan secara klinis.
- Pohon akan menyajikan aturan IF–THEN yang eksplisit, misalnya: "JIKA `Lumbar pain` = Ya DAN `Temperature of patient` > 38.5, MAKA kemungkinan `Inflammation of urinary bladder` lebih tinggi."

### Implikasi Praktis

Model yang transparan seperti C4.5 cocok sebagai sistem pendukung keputusan klinis (CDSS) pada layanan primer. Dengan memetakan pola gejala ke probabilitas inflamasi kandung kemih, model dapat membantu tenaga kesehatan dalam membuat keputusan awal terkait pemeriksaan lanjutan atau pengobatan.

Catatan: fokus repo saat ini adalah memprediksi kolom `Inflammation of urinary bladder` berdasarkan pola pada kolom lain dalam `UTI.csv`.
