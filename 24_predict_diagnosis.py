import json
import pandas as pd

# Konfigurasi
TREE_JSON_PATH = r'gen_c45_tree.json'
CSV_PATH = r'UTI.csv'
TARGET = 'Inflammation of urinary bladder'


def load_tree(filepath: str) -> dict:
    """Load tree dari JSON file."""
    with open(filepath, 'r') as f:
        return json.load(f)


def load_data(filepath: str) -> pd.DataFrame:
    """Load dataset untuk mendapatkan column names."""
    return pd.read_csv(filepath)


def predict_single(tree: dict, sample: dict) -> tuple:
    """
    Predict diagnosis untuk single sample.
    
    Returns:
    --------
    tuple : (prediction, decision_path)
    """
    path = []
    node = tree
    
    while node['type'] == 'internal':
        attr = node['attribute']
        sample_value = sample.get(attr)
        
        if sample_value not in node['children']:
            return (None, path + [f"ERROR: Unseen value '{sample_value}' for {attr}"])
        
        path.append(f"  -> {attr} = '{sample_value}'")
        node = node['children'][sample_value]
    
    prediction = node['value']
    return (prediction, path)


def get_input_from_user(df: pd.DataFrame, target: str) -> dict:
    """
    Get input dari user untuk semua atribut kecuali target dan Temperature.
    
    Parameters:
    -----------
    df : DataFrame
        Dataset untuk mendapatkan list kolom
    target : str
        Nama target column
    
    Returns:
    --------
    dict : {attribute: value}
    """
    # Skip target dan Temperature (tipe data double)
    attributes = [col for col in df.columns if col != target and col != 'Temperature of patient']
    sample = {}
    
    print("\n" + "="*100)
    print("INFLAMMATION PREDICTOR - INPUT PATIENT DATA")
    print("="*100)
    print("\nMasukkan nilai setiap atribut dengan 'y' atau 'n':\n")
    
    for i, attr in enumerate(attributes, 1):
        while True:
            user_input = input(f"{i}. {attr}: ").strip().lower()
            if user_input in ['y', 'n', 'yes', 'no']:
                # Normalize input
                value = 'yes' if user_input in ['y', 'yes'] else 'no'
                sample[attr] = value
                break
            else:
                print("   [ERROR] Masukkan 'y' atau 'n' saja!")
    
    return sample


def display_decision_path(path: list) -> None:
    """Display decision path yang dilalui."""
    print("\nDECISION PATH:")
    print("-" * 100)
    for step in path:
        print(step)
    print("-" * 100)


def main():
    print("\n" * 2)
    print("="*100)
    print("C4.5 DECISION TREE - INFLAMMATION PREDICTOR")
    print("="*100)
    
    # Load tree dan data
    print("\nLoading tree model...")
    try:
        tree = load_tree(TREE_JSON_PATH)
        print("[OK] Tree model loaded\n")
    except FileNotFoundError:
        print("[ERROR] Tree file not found. Please run 25_c45_tree_builder.py first.")
        return
    
    print("Loading dataset structure...")
    try:
        df = pd.read_csv(CSV_PATH)
        print(f"[OK] Dataset loaded (shape: {df.shape})\n")
    except FileNotFoundError:
        print("[ERROR] Dataset file not found.")
        return
    
    # Main loop
    while True:
        # Get user input
        sample = get_input_from_user(df, TARGET)
        
        # Make prediction
        print("\n" + "="*100)
        print("PROCESSING PREDICTION...")
        print("="*100)
        
        prediction, path = predict_single(tree, sample)
        
        # Display decision path
        display_decision_path(path)
        
        # Display result
        print("\n" + "="*100)
        print("PREDICTION RESULT")
        print("="*100)
        
        if prediction is None:
            print("\n[ERROR] Prediction failed!")
        else:
            # Format hasil
            diagnosis = "POSITIVE" if prediction == "yes" else "NEGATIVE"
            diagnosis_text = "Inflammation Detected" if prediction == "yes" else "No Inflammation"
            
            print(f"\nPrediction: {diagnosis}")
            print(f"Diagnosis: {diagnosis_text}")
            print(f"Target: {TARGET}")
            print(f"Confidence: Based on C4.5 Decision Tree Model")
        
        print("\n" + "="*100 + "\n")
        
        # Ask user if want to continue
        while True:
            continue_input = input("Ingin melakukan prediksi lagi? (y/n): ").strip().lower()
            if continue_input in ['y', 'n', 'yes', 'no']:
                break
            else:
                print("[ERROR] Masukkan 'y' atau 'n' saja!")
        
        if continue_input in ['n', 'no']:
            print("\n" + "="*100)
            print("Terima kasih telah menggunakan Inflammation Predictor!")
            print("="*100 + "\n")
            break


if __name__ == '__main__':
    main()
