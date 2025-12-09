from core.converter import to_rovarsprak, from_rovarsprak
from core.filehandler import list_input_files, read_file, write_file, make_output_filename, make_decoded_output_filename
from config import OUTPUT_DIR
import re, time
from utils.logger import logger
import time
from core.analyzer import analyze_text

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
                logger.info("User saved a txt-file.")
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

        if yes_no("Vill du konvertera något annat? J/N"):
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

    #räkna tiden konverteringen tar
    start = time.perf_counter()

    text_from_file = read_file(selected_file)
    converted = to_rovarsprak(text_from_file)
    new_txt_path = make_output_filename(selected_file)
    write_file(new_txt_path, converted)

    end = time.perf_counter()
    duration = end - start

    #Texanalys, före och efter konvertering:
    orig_stats = analyze_text(text_from_file)
    conv_stats = analyze_text(converted)

    print(f"\nDin fil är sparad som {new_txt_path.name}!")
    print()
    print("====== TEXTANALYS ======")
    print(f"Original: {orig_stats['length']} tecken")
    print(f"  → Vokaler: {orig_stats['vowels']}")
    print(f"  → Konsonanter: {orig_stats['consonants']}")

    print(f"\nKonverterad: {conv_stats['length']} tecken")
    print(f"  → Vokaler: {conv_stats['vowels']}")
    print(f"  → Konsonanter: {conv_stats['consonants']}")

    print(f"\nKonverteringstid: {duration:.5f} sekunder")
    print("=========================\n")

def translate_file(selected_file):
    print("Du valde:", selected_file.name)

    #Mäta tiden
    start = time.perf_counter()

    text_from_file = read_file(selected_file)
    translated = from_rovarsprak(text_from_file)
    new_txt_path = make_decoded_output_filename(selected_file)
    write_file(new_txt_path, translated)

    end = time.perf_counter()
    duration = end - start

    enc_stats = analyze_text(text_from_file)
    dec_stats = analyze_text(translated)

    print(f"\nDin fil är sparad som {new_txt_path.name}!")
    print()
    print("====== TEXTANALYS ======")
    print(f"Kodad text: {enc_stats['length']} tecken")
    print(f"  → Vokaler: {enc_stats['vowels']}")
    print(f"  → Konsonanter: {enc_stats['consonants']}")

    print(f"\nAvkodad text: {dec_stats['length']} tecken")
    print(f"  → Vokaler: {dec_stats['vowels']}")
    print(f"  → Konsonanter: {dec_stats['consonants']}")

    print(f"\nAvkodningstid: {duration:.5f} sekunder")
    print("=========================\n")

   
    
def convert_from_file():
    while True:
        selected_file = select_file()

        # ❗ Måste hantera att select_file kan returnera None
        if selected_file is None:
            print("Ingen fil vald. Återgår till menyn.")
            return

        convert_file(selected_file)
        logger.info("Text from file successfully converted.")

        if yes_no("Vill du läsa in en till fil? J/N"):
            continue
        else:
            break

def translate_from_file():
    while True:
        selected_file = select_file()

        # ❗ Måste hantera att select_file kan returnera None
        if selected_file is None:
            print("Ingen fil vald. Återgår till menyn.")
            return

        translate_file(selected_file)
        logger.info("Text from file successfully translated.")

        if yes_no("Vill du läsa in en till fil? J/N"):
            continue
        else:
            break

def batch_convert():
    while True:
        files = list_input_files()

        if not files:
            print("Inga filer att konvertera!")
            return

        print("Batch convert in process", end="", flush=True)

        for i in range(1, 6):
            time.sleep(0.5)
            print(f"\rBatch convert in process {'.' * i}", end="", flush=True)
            
        
        for file in files:
            convert_file(file)

        print("\nBatch klar!")
        logger.info("Batch converted succesfully.")

        if not yes_no("Vill du köra batch igen? J/N: "):
            return

def batch_translate():
    while True:
        files = list_input_files()

        if not files:
            print("Inga filer att konvertera!")
            return

        for i in range(1, 6):
            time.sleep(0.5)
            print(f"\rBatch convert in process {'.' * i}", end="", flush=True)
           

        for file in files:
            translate_file(file)

        print("\nBatch klar!")
        logger.info("Batch translated succesfully.")

        if not yes_no("Vill du köra batch igen? J/N: "):
            return
        
def analyze_file():
    while True:
        selected_file = select_file()

        if selected_file is None:
            print("Ingen fil vald. Återgår till menyn.")
            return

        text = read_file(selected_file)
        stats = analyze_text(text)

        print("\n====== TEXTANALYS ======")
        print(f"Textlängd: {stats['length']} tecken")
        print(f"  → Vokaler: {stats['vowels']}")
        print(f"  → Konsonanter: {stats['consonants']}")
        print("=========================\n")

        if not yes_no("Vill du analysera en annan fil? J/N: "):
            return



def app():
    print("\nHej och Välkommen till Rövarspråkskonverteraren!")
    while True:
        print("1. Skriv in text du vill konvertera till rövarspråk.")
        print("2. Konvertera till rövarspråk från en text-fil.")
        print("3. Översätt rövarspråk från en text-fil")
        print("4. Konvertera en batch txt-filer")
        print("5. Översätt en batch txt-filer")
        print("6. Analysera en text från fil" )
        print("7. Avsluta")

        val = input("Gör ditt val:")

        if val == "1":
            logger.info("User selected option 1: input_rovarsprak")
            input_rovarsprak()
            print()
                   
        elif val == "2":
            logger.info("User selected option 2: convert_from_file")
            convert_from_file()

        elif val == "3":
            logger.info("User selected option 3: translate_from_file")
            translate_from_file()

        elif val =="4":
            logger.info("User selected option 4: batch_convert")
            batch_convert()

        elif val =="5":
            logger.info("User selected option 5: batch_translate")
            batch_translate()

        elif val == "6":
            analyze_file()

        elif val =="7":
            logger.info("User selected option 6: quit program")
            break
        else:
            logger.warning("User made wrong meny choice")
            print("Fel val ditt popucockoko!")
        

    