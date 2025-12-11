# Core-funktioner
from rovarsprak.core.converter import (
    to_rovarsprak,
    convert_file,
    translate_file
)
from rovarsprak.core.filehandler import (
    list_input_files,
    list_output_files
)
from rovarsprak.core import hacker_mode   # endast ON/OFF state

# Konfiguration & logger
from rovarsprak.config import OUTPUT_DIR
from rovarsprak.utils.logger import logger

# Shared helpers (input, J/N, filval osv.)
from rovarsprak.shared.helpers import (
    save_file,
    select_file
)

from rovarsprak.core.hacker_mode import toggle

# Hacker-specifika analyser
from rovarsprak.ui.hacker.analys import (
    print_converted_analys_hacker,
    print_translated_analys_hacker
)

# Hacker-animationer
from rovarsprak.ui.hacker.effects import hacker_logo_glitch, hacker_intro_animation, self_destruct_animation, hacker_glitch_line

# Standardmoduler
import time
import random

from rovarsprak.core.hacker_mode import color as hcol



# ===============================
# HACKER MENU
# ===============================

def show_hacker_menu():

    print()
    print("[1] DEPLOY ENCRYPTION PROTOCOL (USER INPUT)")
    print("[2] LOAD FILE → APPLY SCRAMBLER SEQUENCE")
    print("[3] LOAD FILE → DECRYPT CHOSEN PAYLOAD")
    print("[4] EXECUTE MASS-ENCRYPTION SUBROUTINE")
    print("[5] INITIATE GLOBAL DECRYPTION WAVE")
    print("[6] DISABLE ULTRA HACKER MODE (RETURN TO NOOB MODE)")
    print("[7] INITIATE SELF-DESTRUCT SEQUENCE (EXIT)")
    print()

#HACKER FUNCTIONS:

def yes_no_hacker(prompt: str) -> bool:
    """
    Hacker-version av yes/no.
    Accepterar Y/N. Ger glitchiga felmeddelanden.
    """
    while True:
        ans = input(hcol(prompt)).strip().lower()

        if ans == "y":
            return True
        if ans == "n":
            return False

        # FEL – glitch error
        glitch = "".join(random.choice("▓░▞▚#/&@") for _ in range(12))
        print(hcol(f"!!! INVALID RESPONSE DETECTED: {glitch} !!!"))
        time.sleep(0.2)
        print(hcol("SYSTEM REQUIRES A 'Y' OR 'N' INPUT. RETRYING...\n"))
        time.sleep(0.2)

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
        if yes_no_hacker("STORE OUTPUT TO ENCRYPTED FILE? (Y/N): "):
            save_file(encoded)

        print()
        if not yes_no_hacker("FEED MORE DATA INTO EPIC MACHINE? (Y/N): "):
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

    if yes_no_hacker(hcol("PROCESS ANOTHER FILE? (Y/N): ")):
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

def hacker_batch_encode():
    print(hcol("\n> INITIALIZING MASS-ENCRYPTION SUBSYSTEM...\n"))
    time.sleep(0.5)

    files = list_input_files()
    if not files:
        print(hcol("> ERROR: NO PAYLOADS FOUND FOR MASS-PROCESSING.\n"))
        return

    print(hcol(f"> PAYLOADS DETECTED: {len(files)} FILES"))
    time.sleep(0.3)
    print(hcol("> ACTIVATING SCRAMBLER SWARM..."))
    time.sleep(0.4)

    # Animation: scanning through file list
    for f in files:
        glitch = "".join(random.choice("▓▒░█▚▞▟") for _ in range(25))
        print(hcol(f"[SCAN] {f.name:<20} {glitch}"))
        time.sleep(0.08)

    print(hcol("\n> MASS-ENCRYPTION IN PROGRESS...\n"))
    time.sleep(0.5)

    # Actual batch encode
    for f in files:
        print(hcol(f"> ENCRYPTING {f.name}..."))
        time.sleep(0.1)
        result = convert_file(f)
        print_converted_analys_hacker(result)
        time.sleep(0.15)

    print(hcol("\n> ALL PAYLOADS SUCCESSFULLY ENCRYPTED.\n"))
    time.sleep(0.4)
    print(hcol("> MASS-ENCRYPTION SUBSYSTEM STANDBY.\n"))

def hacker_batch_decode():
    print(hcol("\n> INITIALIZING GLOBAL DECRYPTION WAVE...\n"))
    time.sleep(0.5)

    files = [f for f in list_output_files() if f.name.endswith("_rovar.txt")]
    if not files:
        print(hcol("> ERROR: NO ENCRYPTED PAYLOADS DETECTED.\n"))
        return

    print(hcol(f"> TARGETS IDENTIFIED: {len(files)} FILES"))
    time.sleep(0.3)
    print(hcol("> SPINNING UP QUANTUM DE-SCRAMBLER ARRAY..."))
    time.sleep(0.4)

    for f in files:
        glitch = "".join(random.choice("▙▜▟▛░▒▓█") for _ in range(22))
        print(hcol(f"[DECRYPT-SCAN] {f.name:<20} {glitch}"))
        time.sleep(0.08)

    print(hcol("\n> INITIATING RESTORATION PROCESS...\n"))
    time.sleep(0.5)

    for f in files:
        print(hcol(f"> DECRYPTING {f.name}..."))
        time.sleep(0.1)
        result = translate_file(f)              # ← här ska f användas
        print_translated_analys_hacker(result)
        time.sleep(0.15)

    print(hcol("\n> GLOBAL DECRYPTION WAVE COMPLETE.\n"))
    time.sleep(0.4)
    print(hcol("> SYSTEM RETURNING TO IDLE MODE.\n"))
        


# ===============================
# MAIN HACKER UI LOOP
# ===============================

def run_hacker_ui():
    """Startar hela hackermodet."""

    # glitch-intro
    hacker_logo_glitch()
    hacker_intro_animation()
    time.sleep(0.3)
    print()  

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
            hacker_batch_encode()

        elif val == "5":
            hacker_batch_decode()

        elif val == "6":
            # Tillbaka till normal mode
            toggle()
            print("FAREWELL NOOB!")
            return

        elif val == "7":
            self_destruct_animation() 
            

        else:
            print(hcol("INVALID INPUT. TRY AGAIN."))