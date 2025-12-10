from rovarsprak.core.converter import to_rovarsprak, translate_file, convert_file
from rovarsprak.core.filehandler import (
    list_input_files,
    read_file,
    write_file,
    make_output_filename,
    make_decoded_output_filename
)
from rovarsprak.config import OUTPUT_DIR
from rovarsprak.utils.logger import logger

from rovarsprak.ui.normal.analys import (
    print_converted_analys_normal,
    print_translated_analys_normal
)

from rovarsprak.shared.helpers import (
    save_file,
    yes_no,
    is_valid_filename,
    select_file
)

from rovarsprak.ui.normal.menu_colors import (
    color,
    N_YELLOW,
    N_MAGENTA,
    N_RED,
    N_CYAN,
    N_RESET
)

from rovarsprak.core import hacker_mode
import re, time
from rovarsprak.ui.hacker.ui import run_hacker_ui


def color(text: str, code: str) -> str:
    """Returnera text inlindad i en färgkod."""
    return f"{code}{text}{N_RESET}"

def print_logo():
    print(color("=" * 40, N_CYAN))
    print(color("   RÖVARSPRÅKS-KONVERTERAREN 3000", N_CYAN))
    print(color("=" * 40, N_CYAN))


def show_menu():
    print()
    print(color("Välj ett alternativ:", N_MAGENTA))
    print()
    print(color("1.", N_YELLOW), "Skriv in text du vill konvertera till rövarspråk.")
    print(color("2.", N_YELLOW), "Konvertera till rövarspråk från en text-fil.")
    print(color("3.", N_YELLOW), "Översätt rövarspråk från en text-fil.")
    print(color("4.", N_YELLOW), "Konvertera en batch txt-filer.")
    print(color("5.", N_YELLOW), "Översätt en batch txt-filer.")
    print(color("6.", N_YELLOW), "ULTRA HACKER MODE ON/OFF")
    print(color("7.", N_RED),    "Avsluta")
    print()

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
    
def convert_from_file():
    while True:
        selected_file = select_file()

        if selected_file is None:
            print("Ingen fil vald. Återgår till menyn.")
            return

        # Kör en konvertering
        result = convert_file(selected_file)

        # Visa analys
        print_converted_analys_normal(result)

        logger.info("Text from file successfully converted.")

        if not yes_no("Vill du läsa in en till fil? J/N"):
            return

def translate_from_file():
    while True:
        selected_file = select_file()

        # ❗ Måste hantera att select_file kan returnera None
        if selected_file is None:
            print("Ingen fil vald. Återgår till menyn.")
            return

        result = translate_file(selected_file)
        print_translated_analys_normal(result)

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
        


def run_normal_ui():
    print_logo()

    while True:
        print()
        show_menu()
            
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
            logger.info("BADASS USER ACTIVATED ULTRA HACKER MODE")
            if hacker_mode.toggle():
                print(hacker_mode.color("ULTRA HACKER MODE AKTIVERAT"))
                run_hacker_ui()   # ← THIS IS THE IMPORTANT PART
            else:
                print("ULTRA HACKER MODE AVSTÄNGT")

        elif val =="7":
            logger.info("User selected option 7: quit program")
            print("Hejdå gogulollolisos!")
            return "EXIT"
        else:
            logger.warning("User made wrong meny choice")
            print("Fel val ditt popucockoko!")
        

    