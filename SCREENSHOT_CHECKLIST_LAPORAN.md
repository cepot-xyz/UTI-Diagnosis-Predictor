# Dokumentasi UTI Inflammation Predictor - Screenshot Checklist

## Untuk Laporan Word/PDF

Panduan lengkap apa saja yang perlu di-screenshot dan dokumentasikan untuk laporan final.

---

## PART 1: DATASET & PREPROCESSING

### 1.1 Dataset Overview
**File:** `01_hitung_data_UTI.py`
**Action:** Jalankan file, screenshot output terminal
```bash
python 01_hitung_data_UTI.py
```
**Capture:** 
- ✅ Seluruh output terminal (dataset shape, columns, info, etc.)
- ✅ Naming: "01_dataset_overview_output.png"

**Deskripsi untuk laporan:**
Output ini menunjukkan:
- Total 120 records dengan 8 kolom (7 atribut + 1 target)
- Semua kolom berisi nilai binary (yes/no)
- Target: "Inflammation of urinary bladder"
- Atribut: Temperature, Occurrence of nausea, Lumbar pain, dll

---

## PART 2: ENTROPY CALCULATION

### 2.1 Entropy - Temperature
**File:** `02_entroper_temperature.py`
**Action:** Jalankan file, screenshot output terminal
```bash
python 02_entroper_temperature.py
```
**Capture:**
- ✅ Entropy calculation hasil
- ✅ Naming: "02_entropy_temperature.png"

### 2.2 Entropy - Semua Atribut (Representative)
**Action:** Jalankan 2-3 file entropy lainnya (pilih berbeda)
```bash
python 03_entroper_occurance.py
python 05_entroper_urine.py
python 09_entroper_nephritis.py
```
**Capture:**
- ✅ Output dari 3 file berbeda
- ✅ Naming: "entropy_[attribute]_output.png"

**Deskripsi untuk laporan:**
Entropy dihitung dari distribusi kelas:
- H(S) = -Σ p(i) × log₂(p(i))
- Menunjukkan tingkat ketidakmurnian data
- Nilai entropy target digunakan untuk menghitung Information Gain

---

## PART 3: INFORMATION GAIN CALCULATION

### 3.1 Information Gain - Representative
**File:** `10_gain_temperature.py`, `12_gain_lumbarpain.py`, `16_gain_inflamation.py`
**Action:** Jalankan 3 file berbeda
```bash
python 10_gain_temperature.py
python 12_gain_lumbarpain.py
python 16_gain_inflamation.py
```
**Capture:**
- ✅ Output terminal dari 3 file
- ✅ Naming: "gain_[attribute]_output.png"

**Deskripsi untuk laporan:**
Information Gain dihitung:
- Gain = H(Target) - H(Target|Atribut)
- Mengukur seberapa banyak informasi didapat dari atribut
- Digunakan dalam ID3 algorithm (lebih tua dari C4.5)

---

## PART 4: GAIN RATIO CALCULATION

### 4.1 Gain Ratio - Representative
**File:** `18_gain_ratio_temperature.py`, `20_gain_ratio_lumbarpain.py`, `24_gain_ratio_inflamation.py`
**Action:** Jalankan 3 file berbeda
```bash
python 18_gain_ratio_temperature.py
python 20_gain_ratio_lumbarpain.py
python 24_gain_ratio_inflamation.py
```
**Capture:**
- ✅ Output terminal dari 3 file
- ✅ Screenshot menunjukkan Gain Ratio value
- ✅ Naming: "gain_ratio_[attribute]_output.png"

**Deskripsi untuk laporan:**
Gain Ratio dihitung:
- Gain Ratio = Information Gain / Split Information
- Split Information = -Σ (|Si|/|S|) × log₂(|Si|/|S|)
- Normalisasi gain untuk mengurangi bias terhadap atribut multi-valued
- Digunakan dalam C4.5 algorithm (improvement dari ID3)
- Contoh: Temperature GR ≈ 0.24, Lumbar pain GR ≈ 0.15, dll

---

## PART 5: TREE BUILDING

### 5.1 Tree Builder Execution
**File:** `25_c45_tree_builder.py`
**Action:** Jalankan file, screenshot full output
```bash
python 25_c45_tree_builder.py
```
**Capture:**
- ✅ Bagian "BUILD C4.5 DECISION TREE" (header)
- ✅ "Dataset shape" sampai "Target distribution"
- ✅ "TREE STATISTICS" section
- ✅ "TREE STRUCTURE" section (ASCII visualization)
- ✅ "ROOT NODE INFORMATION" section
- ✅ Multiple screenshots jika terlalu panjang
- ✅ Naming: "tree_builder_[section]_output.png"

**Deskripsi untuk laporan:**
Output ini menunjukkan:
- Dataset: 120 samples, 8 columns
- Target distribution: no=61 (50.8%), yes=59 (49.2%)
- Tree nodes: 7 total (3 internal, 4 leaf)
- Root node: "Urine pushing" dengan Gain Ratio 0.486
- Tree depth: 3
- Struktur tree dalam format ASCII

### 5.2 File Generated
**File:** `gen_c45_tree.json`
**Action:** Screenshot konten file (partial/full)
```
- Buka file gen_c45_tree.json dengan text editor
- Screenshot struktur JSON tree
```
**Capture:**
- ✅ Root node structure
- ✅ Child nodes (max 3 level untuk clarity)
- ✅ Naming: "gen_c45_tree_json_structure.png"

**Deskripsi untuk laporan:**
JSON tree structure:
- Format: type (internal/leaf), attribute, gain_ratio, children
- Leaf nodes berisi: type, value (yes/no), samples
- Internal nodes berisi: type, attribute, gain_ratio, children dictionary
- Mudah di-parse untuk prediction

---

## PART 6: TREE VISUALIZATION (OPTIONAL)

### 6.1 Run Visualization
**File:** `26_visualize_tree_matplotlib.py`
**Action:** Jalankan file, screenshot output
```bash
python 26_visualize_tree_matplotlib.py
```
**Capture:**
- ✅ Output terminal
- ✅ Naming: "visualization_script_output.png"

### 6.2 Generated Visualization
**File:** `gen_uti_tree.png` (jika ada)
**Action:** Screenshot atau copy file
**Capture:**
- ✅ Tree visualization graphic
- ✅ Naming: "gen_uti_tree_visualization.png"
- ✅ Include dalam laporan

### 6.3 Tree Summary Report
**File:** `gen_tree_summary.txt` (jika ada)
**Action:** Buka dan screenshot konten
**Capture:**
- ✅ Tree statistics section
- ✅ Dataset information section
- ✅ Root node information
- ✅ Naming: "gen_tree_summary_report.png"

**Deskripsi untuk laporan:**
Generated files:
- PNG: Visual representation dari decision tree dengan warna (blue=internal, green=leaf)
- TXT: Summary statistics dan interpretasi model

---

## PART 7: PREDICTION & TESTING

### 7.1 Sample Input File
**File:** `sample_input.txt`
**Action:** Screenshot konten file
**Capture:**
- ✅ Konten sample_input.txt
- ✅ Naming: "sample_input_file_content.png"

**Deskripsi untuk laporan:**
Input format:
- 7 baris (7 atribut)
- Setiap baris: y atau n
- Order: Temperature, Occurrence nausea, Lumbar pain, Urine pushing, Micturition pains, Burning/itch/swelling, Nephritis

### 7.2 Predictor Execution - Full Demo
**File:** `24_predict_diagnosis.py`
**Action:** Jalankan dengan sample input, screenshot output
```bash
Get-Content sample_input.txt | python 24_predict_diagnosis.py
```
**Capture:**
- ✅ "C4.5 DECISION TREE - INFLAMMATION PREDICTOR" header
- ✅ "Loading tree model" dan "Loading dataset" messages
- ✅ "INFLAMMATION PREDICTOR - INPUT PATIENT DATA" section
- ✅ "PROCESSING PREDICTION" section
- ✅ "DECISION PATH" section (PENTING - tunjukkan logic decision tree)
- ✅ "PREDICTION RESULT" section (menunjukkan POSITIVE/NEGATIVE)
- ✅ Multiple screenshots jika terlalu panjang
- ✅ Naming: "predictor_demo_[section]_output.png"

**Deskripsi untuk laporan:**
Demo prediction menunjukkan:
- Model berhasil diload dari gen_c45_tree.json
- Dataset berhasil diload (120, 8)
- User input: 7 atribut (temperature=n, nausea=y, lumbar_pain=n, dll)
- Decision path: "Urine pushing = 'no'" → Prediction: NEGATIVE
- Hasil: No Inflammation (confidence based on C4.5 model)

### 7.3 Multiple Predictions (Different Scenarios)
**Action:** Buat test input variations, jalankan 2-3 scenario berbeda
**Test Case 1:** All "no"
**Test Case 2:** All "yes"
**Test Case 3:** Mixed values
```bash
# Create test files and run each
```
**Capture:**
- ✅ Output dari 3 different prediction scenarios
- ✅ Tunjukkan berbeda decision path untuk berbeda inputs
- ✅ Naming: "prediction_test_case_[1-3]_output.png"

**Deskripsi untuk laporan:**
Multiple test cases menunjukkan:
- Model konsisten dalam prediksi
- Decision path berbeda sesuai input
- Akurasi model pada berbagai kombinasi input
- Robustness dari decision tree

---

## PART 8: SOURCE CODE DOCUMENTATION

### 8.1 Core Files - Key Functions
**File:** `25_c45_tree_builder.py`
**Action:** Screenshot specific sections
**Capture:**
- ✅ Baris 1-50: Import dan entropy function (entropy_from_counts)
- ✅ Baris 75-115: calculate_gain_ratio function
- ✅ Baris 120-160: find_best_attribute function
- ✅ Baris 175-240: build_tree function (main recursive)
- ✅ Naming: "code_25_tree_builder_section_[name].png"

**Deskripsi untuk laporan:**
Kode menunjukkan:
- Implementasi entropy calculation
- Implementasi gain ratio computation
- Implementasi recursive tree building
- Stopping criteria untuk pruning

### 8.2 Predictor Code - Key Functions
**File:** `24_predict_diagnosis.py`
**Action:** Screenshot specific sections
**Capture:**
- ✅ Baris 1-30: Load tree function
- ✅ Baris 35-60: predict_single function (traversal logic)
- ✅ Baris 65-100: get_input_from_user function
- ✅ Baris 105-160: main loop logic
- ✅ Naming: "code_24_predictor_section_[name].png"

**Deskripsi untuk laporan:**
Kode menunjukkan:
- Loading model dari JSON
- Tree traversal logic untuk prediksi
- User input handling dan validation
- Output formatting

---

## PART 9: EXECUTION GUIDE

### 9.1 README/Documentation File
**File:** `Urutan Eksekusi.md`
**Action:** Screenshot atau screenshot section-by-section
**Capture:**
- ✅ QUICK START section
- ✅ Phase 3 & 5 (tree building & prediction)
- ✅ Troubleshooting section
- ✅ Naming: "doc_urutan_eksekusi_[section].png"

**Deskripsi untuk laporan:**
Dokumentasi menunjukkan:
- Clear step-by-step execution order
- Minimum steps untuk run predictor
- File dependencies
- Troubleshooting guide

---

## PART 10: REPOSITORY STRUCTURE

### 10.1 File Listing
**Action:** Screenshot output dari file listing
```bash
dir /B "c:\Users\user\Storage\Kampus\Semester 5\Data Mining\UAS\UTI Diagnosis Predictor"
```
**Capture:**
- ✅ File listing di terminal
- ✅ Naming: "repo_file_listing.png"

**Deskripsi untuk laporan:**
File structure menunjukkan:
- Core files (24, 25, 26, UTI.csv, gen_c45_tree.json)
- Educational files (01-25 files untuk learning)
- Documentation (Urutan Eksekusi.md)
- Clean dan terstruktur

---

## SUMMARY TABLE - Untuk Copy-Paste ke Word

```markdown
| NO | Kategori | File/Action | Screenshot Name | Deskripsi |
|----|----------|-------------|-----------------|-----------|
| 1  | Dataset | 01_hitung_data_UTI.py output | 01_dataset_overview_output.png | Dataset info & structure |
| 2  | Entropy | 02_entroper_temperature.py output | entropy_temperature_output.png | Entropy calculation contoh |
| 3  | Entropy | 03_entroper_occurance.py output | entropy_nausea_output.png | Entropy calculation contoh |
| 4  | Entropy | 09_entroper_nephritis.py output | entropy_nephritis_output.png | Entropy calculation contoh |
| 5  | Gain | 10_gain_temperature.py output | gain_temperature_output.png | Information Gain contoh |
| 6  | Gain | 12_gain_lumbarpain.py output | gain_lumbar_output.png | Information Gain contoh |
| 7  | Gain | 16_gain_inflamation.py output | gain_inflammation_output.png | Information Gain contoh |
| 8  | Gain Ratio | 18_gain_ratio_temperature.py output | gain_ratio_temperature_output.png | Gain Ratio calculation |
| 9  | Gain Ratio | 20_gain_ratio_lumbarpain.py output | gain_ratio_lumbar_output.png | Gain Ratio calculation |
| 10 | Gain Ratio | 24_gain_ratio_inflamation.py output | gain_ratio_inflammation_output.png | Gain Ratio calculation |
| 11 | Tree Building | 25_c45_tree_builder.py output (part 1) | tree_builder_header_output.png | Tree building start |
| 12 | Tree Building | 25_c45_tree_builder.py output (part 2) | tree_builder_stats_output.png | Tree statistics |
| 13 | Tree Building | 25_c45_tree_builder.py output (part 3) | tree_builder_structure_output.png | ASCII tree structure |
| 14 | Tree Building | 25_c45_tree_builder.py output (part 4) | tree_builder_root_output.png | Root node info |
| 15 | JSON Output | gen_c45_tree.json content | gen_c45_tree_json_structure.png | JSON tree format |
| 16 | Visualization | 26_visualize_tree_matplotlib.py output | visualization_script_output.png | Visualization script execution |
| 17 | Generated Image | gen_uti_tree.png | gen_uti_tree_visualization.png | Visual tree diagram |
| 18 | Generated Report | gen_tree_summary.txt content | gen_tree_summary_report.png | Model summary statistics |
| 19 | Test Input | sample_input.txt content | sample_input_file_content.png | Test case input |
| 20 | Prediction Demo | 24_predict_diagnosis.py output (case 1) | predictor_demo_case1_output.png | Prediction result case 1 |
| 21 | Prediction Demo | 24_predict_diagnosis.py output (case 2) | predictor_demo_case2_output.png | Prediction result case 2 |
| 22 | Prediction Demo | 24_predict_diagnosis.py output (case 3) | predictor_demo_case3_output.png | Prediction result case 3 |
| 23 | Source Code | 25_c45_tree_builder.py (lines 1-50) | code_tree_builder_entropy.png | Entropy functions |
| 24 | Source Code | 25_c45_tree_builder.py (lines 75-115) | code_tree_builder_gain_ratio.png | Gain ratio function |
| 25 | Source Code | 25_c45_tree_builder.py (lines 120-160) | code_tree_builder_best_attr.png | Find best attribute |
| 26 | Source Code | 25_c45_tree_builder.py (lines 175-240) | code_tree_builder_build_tree.png | Build tree recursive |
| 27 | Source Code | 24_predict_diagnosis.py (lines 1-30) | code_predictor_load.png | Load tree function |
| 28 | Source Code | 24_predict_diagnosis.py (lines 35-60) | code_predictor_predict.png | Predict function |
| 29 | Source Code | 24_predict_diagnosis.py (lines 65-100) | code_predictor_input.png | Get input function |
| 30 | Documentation | Urutan Eksekusi.md (Quick Start) | doc_urutan_quick_start.png | Execution guide |
| 31 | Documentation | Urutan Eksekusi.md (Phase 3 & 5) | doc_urutan_phases.png | Tree building & prediction |
| 32 | Repository | File listing output | repo_file_listing.png | Repository structure |
```

---

## NOTES UNTUK LAPORAN WORD

### Cara Organize:

**Bab 1: Dataset & Preprocessing**
- Screenshot 01 (dataset overview)
- Penjelasan struktur data
- Penjelasan kolom dan nilai

**Bab 2: Information Theory & Feature Selection**
- Entropy concept (include formula)
- Screenshots entropy calculation (02, 03, 09)
- Information Gain concept (include formula)
- Screenshots gain calculation (10, 12, 16)
- Gain Ratio concept (include formula + explanation C4.5 vs ID3)
- Screenshots gain ratio calculation (18, 20, 24)

**Bab 3: Decision Tree Building**
- C4.5 Algorithm explanation
- Tree building process explanation
- Screenshots tree builder execution (11-14)
- JSON output explanation
- Screenshot JSON structure (15)

**Bab 4: Visualization & Interpretation**
- Visualization script explanation
- Screenshots visualization output (16, 17, 18)
- Tree structure analysis
- Root node interpretation

**Bab 5: Model Prediction & Testing**
- Predictor system explanation
- Input format explanation
- Screenshot sample input (19)
- Screenshots prediction results (20, 21, 22)
- Analysis of decision paths

**Bab 6: Implementation Details**
- Source code walkthrough
- Screenshots key functions (23-29)
- Penjelasan algoritma dalam code

**Bab 7: Documentation & Execution**
- User guide
- Screenshots documentation (30, 31)
- Step-by-step execution
- Repository overview (32)

---

## CHECKLIST - Sebelum Masukkan ke Word

```
SCREENSHOTS COMPLETION:
□ Dataset overview (1 screenshot)
□ Entropy examples (3 screenshots)
□ Information gain examples (3 screenshots)
□ Gain ratio examples (3 screenshots)
□ Tree building output (4 screenshots)
□ JSON structure (1 screenshot)
□ Visualization output (1 screenshot)
□ Generated image (1 screenshot)
□ Generated report (1 screenshot)
□ Sample input (1 screenshot)
□ Prediction results (3 screenshots)
□ Source code sections (7 screenshots)
□ Documentation (2 screenshots)
□ Repository structure (1 screenshot)

TOTAL: 32 screenshots

CODE SECTIONS:
□ Key algorithms documented
□ Formulas included
□ Explanations clear
□ Outputs interpreted

DELIVERABLE:
□ Semua screenshots organized
□ Naming consistent
□ Descriptions written
□ Table of contents ready
□ Ready for Word insertion
```

---

## FINAL TIPS

1. **Screenshot Tools:**
   - Gunakan Snipping Tool (Windows) atau ShareX untuk SS berkualitas
   - Set resolution tinggi untuk clarity
   - Highlight important parts dengan arrow/annotation

2. **File Organization:**
   - Buat folder "Screenshots_Laporan" untuk menyimpan semua SS
   - Gunakan naming konsisten
   - Keep backup dari semua files

3. **Word Format:**
   - Masukkan SS dengan caption
   - Include figure numbers (Figure 1.1, 1.2, dll)
   - Cross-reference dalam text
   - Resize SS agar readable (tidak terlalu kecil)

4. **Quality Check:**
   - Verify semua outputs benar
   - Check file paths konsisten
   - Verify code readability
   - Check bahwa semua claims supported oleh screenshots

---

Dengan checklist ini, laporan akan **lengkap, terstruktur, dan profesional**! 📄✅
