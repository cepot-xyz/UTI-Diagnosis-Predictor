import pandas as pd
import math
from typing import Sequence, Optional

# Konfigurasi
CSV_PATH = r'UTI.csv'
TARGET = 'Inflammation of urinary bladder'


def entropy_from_counts(counts: Sequence[int]) -> float:
    """Hitung entropy dari daftar hitungan kelas."""
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
    """Hitung entropy dari sebuah pandas Series."""
    counts = series.value_counts().tolist()
    return entropy_from_counts(counts)


def split_information(df: pd.DataFrame, attribute: str) -> float:
    """Hitung Split Information (Intrinsic Value)."""
    total = len(df)
    split_info = 0.0
    
    for attr_value, group in df.groupby(attribute):
        weight = len(group) / total
        if weight > 0:
            split_info -= weight * math.log2(weight)
    
    return split_info


def calculate_gain_ratio(df: pd.DataFrame, attribute: str, target: str) -> float:
    """Hitung Gain Ratio untuk atribut tertentu."""
    H_target = entropy_of_series(df[target])
    
    total = len(df)
    conditional_entropy = 0.0
    
    for attr_value, group in df.groupby(attribute):
        weight = len(group) / total
        H_sub = entropy_of_series(group[target])
        conditional_entropy += weight * H_sub
    
    gain = H_target - conditional_entropy
    split_info = split_information(df, attribute)
    
    if split_info == 0:
        gain_ratio = 0.0
    else:
        gain_ratio = gain / split_info
    
    return gain_ratio


def find_best_attribute(df: pd.DataFrame, target: str, excluded_attrs: list = None) -> Optional[str]:
    """Temukan atribut dengan Gain Ratio tertinggi."""
    if excluded_attrs is None:
        excluded_attrs = []
    
    attributes = [col for col in df.columns if col != target and col not in excluded_attrs]
    
    if not attributes:
        return None
    
    best_attr = None
    best_ratio = -1
    
    for attr in attributes:
        ratio = calculate_gain_ratio(df, attr, target)
        if ratio > best_ratio:
            best_ratio = ratio
            best_attr = attr
    
    return best_attr


def is_pure(series: pd.Series) -> bool:
    """Cek apakah semua nilai dalam series sama (node pure/leaf)."""
    return len(series.unique()) == 1


def get_majority_class(series: pd.Series) -> str:
    """Dapatkan kelas mayoritas dari series."""
    return series.value_counts().idxmax()


def build_tree(
    df: pd.DataFrame,
    target: str,
    excluded_attrs: list = None,
    min_samples: int = 1,
    depth: int = 0,
    max_depth: int = None
) -> dict:
    """
    Build C4.5 decision tree secara rekursif.
    
    Parameters:
    -----------
    df : DataFrame
        Dataset untuk membangun tree
    target : str
        Nama kolom target
    excluded_attrs : list
        Atribut yang sudah digunakan (untuk rekursi)
    min_samples : int
        Minimum samples untuk split node
    depth : int
        Kedalaman tree saat ini (internal)
    max_depth : int
        Maximum kedalaman tree (None = unlimited)
    
    Returns:
    --------
    dict : Tree node (bisa internal node atau leaf node)
    """
    if excluded_attrs is None:
        excluded_attrs = []
    
    target_series = df[target]
    
    # STOPPING CRITERIA 1: Node adalah pure (semua nilai target sama)
    if is_pure(target_series):
        leaf_value = target_series.iloc[0]
        return {
            'type': 'leaf',
            'value': leaf_value,
            'samples': len(df)
        }
    
    # STOPPING CRITERIA 2: Tidak ada sample yang cukup untuk split
    if len(df) < min_samples:
        majority = get_majority_class(target_series)
        return {
            'type': 'leaf',
            'value': majority,
            'samples': len(df)
        }
    
    # STOPPING CRITERIA 3: Sudah mencapai maximum depth
    if max_depth is not None and depth >= max_depth:
        majority = get_majority_class(target_series)
        return {
            'type': 'leaf',
            'value': majority,
            'samples': len(df)
        }
    
    # STOPPING CRITERIA 4: Tidak ada atribut tersisa untuk split
    best_attr = find_best_attribute(df, target, excluded_attrs)
    if best_attr is None:
        majority = get_majority_class(target_series)
        return {
            'type': 'leaf',
            'value': majority,
            'samples': len(df)
        }
    
    # BUILD INTERNAL NODE
    node = {
        'type': 'internal',
        'attribute': best_attr,
        'samples': len(df),
        'gain_ratio': calculate_gain_ratio(df, best_attr, target),
        'children': {}
    }
    
    # Split data berdasarkan atribut terbaik
    new_excluded = excluded_attrs + [best_attr]
    
    for attr_value, subset in df.groupby(best_attr):
        # Rekursi untuk setiap branch
        child_node = build_tree(
            subset.reset_index(drop=True),
            target,
            excluded_attrs=new_excluded,
            min_samples=min_samples,
            depth=depth + 1,
            max_depth=max_depth
        )
        
        node['children'][attr_value] = child_node
    
    return node


def count_nodes(node: dict) -> tuple:
    """
    Hitung jumlah internal nodes dan leaf nodes.
    
    Returns:
    --------
    tuple : (internal_count, leaf_count)
    """
    if node['type'] == 'leaf':
        return (0, 1)
    
    internal_count = 1
    leaf_count = 0
    
    for child in node['children'].values():
        child_internal, child_leaf = count_nodes(child)
        internal_count += child_internal
        leaf_count += child_leaf
    
    return (internal_count, leaf_count)


def print_tree(node: dict, prefix: str = "", attribute_name: str = "Root", attribute_value: str = ""):
    """
    Print tree structure dalam format text yang readable.
    """
    if node['type'] == 'leaf':
        print(f"{prefix}└─ Prediksi: {node['value']} (samples: {node['samples']})")
    else:
        # Print attribute
        attr = node['attribute']
        print(f"{prefix}└─ {attr} ?")
        
        # Print setiap branch
        branches = list(node['children'].keys())
        for i, value in enumerate(branches):
            is_last = (i == len(branches) - 1)
            child = node['children'][value]
            
            branch_prefix = prefix + ("   " if is_last else "│  ")
            print(f"{prefix}{'   ' if is_last else '│  '}├─ {attr} = '{value}':")
            
            print_tree(child, branch_prefix, attr, str(value))


def save_tree_to_json(node: dict, filepath: str):
    """
    Save tree ke file JSON untuk analisis lebih lanjut.
    """
    import json
    
    # Convert tree to JSON-serializable format
    def convert_node(n):
        if n['type'] == 'leaf':
            return {
                'type': 'leaf',
                'value': str(n['value']),
                'samples': n['samples']
            }
        else:
            return {
                'type': 'internal',
                'attribute': n['attribute'],
                'samples': n['samples'],
                'gain_ratio': round(n['gain_ratio'], 6),
                'children': {
                    str(k): convert_node(v) for k, v in n['children'].items()
                }
            }
    
    tree_json = convert_node(node)
    
    with open(filepath, 'w') as f:
        json.dump(tree_json, f, indent=2)


def main():
    # Muat data
    df = pd.read_csv(CSV_PATH)
    
    print("="*100)
    print("BUILD C4.5 DECISION TREE - INFLAMMATION PREDICTION")
    print("="*100)
    print(f"\nDataset shape: {df.shape}")
    print(f"Target variable: {TARGET}")
    print(f"Target distribution:\n{df[TARGET].value_counts()}\n")
    
    # Build tree
    print("\n" + "="*100)
    print("BUILDING TREE...")
    print("="*100 + "\n")
    
    tree = build_tree(df, TARGET, min_samples=1, max_depth=None)
    
    # Statistik tree
    internal_count, leaf_count = count_nodes(tree)
    total_nodes = internal_count + leaf_count
    
    print("\nTREE STATISTICS:")
    print(f"  Total nodes: {total_nodes}")
    print(f"  Internal nodes: {internal_count}")
    print(f"  Leaf nodes: {leaf_count}\n")
    
    # Visualisasi tree
    print("\n" + "="*100)
    print("TREE STRUCTURE:")
    print("="*100 + "\n")
    print_tree(tree)
    
    # Save tree
    print("\n" + "="*100)
    print("SAVING TREE...")
    print("="*100)
    
    tree_json_path = 'gen_c45_tree.json'
    save_tree_to_json(tree, tree_json_path)
    print(f"[OK] Tree saved to: {tree_json_path}\n")
    
    # Print beberapa informasi detail tentang root node
    print("\n" + "="*100)
    print("ROOT NODE INFORMATION:")
    print("="*100)
    if tree['type'] == 'internal':
        print(f"Splitting attribute: {tree['attribute']}")
        print(f"Gain Ratio: {tree['gain_ratio']:.6f}")
        print(f"Samples at root: {tree['samples']}")
        print(f"Number of branches: {len(tree['children'])}")
        print(f"Branch values: {list(tree['children'].keys())}")
    
    print("\n" + "="*100 + "\n")
    
    return tree


if __name__ == '__main__':
    tree = main()
