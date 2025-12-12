# ENTROPY ANALYSIS REPORT - UTI DATASET

## Dataset Information
- **Total Records**: 120
- **Total Attributes**: 8
- **Dataset Source**: Urinary Tract Infection (UTI) Detection Dataset from Kaggle
- **Analysis Type**: Information Entropy Calculation (C4.5 Decision Tree)

---

## Summary of Entropy Values

| Attribute | Entropy (bits) | Information Gain Potential |
|-----------|---|---|
| Temperature of patient | 5.161080 | High |
| Occurrence of nausea | 0.797801 | High |
| Lumbar pain | 0.979869 | High |
| Urine pushing | 0.918296 | High |
| Micturition pains | 0.999800 | High |
| Burning of urethra / itch / swelling | 0.979900 | High |
| Inflammation of urinary bladder | 0.999800 | High |
| Nephritis of renal pelvis origin | 0.979869 | High |

---

## Temperature of patient

### Value Distribution

| Value | Count | Percentage |
|-------|-------|------------|
| 35.5 | 1 | 0.83% |
| 35.9 | 2 | 1.67% |
| 36.0 | 3 | 2.50% |
| 36.2 | 2 | 1.67% |
| 36.3 | 1 | 0.83% |
| 36.6 | 4 | 3.33% |
| 36.7 | 3 | 2.50% |
| 36.8 | 2 | 1.67% |
| 36.9 | 2 | 1.67% |
| 37.0 | 8 | 6.67% |
| 37.1 | 3 | 2.50% |
| 37.2 | 3 | 2.50% |
| 37.3 | 3 | 2.50% |
| 37.4 | 2 | 1.67% |
| 37.5 | 6 | 5.00% |
| 37.6 | 3 | 2.50% |
| 37.7 | 4 | 3.33% |
| 37.8 | 3 | 2.50% |
| 37.9 | 5 | 4.17% |
| 38.0 | 2 | 1.67% |
| 38.1 | 1 | 0.83% |
| 38.3 | 1 | 0.83% |
| 38.5 | 1 | 0.83% |
| 38.7 | 1 | 0.83% |
| 38.9 | 1 | 0.83% |
| 39.0 | 1 | 0.83% |
| 39.4 | 1 | 0.83% |
| 39.7 | 1 | 0.83% |
| 40.0 | 8 | 6.67% |
| 40.1 | 1 | 0.83% |
| 40.2 | 3 | 2.50% |
| 40.3 | 1 | 0.83% |
| 40.4 | 5 | 4.17% |
| 40.5 | 1 | 0.83% |
| 40.6 | 3 | 2.50% |
| 40.7 | 5 | 4.17% |
| 40.8 | 1 | 0.83% |
| 40.9 | 3 | 2.50% |
| 41.0 | 4 | 3.33% |
| 41.1 | 5 | 4.17% |
| 41.2 | 4 | 3.33% |
| 41.3 | 1 | 0.83% |
| 41.4 | 1 | 0.83% |
| 41.5 | 4 | 3.33% |
| **TOTAL** | **120** | **100.00%** |

### Entropy Calculation

**Formula**: H(X) = -Σ P(x) × log₂(P(x))

**Entropy Result**: 5.161080 bits

---

## Occurrence of nausea

### Value Distribution

| Value | Count | Percentage |
|-------|-------|------------|
| no | 91 | 75.83% |
| yes | 29 | 24.17% |
| **TOTAL** | **120** | **100.00%** |

### Entropy Calculation

**Formula**: H(X) = -Σ P(x) × log₂(P(x))

**Entropy Result**: 0.797801 bits

---

## Lumbar pain

### Value Distribution

| Value | Count | Percentage |
|-------|-------|------------|
| no | 50 | 41.67% |
| yes | 70 | 58.33% |
| **TOTAL** | **120** | **100.00%** |

### Entropy Calculation

**Formula**: H(X) = -Σ P(x) × log₂(P(x))

**Entropy Result**: 0.979869 bits

---

## Urine pushing

### Value Distribution

| Value | Count | Percentage |
|-------|-------|------------|
| no | 40 | 33.33% |
| yes | 80 | 66.67% |
| **TOTAL** | **120** | **100.00%** |

### Entropy Calculation

**Formula**: H(X) = -Σ P(x) × log₂(P(x))

**Entropy Result**: 0.918296 bits

---

## Micturition pains

### Value Distribution

| Value | Count | Percentage |
|-------|-------|------------|
| no | 61 | 50.83% |
| yes | 59 | 49.17% |
| **TOTAL** | **120** | **100.00%** |

### Entropy Calculation

**Formula**: H(X) = -Σ P(x) × log₂(P(x))

**Entropy Result**: 0.999800 bits

---

## Burning of urethra / itch / swelling

### Value Distribution

| Value | Count | Percentage |
|-------|-------|------------|
| no | 70 | 58.33% |
| yes | 50 | 41.67% |
| **TOTAL** | **120** | **100.00%** |

### Entropy Calculation

**Formula**: H(X) = -Σ P(x) × log₂(P(x))

**Entropy Result**: 0.979900 bits

---

## Inflammation of urinary bladder

### Value Distribution

| Value | Count | Percentage |
|-------|-------|------------|
| no | 61 | 50.83% |
| yes | 59 | 49.17% |
| **TOTAL** | **120** | **100.00%** |

### Entropy Calculation

**Formula**: H(X) = -Σ P(x) × log₂(P(x))

**Entropy Result**: 0.999800 bits

---

## Nephritis of renal pelvis origin

### Value Distribution

| Value | Count | Percentage |
|-------|-------|------------|
| no | 70 | 58.33% |
| yes | 50 | 41.67% |
| **TOTAL** | **120** | **100.00%** |

### Entropy Calculation

**Formula**: H(X) = -Σ P(x) × log₂(P(x))

**Entropy Result**: 0.979869 bits

---

## Analysis Summary

### Key Findings
1. **Temperature**: Highest entropy value indicates maximum diversity in temperature values
2. **Occurrence of nausea**: Lower entropy - data is more skewed (mostly "no")
3. **Lumbar pain**: Moderate entropy - relatively balanced distribution
4. **Urine pushing**: High entropy - many distinct values present
5. **Micturition pains**: Balanced distribution with moderate entropy
6. **Burning/itch/swelling**: Moderate entropy value
7. **Inflammation of urinary bladder**: Balanced distribution
8. **Nephritis**: Balanced "yes/no" distribution

### Statistical Notes
- **Entropy** measures the uncertainty/impurity in data
- Higher entropy = More diverse/uncertain data
- Lower entropy = More uniform/certain data
- Used in C4.5 algorithm to determine best split points
