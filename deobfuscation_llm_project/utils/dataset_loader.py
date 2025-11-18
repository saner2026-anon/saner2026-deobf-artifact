from pathlib import Path
from config import DATASET_PATH

def load_dataset():
    p = Path(DATASET_PATH)
    if not p.exists():
        raise FileNotFoundError(f"Dataset not found: {p}")
    return p.open("r", encoding="utf-8")
