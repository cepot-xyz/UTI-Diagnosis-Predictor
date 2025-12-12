import json
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import pandas as pd

# Konfigurasi
TREE_JSON_PATH = r'gen_c45_tree.json'
CSV_PATH = r'UTI.csv'
TARGET = 'Inflammation of urinary bladder'


def load_tree(filepath: str) -> dict:
    """Load tree dari JSON file."""
    with open(filepath, 'r') as f:
        return json.load(f)


class TreeVisualizer:
    """Visualisasi decision tree menggunakan matplotlib."""
    
    def __init__(self, tree: dict):
        self.tree = tree
        self.fig = None
        self.ax = None
        self.node_positions = {}
        self.node_counter = 0
        
    def calculate_positions(self, node: dict, x: float = 0, y: float = 0, layer_width: float = 2) -> None:
        """Calculate positions untuk setiap node."""
        node_id = self.node_counter
        self.node_counter += 1
        self.node_positions[node_id] = (x, y)
        
        if node['type'] == 'leaf':
            return
        
        # Calculate child positions
        num_children = len(node['children'])
        child_x_offset = layer_width / (num_children + 1) if num_children > 0 else 0
        child_y = y - 1.5
        
        for i, (branch_value, child) in enumerate(node['children'].items()):
            child_x = x - layer_width / 2 + (i + 1) * child_x_offset
            self.calculate_positions(child, child_x, child_y, layer_width / 2)
    
    def draw_node(self, node_id: int, node: dict, parent_id: int = None, 
                  branch_value: str = "") -> int:
        """Draw single node dan connectionnya."""
        x, y = self.node_positions[node_id]
        
        if node['type'] == 'leaf':
            # Leaf node - warna hijau
            color = 'lightgreen'
            edgecolor = 'darkgreen'
            label = f"{node['value']}\n(n={node['samples']})"
        else:
            # Internal node - warna biru
            color = 'lightblue'
            edgecolor = 'darkblue'
            attr_short = node['attribute'][:30]  # Shorten long names
            label = f"{attr_short}\nGR: {node['gain_ratio']:.3f}\n(n={node['samples']})"
        
        # Draw box
        bbox = FancyBboxPatch(
            (x - 0.4, y - 0.3), 0.8, 0.6,
            boxstyle="round,pad=0.05",
            edgecolor=edgecolor,
            facecolor=color,
            linewidth=2
        )
        self.ax.add_patch(bbox)
        
        # Draw text
        self.ax.text(x, y, label, ha='center', va='center', fontsize=8, weight='bold')
        
        # Draw edge dari parent
        if parent_id is not None:
            parent_x, parent_y = self.node_positions[parent_id]
            arrow = FancyArrowPatch(
                (parent_x, parent_y - 0.35),
                (x, y + 0.3),
                arrowstyle='-|>',
                mutation_scale=15,
                linewidth=1.5,
                color='gray'
            )
            self.ax.add_patch(arrow)
            
            # Draw branch label
            mid_x = (parent_x + x) / 2
            mid_y = (parent_y + y) / 2
            self.ax.text(mid_x + 0.15, mid_y, f"= {branch_value}", 
                        fontsize=7, style='italic', color='darkred')
        
        # Draw child nodes
        if node['type'] == 'internal':
            next_node_id = node_id + 1
            for branch_value, child in node['children'].items():
                next_node_id = self.draw_node(next_node_id, child, node_id, branch_value)
            return next_node_id
        
        return node_id + 1
    
    def visualize(self, figsize=(16, 10), save_path: str = "gen_uti_tree.png"):
        """Generate dan save visualization."""
        self.node_counter = 0
        self.calculate_positions(self.tree)
        
        self.fig, self.ax = plt.subplots(figsize=figsize)
        self.ax.set_xlim(-5, 5)
        self.ax.set_ylim(-4, 1)
        self.ax.axis('off')
        
        # Draw tree
        self.node_counter = 0
        self.draw_node(0, self.tree)
        
        # Add title
        self.fig.suptitle('C4.5 Decision Tree - UTI Inflammation Predictor', 
                         fontsize=16, weight='bold', y=0.98)
        
        # Add legend
        leaf_patch = mpatches.Patch(color='lightgreen', label='Leaf Node (Prediction)')
        internal_patch = mpatches.Patch(color='lightblue', label='Internal Node (Decision)')
        self.ax.legend(handles=[internal_patch, leaf_patch], loc='upper right', fontsize=10)
        
        # Save
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"[OK] Tree visualization saved to: {save_path}")
        plt.close()


def create_summary_report(tree: dict, df: pd.DataFrame, target: str):
    """Create summary report tentang tree."""
    
    def count_nodes(n):
        if n['type'] == 'leaf':
            return (0, 1)
        internal, leaf = 0, 0
        for child in n['children'].values():
            ci, cl = count_nodes(child)
            internal += ci
            leaf += cl
        return (internal + 1, leaf)
    
    def get_depth(n):
        if n['type'] == 'leaf':
            return 0
        return 1 + max((get_depth(child) for child in n['children'].values()), default=0)
    
    internal, leaf = count_nodes(tree)
    depth = get_depth(tree)
    
    report = f"""
{'='*100}
C4.5 DECISION TREE - FINAL REPORT
{'='*100}

TREE STATISTICS:
  * Total Nodes: {internal + leaf}
  * Internal Nodes (Decision): {internal}
  * Leaf Nodes (Prediction): {leaf}
  * Tree Depth: {depth}

DATASET INFORMATION:
  * Total Samples: {len(df)}
  * Target Variable: {target}
  * Class Distribution:
"""
    
    for target_val, count in df[target].value_counts().items():
        pct = count / len(df) * 100
        report += f"    - {target_val}: {count} ({pct:.2f}%)\n"
    
    report += f"""
ROOT NODE (Best Split):
  * Splitting Attribute: {tree['attribute']}
  * Gain Ratio: {tree['gain_ratio']:.6f}
  * Samples: {tree['samples']}
  * Number of Branches: {len(tree['children'])}

INTERPRETATION:
  The model identified "{tree['attribute']}" as the most important
  feature for predicting Inflammation diagnosis. This attribute
  provides the highest information gain ratio among all features.

OUTPUT FILES GENERATED:
  [OK] gen_c45_tree.json - Tree structure in JSON format
  [OK] gen_uti_tree.png - Tree visualization (high-res)
  [OK] gen_tree_summary.txt - This summary report

{'='*100}
"""
    
    return report


def main():
    print("="*100)
    print("TREE VISUALIZATION WITH MATPLOTLIB")
    print("="*100 + "\n")
    
    # Load tree and data
    print("Loading tree...")
    tree = load_tree(TREE_JSON_PATH)
    print("[OK] Tree loaded\n")
    
    print("Loading dataset...")
    df = pd.read_csv(CSV_PATH)
    print("[OK] Dataset loaded\n")
    
    # Create visualizations
    print("Generating tree visualization...")
    visualizer = TreeVisualizer(tree)
    visualizer.visualize(figsize=(16, 10), save_path="gen_uti_tree.png")
    print()
    
    # Generate summary report
    print("Generating summary report...")
    report = create_summary_report(tree, df, TARGET)
    print(report)
    
    # Save report with UTF-8 encoding
    with open("gen_tree_summary.txt", "w", encoding='utf-8') as f:
        f.write(report)
    print("[OK] Summary report saved to: gen_tree_summary.txt\n")
    
    print("="*100)
    print("[OK] DOKUMENTASI LENGKAP - SELESAI!")
    print("="*100 + "\n")


if __name__ == '__main__':
    main()
