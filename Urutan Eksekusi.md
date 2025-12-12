# UTI Inflammation Predictor - Execution Order

## Step-by-Step untuk Menjalankan Predictor

File terakhir yang akan dijalankan: **24_predict_diagnosis.py**

---

## Phase 1: Data Analysis & Entropy Calculation

**Tujuan:** Understand dataset dan calculate entropy untuk setiap atribut

### 1. [REQUIRED] `01_hitung_data_UTI.py`
- **Input:** `UTI.csv`
- **Output:** Dataset overview, basic statistics
- **Tujuan:** Validate dataset, lihat struktur data

### 2. [OPTIONAL] `02-09_entroper_*.py`
- **Input:** `UTI.csv`
- **Output:** Entropy values per attribute
- **Tujuan:** Educational - understand information theory
- **Note:** Bisa skip jika ingin cepat ke prediction

---

## Phase 2: Gain & Gain Ratio Calculation

**Tujuan:** Calculate Information Gain dan Gain Ratio untuk feature selection

### 3. [OPTIONAL] `10-17_gain_*.py`
- **Input:** `UTI.csv`
- **Output:** Gain values
- **Tujuan:** Educational - compare dengan Gain Ratio
- **Note:** Bisa skip jika ingin cepat

### 4. [OPTIONAL] `18-25_gain_ratio_*.py`
- **Input:** `UTI.csv`
- **Output:** Gain Ratio values
- **Tujuan:** Educational - see which attributes are best
- **Note:** Bisa skip jika ingin cepat

---

## Phase 3: Build Decision Tree (REQUIRED)

**Tujuan:** Build C4.5 Decision Tree model

### 5. [REQUIRED] `25_c45_tree_builder.py`
- **Input:** `UTI.csv`
- **Output:** `gen_c45_tree.json` (tree model)
- **Tujuan:** Build the actual decision tree
- ⚠️ **WAJIB dijalankan sebelum prediction!**
- **Important:** Nama file output harus `gen_c45_tree.json` (predictor akan memuat file ini)

---

## Phase 4: Visualization (OPTIONAL)

**Tujuan:** Visualisasi tree structure

### 6. [OPTIONAL] `26_visualize_tree_matplotlib.py`
- **Input:** `gen_c45_tree.json` (dari Step 5)
- **Output:**
  - `gen_uti_tree.png` (gambar tree)
  - `gen_tree_summary.txt` (text report)
- **Tujuan:** Lihat struktur tree visually
- **Note:** Bisa skip jika hanya mau prediction

---

## Phase 5: Prediction (FINAL)

**Tujuan:** Predict inflammation status berdasarkan gejala pasien

### 7. [REQUIRED] `24_predict_diagnosis.py`
- **Input:** 
  - `gen_c45_tree.json` (dari Step 5)
  - `UTI.csv` (untuk structure)
- **Output:** Interactive prediction di terminal
- **Tujuan:** Main program untuk diagnosis
- ⚠️ **HARUS menjalankan Step 5 terlebih dahulu!**

---

## Quick Start (Minimal)

Jika ingin langsung ke prediction tanpa tahap analysis:

```bash
# Step 1: Build tree model
python 25_c45_tree_builder.py

# Step 2: Run predictor
python 24_predict_diagnosis.py
```

---

## Demo dengan Sample Input

```bash
# PowerShell
Get-Content sample_input.txt | python 24_predict_diagnosis.py
```

---

## Files untuk Cleanup (Bisa Dihapus)

### Duplikat/Deprecated:
- `26_split_data.py` (fungsi sudah integrated di tree builder)
- `27_c45_tree_builder.py` (duplikat dari 25_c45_tree_builder.py)
- `28_visualize_tree_matplotlib.py` (duplikat dari 26_visualize_tree_matplotlib.py)
- `29_c45_tree.json` (old tree file)
- `30_predict_diagnosis.py` (old predictor)
- `32_c45_tree_builder.py` (old naming)
- `32_c45_tree.json` (old file)
- `33_predict_diagnosis.py` (old naming)
- `34_visualize_tree_matplotlib.py` (old naming)
- `35_predict_diagnosis.py` (old naming)
- `README_EXECUTION_ORDER.txt` (old documentation)

### Optional (Educational):
- `01_hitung_data_UTI.py`
- `02-09_entroper_*.py`
- `10-17_gain_*.py`
- `18-25_gain_ratio_*.py` (kecuali 25_c45_tree_builder.py)
- `exp_gain_temperature.py`
- `entroper_report.md`
- `nilai perdata.md`

### Keep (REQUIRED):
- ✅ `25_c45_tree_builder.py`
- ✅ `24_predict_diagnosis.py`
- ✅ `26_visualize_tree_matplotlib.py` (optional but recommended)
- ✅ `UTI.csv`
- ✅ `gen_c45_tree.json` (generated file)

---

## File Naming Convention

### Source Files (Non-Generated)
```
[number]_[purpose]_[optional_attribute].py
```

Contoh:
- `25_c45_tree_builder.py`
- `24_predict_diagnosis.py`
- `26_visualize_tree_matplotlib.py`

### Generated Files (Output)
```
gen_[purpose].json
gen_[purpose].png
gen_[purpose].txt
```

Contoh:
- `gen_c45_tree.json` (tree model)
- `gen_uti_tree.png` (visualization)
- `gen_tree_summary.txt` (report)

---

## Troubleshooting

| Error | Solusi |
|-------|--------|
| `FileNotFoundError: gen_c45_tree.json` | Jalankan `25_c45_tree_builder.py` terlebih dahulu |
| `ModuleNotFoundError: pandas` | `pip install pandas` |
| `ModuleNotFoundError: matplotlib` | `pip install matplotlib` (hanya jika pakai visualization) |

---

## Summary

| Phase | File | Required | Output |
|-------|------|----------|--------|
| 1 | 01_hitung_data_UTI.py | ❌ Optional | Dataset overview |
| 2 | 02-09_entroper_*.py | ❌ Optional | Entropy values |
| 3 | 10-17_gain_*.py | ❌ Optional | Information Gain |
| 4 | 18-25_gain_ratio_*.py | ❌ Optional | Gain Ratio |
| **5** | **25_c45_tree_builder.py** | **✅ REQUIRED** | **gen_c45_tree.json** |
| 6 | 26_visualize_tree_matplotlib.py | ❌ Optional | PNG + Text Report |
| **7** | **24_predict_diagnosis.py** | **✅ REQUIRED** | **Interactive Predictor** |
