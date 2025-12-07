from core.converter import to_rovarsprak
from core.filehandler import list_input_files, read_file, write_file, make_output_filename
from config import OUTPUT_DIR
import re

def is_valid_filename(name: str) -> bool:
    return bool(re.match(r"^[A-Za-zÅÄÖåäö0-9_-]+$", name))

def input_rovarsprak():
    text = input("Skriv något du vill konvertera till Rövarspråk:")
    resultat = to_rovarsprak(text)
    print(f"Rövarspråk: {resultat}")

    while True:
        save = input("Vill du spara resultatet till en fil? J/N: ").lower()
        if save == "j":
            while True:
                filename = input("Ange ett filnamn (utan .txt): ")
                if is_valid_filename(filename):
                    break
                print("Ogiltigt filnamn! Använd bara bokstäver, siffror, _ eller -.")
            output_path = OUTPUT_DIR / f"{filename}.txt"
            write_file(output_path, resultat)
            print(f"Texten sparades som {output_path.name}")
            break
        elif save == "n":
            break
        else:
            print("Skriv J eller N tack.")

def app():
    print("\nHej och Välkommen till Rövarspråkskonverteraren!")
    while True:
        print("1. Skriv in text du vill översätta.")
        print("2. Översätt från en text-fil.")
        print("3. Avsluta")

        val = input("Gör ditt val:")

        if val == "1":
            while True:
                input_rovarsprak()
                print()
                igen = input("En gång till kanske? J/N: ").lower()
                if igen == "j":
                    continue
                elif igen == "n":
                    break
                else:
                    print("J eller N, det är inte svårt!")
                    continue
                
        elif val == "2":
            files = list_input_files()
            if not files:
                print("No files in folder!")
                continue
            
            print("\nTillgängliga filer:")
            for i, file in enumerate(files, start=1):
                print(f"{i} - {file.name}")

            while True:
                choice = input("Välj filnummer: ")
                try:
                    choice = int(choice)
                except ValueError:
                    print("Du måste skriva ett nummer!")
                    continue
                if 1 <= choice <= len(files):
                    break
                print("Numret finns inte i listan, försök igen.")

            selected_file = files[choice - 1]
            print("Du valde:", selected_file.name)

            text_from_file = read_file(selected_file)
            translated = to_rovarsprak(text_from_file)

            new_txt_path = make_output_filename(selected_file)
            write_file(new_txt_path, translated)
            print(f"\nDin fil är sparad som {new_txt_path.name}!")

            igen = input("\nVill du börja om? J/N: ").lower()
            if igen == "j":
                continue
            else:
                print("Ha de gött!")
                break

        elif val == "3":
            break
        else:
            print("Fel val ditt popucockoko!")
        

    