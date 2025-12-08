from core.converter import to_rovarsprak
from core.filehandler import list_input_files, read_file, write_file, make_output_filename
from config import OUTPUT_DIR
import re

def is_valid_filename(name: str) -> bool:
    return bool(re.match(r"^[A-Za-zÅÄÖåäö0-9_-]+$", name))

def yes_no(prompt: str):
    while True:
        question = input(prompt).strip().lower()
        if question == "j":
            return True
        elif question == "n":
            return False
        else:
            print("Jag behöver J eller N, baby!")

def save_file(resultat: str):
    if yes_no("Vill du spara resultatet till en text-fil? J/N:"):    
        while True:
            filename = input("Ange ett filnamn:").strip()
            if is_valid_filename(filename):               
                output_path = OUTPUT_DIR / f"{filename}.txt"
                write_file(output_path, resultat)
                print(f"Texten sparades som {output_path.name}")
                return
            else:
                print("Ogiltigt filnamn! Använd bara bokstäver, siffror, _ eller -.")
    else:
        return

def input_rovarsprak():
    while True:
        text = input("Skriv något du vill konvertera till Rövarspråk:")
        resultat = to_rovarsprak(text)
        print(f"Rövarspråk: {resultat}")

        save_file(resultat)

        if yes_no("Vill du konvertera något annat?"):
            continue
        else:
            return
        

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

def convert_file(selected_file):
            
    print("Du valde:", selected_file.name)

    text_from_file = read_file(selected_file)
    translated = to_rovarsprak(text_from_file)
    new_txt_path = make_output_filename(selected_file)
    write_file(new_txt_path, translated)

    print(f"\nDin fil är sparad som {new_txt_path.name}!")
   
    
def convert_from_file():
    while True:
        selected_file = select_file()

        # ❗ Måste hantera att select_file kan returnera None
        if selected_file is None:
            print("Ingen fil vald. Återgår till menyn.")
            return

        convert_file(selected_file)

        if yes_no("Vill du läsa in en till fil?"):
            continue
        else:
            break


def app():
    print("\nHej och Välkommen till Rövarspråkskonverteraren!")
    while True:
        print("1. Skriv in text du vill översätta.")
        print("2. Översätt från en text-fil.")
        print("3. Avsluta")

        val = input("Gör ditt val:")

        if val == "1":
            input_rovarsprak()
            print()
                   
        elif val == "2":
            convert_from_file()

        elif val == "3":
            break
        else:
            print("Fel val ditt popucockoko!")
        

    