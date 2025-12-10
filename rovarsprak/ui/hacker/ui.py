# Core-funktioner
from rovarsprak.core.converter import (
    to_rovarsprak,
    convert_file,
    translate_file
)
from rovarsprak.core.filehandler import (
    list_input_files,
    read_file,
    write_file,
    make_output_filename,
    make_decoded_output_filename
)
from rovarsprak.core.analyzer import analyze_text
from rovarsprak.core import hacker_mode   # endast ON/OFF state

# Konfiguration & logger
from rovarsprak.config import OUTPUT_DIR
from rovarsprak.utils.logger import logger

# Shared helpers (input, J/N, filval osv.)
from rovarsprak.shared.helpers import (
    save_file,
    yes_no,
    is_valid_filename,
    select_file
)


from rovarsprak.core.hacker_mode import toggle

# Hacker-specifika analyser
from rovarsprak.ui.hacker.analys import (
    print_converted_analys_hacker,
    print_translated_analys_hacker
)

# Hacker-animationer
from rovarsprak.ui.hacker.effects import hacker_logo_glitch, hacker_intro_animation, hacker_self_destruct, hacker_glitch_line

# Standardmoduler
import time
import re
import random

from rovarsprak.core.hacker_mode import color as hcol



# ===============================
# HACKER MENU
# ===============================

def show_hacker_menu():
    print()
    hacker_intro_animation()
    print()
    print("[1] DEPLOY ENCRYPTION PROTOCOL (USER INPUT)")
    print("[2] LOAD FILE → APPLY SCRAMBLER SEQUENCE")
    print("[3] REVERSE ENGINEER ENCRYPTED PAYLOAD")
    print("[4] EXECUTE MASS-ENCRYPTION SUBROUTINE")
    print("[5] INITIATE GLOBAL DECRYPTION WAVE")
    print("[6] DISABLE SYSTEM OVERCLOCKING (RETURN TO NOOB MODE)")
    print("[7] INITIATE SELF-DESTRUCT SEQUENCE (EXIT)")
    print()

#HACKER FUNCTIONS:
def hacker_input():
    while True:
        # Glitching input prompt
        glitch = "".join(random.choice("@#$%&*01") for _ in range(3))
        user_text = input(f"[{glitch}] ENTER DATA > ")

        time.sleep(0.2)
        print("\n> PROCESSING PAYLOAD...")
        time.sleep(0.4)

        encoded = to_rovarsprak(user_text)

        # Output with hacker flair
        print("\n> SCRAMBLER OUTPUT READY:")
        time.sleep(0.2)
        hacker_glitch_line()
        print(encoded)
        hacker_glitch_line()

        time.sleep(0.2)

        # Save option
        if yes_no("STORE OUTPUT TO ENCRYPTED FILE? (Y/N): "):
            save_file(encoded)

        print()
        if not yes_no("FEED MORE DATA INTO SCRAMBLER? (Y/N): "):
            print("\n> DISCONNECTING INPUT CHANNEL...\n")
            time.sleep(0.3)
            return
        
def select_file_hacker():
    print(hcol("\n> SCANNING DIRECTORY FOR PAYLOADS...\n"))
    time.sleep(0.3)

    # Glitch animation
    for _ in range(8):
        hacker_glitch_line(40)
        time.sleep(0.03)

    print(hcol("\n> DIRECTORY SCAN COMPLETE."))
    time.sleep(0.2)

    # Call normal selector to actually choose
    selected = select_file()

    # No file selected
    if selected is None:
        print(hcol("> NO FILE SELECTED — ABORTING OPERATION.\n"))
        time.sleep(0.3)
        return None

    print(hcol(f"\n> TARGET ACQUIRED: {selected.name}\n"))
    time.sleep(0.3)
    return selected


def hacker_encode_file():
    print(hcol("\n> INITIALIZING ENCRYPTION ROUTINE...\n"))
    time.sleep(0.3)

    selected = select_file_hacker()

    if selected is None:
        print(hcol("> ERROR: NO PAYLOAD SELECTED."))
        time.sleep(0.3)
        return

    print(hcol(f"> ACCESSING FILE: {selected.name}"))
    time.sleep(0.4)

    print(hcol("> DEPLOYING SCRAMBLER NANOBOTS..."))
    time.sleep(0.4)

    # Glitch animation
    for _ in range(6):
        line = "".join(random.choice("▌▒░▓█") for _ in range(30))
        print(hcol(line))
        time.sleep(0.05)

    # Perform actual conversion
    result = convert_file(selected)

    print(hcol("\n> ENCRYPTION COMPLETE. PAYLOAD TRANSFORMED.\n"))

    print_converted_analys_hacker(result)

    if yes_no(hcol("PROCESS ANOTHER FILE? (Y/N): ")):
        return hacker_encode_file()  
    else:
        print(hcol("\n> EXITING ENCRYPTION SUBSYSTEM..."))
        time.sleep(0.3)
        return
    
def hacker_decode_file():
    print(hcol("\n> INITIALIZING DECRYPTION ROUTINE...\n"))
    time.sleep(0.3)

    selected = select_file_hacker()

    if selected is None:
        print(hcol("> ERROR: NO ENCRYPTED PAYLOAD PROVIDED."))
        time.sleep(0.3)
        return

    print(hcol(f"> ACCESSING ENCRYPTED PAYLOAD: {selected.name}"))
    time.sleep(0.4)

    print(hcol("> SPINNING UP QUANTUM DE-SCRAMBLER..."))
    time.sleep(0.4)

    # Decrypt-style glitch animation (more structured, scanning-like)
    for _ in range(6):
        line = "".join(random.choice("█▓▒░▖▘▙▚") for _ in range(32))
        print(hcol(line))
        time.sleep(0.04)

    # Perform actual decryption
    result = translate_file(selected)

    print(hcol("\n> DECRYPTION SUCCESSFUL. PAYLOAD RESTORED.\n"))

    print_translated_analys_hacker(result)

    if yes_no(hcol("DECRYPT ANOTHER PAYLOAD? (Y/N): ")):
        return hacker_decode_file()
    else:
        print(hcol("\n> EXITING DECRYPTION SUBSYSTEM..."))
        time.sleep(0.3)
        return
        


# ===============================
# MAIN HACKER UI LOOP
# ===============================

def run_hacker_ui():
    """Startar hela hackermodet."""
    
    # glitch-intro
    hacker_logo_glitch()

    while True:
        show_hacker_menu()
        val = input("> ").strip()

        if val == "1":
            # Kommer implementeras senare
            hacker_input()

        elif val == "2":
            hacker_encode_file()

        elif val == "3":
            hacker_decode_file()

        elif val == "4":
            pass

        elif val == "5":
            pass

        elif val == "6":
            # Tillbaka till normal mode
            return

        elif val == "7":
            hacker_self_destruct() 
            

        else:
            print(hcol("INVALID INPUT. TRY AGAIN."))