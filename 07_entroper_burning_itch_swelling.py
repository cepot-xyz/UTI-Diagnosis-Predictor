import pandas as pd
import math

df = pd.read_csv(r'UTI.csv')

burning_counts = df['Burning of urethra, itch, swelling of urethra outlet'].value_counts().sort_index()

print(f"\n{'='*60}")
print("Kolom: Burning of urethra, itch, swelling of urethra outlet")
print(f"{'='*60}")

total = 0
for temp, count in burning_counts.items():
    print(f"{temp}: {count}")
    total += count

print(f"{'-'*60}")
print(f"TOTAL: {total}")
print(f"{'='*60}\n")

print(f"PERHITUNGAN ENTROPY:")
print(f"{'='*60}")

entropy = 0
for temp, count in burning_counts.items():
    probability = count / total
    if probability > 0:
        entropy -= probability * math.log2(probability)
    print(f"P({temp}) = {count}/{total} = {probability:.4f}")

print(f"{'-'*60}")
print(f"ENTROPY = {entropy:.4f}")
print(f"{'='*60}\n")