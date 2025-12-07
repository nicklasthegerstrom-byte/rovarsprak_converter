from pathlib import Path

# Hitta projektets root (där config.py ligger)
BASE_DIR = Path(__file__).resolve().parent

# Data-directory
DATA_DIR = BASE_DIR / "data"

# Input och Output directories
INPUT_DIR = DATA_DIR / "input"
OUTPUT_DIR = DATA_DIR / "output"

# Skapa mapparna om de inte finns
INPUT_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
