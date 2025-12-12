import pandas as pd
import math
from typing import Sequence

# Konfigurasi sederhana — ubah sesuai kebutuhan untuk atribut/target lain
CSV_PATH = r'UTI.csv'
ATTRIBUTE = 'Micturition pains'  # contoh: 'Micturition pains'
TARGET = 'Nephritis of renal pelvis origin'  # kolom target untuk dihitung Gain


def entropy_from_counts(counts: Sequence[int]) -> float:
    """Hitung entropy dari daftar hitungan kelas.

    Rumus: H = - sum(p * log2(p)) dengan p = count / total
    """
    total = sum(counts)
    if total == 0:
        return 0.0
    ent = 0.0
    for c in counts:
        if c <= 0:
            continue
        p = c / total
        ent -= p * math.log2(p)
    return ent


def entropy_of_series(series: pd.Series) -> float:
    """Hitung entropy dari sebuah pandas Series dengan menghitung frekuensi tiap nilai."""
    counts = series.value_counts().tolist()
    return entropy_from_counts(counts)


def information_gain(df: pd.DataFrame, attribute: str, target: str) -> float:
    """Hitung Information Gain: Gain(Target, Attribute).

    Alur ringkas:
    1. Hitung entropy target sebelum split (H_target).
    2. Bagi data berdasarkan tiap nilai attribute.
    3. Untuk tiap grup, hitung entropy target di grup itu dan bobotnya.
    4. Entropy kondisional = jumlah(bobot * entropy_grup).
    5. Gain = H_target - H_kondisional.

    Catatan: fungsi ini menganggap attribute bersifat diskret.
    Untuk attribute numerik (mis. Temperature) pertimbangkan binning
    atau mencari threshold terbaik terlebih dahulu.
    """
    # Entropy target sebelum splitting
    H_target = entropy_of_series(df[target])

    # Hitung entropy kondisional H(Target | Attribute)
    total = len(df)
    conditional_entropy = 0.0
    print(f"Entropy(Target={target}) = {H_target:.6f}\n")
    print(f"Membagi berdasarkan Attribute={attribute}")
    for attr_value, group in df.groupby(attribute):
        weight = len(group) / total
        H_sub = entropy_of_series(group[target])
        conditional_entropy += weight * H_sub
        # Menampilkan rincian agar mudah dipahami
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
