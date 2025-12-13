import pandas as pd
import math

# Baca data langsung dari CSV
df = pd.read_csv(r'UTI.csv')

# Hitung jumlah setiap temperature
occurance_counts = df['Occurrence of nausea'].value_counts().sort_index()

print(f"\n{'='*60}")
print("Kolom: Occurrence of nausea")
print(f"{'='*60}")

# Loop untuk menampilkan setiap nilai
total = 0
for temp, count in occurance_counts.items():
    print(f"{temp}: {count}")
    total += count

print(f"{'-'*60}")
print(f"TOTAL: {total}")
print(f"{'='*60}\n")

# Hitung ENTROPY
print(f"PERHITUNGAN ENTROPY:")
print(f"{'='*60}")

entropy = 0
for temp, count in occurance_counts.items():
    probability = count / total
    if probability > 0:
        entropy -= probability * math.log2(probability)
    print(f"P({temp}) = {count}/{total} = {probability:.4f}")

print(f"{'-'*60}")
print(f"ENTROPY = {entropy:.4f}")
print(f"{'='*60}\n")