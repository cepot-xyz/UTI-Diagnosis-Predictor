# Studi Kasus Data Mining: Klasifikasi Diagnosis Infeksi Saluran Kemih Menggunakan Algoritma C4.5

## 1. Pendahuluan

Infeksi Saluran Kemih (ISK) adalah diagnosis umum yang memerlukan penentuan lokasi infeksi (ISK Bawah atau ISK Atas) untuk manajemen klinis yang optimal. ISK Bawah (radang kandung kemih/sistitis) dan ISK Atas (nefropati origin pelvis ginjal/pielonefritis) memiliki risiko dan protokol penanganan yang berbeda.

Studi kasus ini berfokus pada pengembangan **model prediktif** menggunakan teknik **Data Mining** untuk membedakan kedua kondisi tersebut. Model akan memanfaatkan gejala klinis spesifik—seperti **Suhu Tubuh**, **Nyeri Lumbar**, dan **Nyeri saat Berkemih (Micturition Pains)**—sebagai fitur masukan utama.

## 2. Tujuan Analisis dan Pemodelan C4.5

Tujuan utama dari studi ini adalah:

1.  **Implementasi C4.5:** Menerapkan algoritma **Pohon Keputusan (Decision Tree) C4.5** pada dataset rekam medis pasien ISK (`UTI.csv`) untuk tugas klasifikasi.
2.  **Identifikasi Fitur Kunci:** Mengukur efektivitas setiap gejala dalam memecah data menggunakan metrik **Gain Ratio** dari C4.5, untuk menentukan prediktor diagnosis yang paling kuat.
3.  **Evaluasi Kinerja:** Mengukur kinerja model C4.5 melalui metrik standar data mining (Akurasi, Presisi, *Recall*, dan F1-Score) dalam memprediksi dua kelas diagnosis akhir.

## 3. Sumber Data dan Rincian Algoritma

| Detail | Deskripsi |
| :--- | :--- |
| **Nama Dataset** | `UTI.csv` |
| **Metode Pembelajaran** | *Supervised Learning* (Klasifikasi) |
| **Algoritma Utama** | **C4.5 (Pohon Keputusan)** |
| **Fitur Utama (Variabel Independen)** | `Temperature of patient`, `Lumbar pain`, `Micturition pains` (serta fitur gejala biner lainnya dalam dataset). |
| **Kelas Target (Variabel Dependen)** | `Inflammation of urinary bladder` (ISK Bawah) dan `Nephritis of renal pelvis origin` (ISK Atas). |

## 4. Metodologi Pemodelan C4.5

Implementasi algoritma C4.5 akan mengikuti langkah-langkah berikut:

1.  **Preprocessing Data:** Memastikan data bersih, menangani nilai yang hilang (jika ada), dan mengubah variabel kontinu (`Temperature of patient`) menjadi diskrit (jika diperlukan oleh implementasi C4.5 tertentu).
2.  **Pembentukan Pohon:** C4.5 akan melatih pohon keputusannya dengan memilih atribut pada setiap *node* yang menghasilkan *Gain Ratio* tertinggi. `Lumbar pain` dan `Temperature of patient` diharapkan menjadi *node* percabangan awal yang krusial.
3.  **Pruning:** Melakukan pemangkasan (pruning) pada pohon yang telah dibangun untuk menghindari *overfitting* dan meningkatkan kemampuan generalisasi model pada data baru.
4.  **Validasi:** Menguji model yang telah di-*pruning* menggunakan teknik *cross-validation* atau set data *holdout* untuk menghasilkan **Matriks Kebingungan (Confusion Matrix)**.

## 5. Hasil yang Diharapkan dan Implikasi Klinis

### Hasil yang Diharapkan

* Model C4.5 diharapkan menghasilkan **pohon keputusan yang ringkas** dan mudah diinterpretasikan.
* Pohon tersebut akan menyediakan **aturan IF-THEN** yang transparan, misalnya: "JIKA `Lumbar pain` = Ya AND `Temperature of patient` > 38.5, MAKA Diagnosis = Nefropati (ISK Atas)."

### Implikasi Praktis

Model C4.5 menawarkan transparansi yang lebih baik daripada model *black-box* lainnya. Model yang akurat ini dapat berfungsi sebagai **sistem pendukung keputusan klinis (CDSS)** di fasilitas kesehatan primer. Dengan cepat memproses gejala pasien, sistem dapat memberikan prediksi diagnosis dini (ISK Bawah vs. Atas) yang objektif, membantu tenaga medis mempercepat pengambilan keputusan pengobatan yang tepat.
