import re
from pathlib import Path
from rovarsprak.config import OUTPUT_DIR
from core.filehandler import write_file

def is_valid_filename(name: str) -> bool:
    """Validerar att ett filnamn bara innehåller tillåtna tecken."""
    return bool(re.match(r"^[A-Za-zÅÄÖåäö0-9_-]+$", name))


def yes_no(prompt: str) -> bool:
    """Ställer en Ja/Ni-fråga till användaren och returnerar True/False."""
    while True:
        answer = input(prompt).strip().lower()
        if answer == "j":
            return True
        elif answer == "n":
            return False
        else:
            print("Jag behöver ett J eller N, vännen!")


def save_file(result: str):
    """Fråga användaren om filen ska sparas och hantera filnamn."""
    if not yes_no("Vill du spara resultatet till en text-fil? J/N: "):
        return None

    while True:
        filename = input("Ange ett filnamn: ").strip()
        if is_valid_filename(filename):
            output_path = OUTPUT_DIR / f"{filename}.txt"
            write_file(output_path, result)
            print(f"Texten sparades som {output_path.name}")
            return output_path
        else:
            print("Ogiltigt filnamn! Använd bara bokstäver, siffror, _ eller -.") 


def select_file():

    files = list_input_files()
    if not files:
        print("Måste tyvärr meddela att det inte finns några filer i din lilla lilla mapp. :(")
        return None

    print("\nTillgängliga filer:")
    for i, file in enumerate(files, start=1):
        print(f"{i} - {file.name}")

    while True:
        choice = input("Välj filnummer: ").strip()
        try:
            num = int(choice)    
        except ValueError:
            print("Du måste skriva ett nummer!")
            continue
        if 1 <= num <= len(files):
            return files[num - 1]
        else:
            print("Filen finns inte i listan!")