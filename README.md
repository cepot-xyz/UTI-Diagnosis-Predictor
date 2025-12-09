# Studi Kasus Analisis: Pengaruh Gejala (Suhu Tubuh, Nyeri Lumbar, dan Micturition Pains) Terhadap Kemungkinan Kejadian Inflamasi Saluran Kemih Bawah dan Atas

## 1. Pendahuluan

Infeksi Saluran Kemih (ISK) merupakan salah satu diagnosis rawat jalan yang paling umum dan dapat diklasifikasikan menjadi ISK Bawah (seperti radang kandung kemih/sistitis) dan ISK Atas (seperti radang ginjal/pielonefritis atau nefropati origin pelvis ginjal). Membedakan kedua kondisi ini sangat krusial karena ISK Atas sering kali membutuhkan pengobatan yang lebih intensif dan berisiko komplikasi yang lebih serius.

Meskipun diagnosis definitif memerlukan kultur urin, penentuan awal diagnosis di fasilitas kesehatan primer sangat bergantung pada interpretasi gejala klinis. Studi kasus ini bertujuan untuk memanfaatkan data rekam medis pasien untuk mengidentifikasi dan mengukur seberapa besar tiga gejala utama—**Suhu Tubuh**, **Nyeri Lumbar**, dan **Nyeri saat Berkemih (Micturition Pains)**—memengaruhi kemungkinan pasien didiagnosis dengan salah satu dari dua kondisi tersebut.

## 2. Tujuan Studi Kasus

Tujuan utama dari analisis ini adalah:

1.  **Mengkuantifikasi Hubungan:** Menentukan kekuatan dan arah hubungan antara tiga gejala terpilih (Suhu Tubuh, Nyeri Lumbar, Nyeri saat Berkemih) dengan dua diagnosis akhir.
2.  **Membentuk Model Prediktif:** Mengembangkan model analitik yang dapat memprediksi, berdasarkan kombinasi gejala-gejala ini, apakah pasien lebih mungkin mengalami ISK Bawah (`Inflammation of urinary bladder`) atau ISK Atas (`Nephritis of renal pelvis origin`).

## 3. Sumber Data

| Detail | Deskripsi |
| :--- | :--- |
| **Nama Dataset** | `UTI.csv` |
| **Tipe Data** | Data retrospektif pasien |
| **Variabel Kunci** | **Gejala (Independen)**: `Temperature of patient` (kontinu), `Lumbar pain` (biner), `Micturition pains` (biner). |
| **Hasil (Dependen)**: `Inflammation of urinary bladder` (biner) dan `Nephritis of renal pelvis origin` (biner). |

## 4. Metodologi Analisis (Rencana)

Untuk menganalisis pengaruh gejala terhadap kemungkinan diagnosis, metodologi yang akan diterapkan meliputi:

1.  **Analisis Deskriptif:** Menghitung statistik deskriptif (rata-rata, standar deviasi) untuk `Temperature of patient`, dikelompokkan berdasarkan hasil diagnosis (ISK Bawah vs. ISK Atas).
2.  **Analisis Korelasi:** Menghitung korelasi antara gejala biner (`Lumbar pain`, `Micturition pains`) dengan kedua hasil diagnosis.
3.  **Pemodelan Regresi Logistik Multinominal:** Membangun model prediksi untuk mengestimasi probabilitas diagnosis ISK Bawah dan ISK Atas sebagai fungsi dari ketiga gejala. Koefisien model ini akan mengukur seberapa besar peningkatan/penurunan kemungkinan kejadian setiap diagnosis akibat adanya gejala tertentu.

## 5. Hipotesis dan Hasil yang Diharapkan

Berdasarkan pengetahuan klinis umum, studi ini mengharapkan hasil sebagai berikut:

* **Nyeri Lumbar:** Gejala ini dihipotesiskan memiliki pengaruh positif yang **signifikan** terhadap kemungkinan diagnosis **ISK Atas (Nefropati)**, karena nyeri pinggang sering mengindikasikan infeksi telah mencapai ginjal.
* **Nyeri saat Berkemih (Micturition Pains):** Gejala ini dihipotesiskan memiliki pengaruh positif yang **kuat** terhadap diagnosis **ISK Bawah**, karena rasa sakit saat buang air kecil adalah gejala klasik dari sistitis.
* **Suhu Tubuh:** Diperkirakan bahwa `Temperature of patient` akan **secara signifikan lebih tinggi** pada kelompok dengan **ISK Atas** dibandingkan dengan ISK Bawah.

## 6. Kesimpulan dan Implikasi

Analisis ini akan menghasilkan model yang *tervalidasi secara data* mengenai peran tiga gejala kunci dalam membedakan ISK Bawah dari ISK Atas.

**Implikasi Praktis:**

Hasil studi ini dapat digunakan oleh dokter umum atau tenaga medis di layanan kesehatan primer sebagai panduan diagnostik awal yang non-invasif. Dengan cepat mengevaluasi **Suhu Tubuh**, keberadaan **Nyeri Lumbar**, dan **Nyeri saat Berkemih**, petugas kesehatan dapat lebih akurat menentukan jalur pengobatan dan kebutuhan rujukan, sehingga mengoptimalkan manajemen pasien dan mencegah komplikasi serius.
