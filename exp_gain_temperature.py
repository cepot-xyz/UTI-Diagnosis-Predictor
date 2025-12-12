import pandas as pd
import math
from typing import Sequence

# Salinan dari `10_gain_temperature.py` — ditambah komentar penjelasan alur
# File ini menghitung Information Gain untuk atribut "Temperature of patient"
# terhadap target "Nephritis of renal pelvis origin" pada dataset CSV.
#
# Penjelasan singkat alur/algoritma (bahasa Indonesia):
# 1) Baca dataset dari file CSV menjadi DataFrame pandas.
# 2) Hitung entropy target sebelum pemisahan (H_target). Entropy mengukur
#    ketidakpastian distribusi kelas target. Rumus: H = - sum(p * log2(p)).
#    p adalah probabilitas masing-masing kelas (frekuensi dibagi total).
# 3) Bagi dataset menurut setiap nilai yang mungkin dari atribut.
# 4) Untuk setiap kelompok (group) dengan nilai atribut tertentu,
#    hitung entropy target di dalam kelompok itu (H_sub) — ini adalah
#    ketidakpastian target setelah melihat nilai atribut.
# 5) Bobotkan setiap entropy kelompok dengan proporsi ukuran kelompok
#    (weight = |group| / |total|). Hitung entropy kondisional
#    H(Target | Attribute) = sum_over_groups(weight * H_sub).
# 6) Information Gain didefinisikan sebagai selisih:
#    Gain = H_target - H(Target | Attribute).
#    Artinya: seberapa banyak ketidakpastian target berkurang jika
#    kita mengetahui nilai attribute.
#
# Catatan praktis:
# - Fungsi ini mengasumsikan attribute bersifat diskrit. Jika atribut
#   numerik (seperti suhu), biasanya perlu melakukan binning atau
#   mencari threshold terbaik untuk menjadi diskrit terlebih dahulu.
# - Entropy bernilai >= 0; jika semua contoh punya kelas sama, entropy = 0.
# - Kita mengabaikan kontribusi dari kelas dengan hitungan 0 untuk
#   menghindari log2(0).

# Konfigurasi sederhana — ubah sesuai kebutuhan untuk atribut/target lain
CSV_PATH = r'UTI.csv'
ATTRIBUTE = 'Temperature of patient'  # contoh: 'Temperature of patient'
TARGET = 'Nephritis of renal pelvis origin'  # kolom target untuk dihitung Gain


def entropy_from_counts(counts: Sequence[int]) -> float:
    """Hitung entropy dari daftar hitungan kelas.

    Penjelasan:
    - 'counts' adalah daftar frekuensi tiap kelas target (mis. [10, 5] untuk dua kelas).
    - Probabilitas tiap kelas p_i = counts[i] / total.
    - Entropy H = - sum_i p_i * log2(p_i).
    - Jika total = 0 (tidak ada contoh), kembalikan 0.0 sebagai keamanan.
    - Abaikan kelas dengan hitungan 0 supaya tidak memanggil log2(0).
    """
    total = sum(counts)
    if total == 0:
        return 0.0
    ent = 0.0
    for c in counts:
        if c <= 0:
            # jika tidak ada contoh untuk kelas ini, kontribusi entropy = 0
            continue
        p = c / total
        ent -= p * math.log2(p)
    return ent


def entropy_of_series(series: pd.Series) -> float:
    """Hitung entropy dari sebuah pandas Series dengan menghitung frekuensi tiap nilai.

    Series ini biasanya adalah kolom target (label). Kita ambil value_counts()
    untuk mendapatkan jumlah per kelas lalu serahkan ke entropy_from_counts().
    """
    counts = series.value_counts().tolist()
    return entropy_from_counts(counts)


def information_gain(df: pd.DataFrame, attribute: str, target: str) -> float:
    """Hitung Information Gain: Gain(Target, Attribute).

    Langkah detail yang dilakukan fungsi ini:
    1) Hitung entropy target sebelum split: H_target = entropy_of_series(df[target]).
    2) Lakukan groupby pada kolom attribute (membagi dataset berdasarkan nilai-nilai attribute).
    3) Untuk setiap grup dengan nilai attribute tertentu:
       - Hitung proporsi (weight) = len(group) / total.
       - Hitung entropy target pada grup itu (H_sub).
       - Tambahkan weight * H_sub ke entropy kondisional.
    4) Entropy kondisional H(Target | Attribute) adalah jumlah bobot-terbobot di atas.
    5) Gain = H_target - H(Target | Attribute).

    Catatan: hasil Gain positif menunjukkan bahwa attribute
    mengurangi ketidakpastian target (bagus untuk split). Semakin besar Gain,
    semakin informatif attribute tersebut terhadap target.
    """
    # Entropy target sebelum splitting
    H_target = entropy_of_series(df[target])

    # Hitung entropy kondisional H(Target | Attribute)
    total = len(df)
    conditional_entropy = 0.0
    print(f"Entropy(Target={target}) = {H_target:.6f}\n")
    print(f"Membagi berdasarkan Attribute={attribute}")

    # df.groupby(attribute) menghasilkan pasangan (nilai_attribute, group_dataframe)
    for attr_value, group in df.groupby(attribute):
        # weight = proporsi contoh yang memiliki nilai attribute tertentu
        weight = len(group) / total
        # H_sub = entropy target jika kita tahu nilai attribute = attr_value
        H_sub = entropy_of_series(group[target])
        conditional_entropy += weight * H_sub
        # Menampilkan rincian agar mudah dipahami — berguna untuk debugging/penjelasan
        print(
            f"Nilai '{attr_value}': count={len(group)}, weight={weight:.6f}, "
            f"H(Target|{attribute}={attr_value})={H_sub:.6f}"
        )

    gain = H_target - conditional_entropy
    print(f"\nEntropy kondisional H(Target|{attribute}) = {conditional_entropy:.6f}")
    print(f"Information Gain(Target, {attribute}) = {gain:.6f}\n")
    return gain


def main():
    # Muat data dari file CSV
    df = pd.read_csv(CSV_PATH)

    # Validasi kolom agar kesalahan cepat terdeteksi
    if ATTRIBUTE not in df.columns:
        raise KeyError(f"Kolom attribute '{ATTRIBUTE}' tidak ditemukan. Kolom tersedia: {list(df.columns)}")
    if TARGET not in df.columns:
        raise KeyError(f"Kolom target '{TARGET}' tidak ditemukan. Kolom tersedia: {list(df.columns)}")

    print(f"Memuat {len(df)} baris dari '{CSV_PATH}'")
    information_gain(df, ATTRIBUTE, TARGET)


if __name__ == '__main__':
    main()
