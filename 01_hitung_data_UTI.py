import pandas as pd

# Baca CSV file
csv_file = r'UTI.csv'
df = pd.read_csv(csv_file)

def count_column_values(dataframe, column_name):
    print(f"\n{'='*60}")
    print(f"Kolom: {column_name}")
    print(f"{'='*60}")
    
    # Hitung nilai
    value_counts = dataframe[column_name].value_counts().sort_index()
    
    # Tampilkan hasil
    for value, count in value_counts.items():
        print(f"{value:15} : {count}")
    
    print(f"{'-'*60}")
    print(f"{'TOTAL':15} : {value_counts.sum()}")
    print(f"{'='*60}\n")

count_column_values(df, "Occurrence of nausea")

count_column_values(df, "Temperature of patient")

count_column_values(df, "Lumbar pain")

count_column_values(df, "Urine pushing (continuous need for urination)")

count_column_values(df, "Nephritis of renal pelvis origin")