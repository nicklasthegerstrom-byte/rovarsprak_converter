from rovarsprak.config import INPUT_DIR, OUTPUT_DIR
from pathlib import Path

def read_file(path: Path) -> str:
    return path.read_text(encoding="utf-8")

def write_file(path: Path, text: str):
    path.write_text(text, encoding="utf-8")

def make_output_filename(input_path: Path) -> Path:
    new_name = input_path.stem + "_rovar" + input_path.suffix
    return OUTPUT_DIR / new_name

def make_decoded_output_filename(input_path: Path) -> Path:
    new_name = input_path.stem + "_decoded" + input_path.suffix
    return OUTPUT_DIR / new_name

def list_input_files() -> list[Path]:
    """Returnerar en lista med alla .txt-filer i input-mappen."""
    return list(INPUT_DIR.glob("*.txt"))

def list_output_files():
    """Returnerar en lista med alla .txt-filer i output-mappen."""
    return list(OUTPUT_DIR.glob("*.txt"))
