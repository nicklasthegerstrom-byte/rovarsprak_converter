from rovarsprak.core.hacker_mode import color as hcol
import time
import random


def print_converted_analys_hacker(result: dict):
    orig = result["orig_stats"]
    conv = result["conv_stats"]
    duration = result["duration"]
    newfile = result["new_txt_path"]

    print(hcol("\n> INITIATING POST-ENCRYPTION DIAGNOSTICS...\n"))
    time.sleep(0.3)

    # Liten glitch-intro
    for _ in range(5):
        line = "".join(random.choice("█▓▒░▖▘▙▚#@%") for _ in range(40))
        print(hcol(line))
        time.sleep(0.04)

    print(hcol("\n> ENCRYPTED PAYLOAD STORED AS: ") + f"{newfile.name}\n")
    time.sleep(0.2)

    print(hcol("=== CHARACTER TRANSFORMATION REPORT ==="))
    time.sleep(0.1)
    print(hcol(f"• ORIGINAL LENGTH..... {orig['length']} chars"))
    print(hcol(f"• ORIGINAL VOWELS..... {orig['vowels']}"))
    print(hcol(f"• ORIGINAL CONSONANTS. {orig['consonants']}"))
    time.sleep(0.1)
    print()
    print(hcol(f"• ENCRYPTED LENGTH.... {conv['length']} chars"))
    print(hcol(f"• ENCRYPTED VOWELS.... {conv['vowels']}"))
    print(hcol(f"• ENCRYPTED CONSONANTS {conv['consonants']}"))
    time.sleep(0.1)

    print(hcol("\n• PROCESSING TIME...... ") + f"{duration:.5f} seconds")
    print(hcol("=======================================\n"))
    time.sleep(0.2)


def print_translated_analys_hacker(result: dict):
    enc = result["enc_stats"]
    dec = result["dec_stats"]
    duration = result["duration"]
    newfile = result["new_txt_path"]

    print(hcol("\n> INITIATING DECRYPTION DIAGNOSTICS...\n"))
    time.sleep(0.3)

    for _ in range(5):
        line = "".join(random.choice("▓▒░▌▚▞▟▙#") for _ in range(40))
        print(hcol(line))
        time.sleep(0.04)

    print(hcol("\n> RESTORED PAYLOAD SAVED AS: ") + f"{newfile.name}\n")
    time.sleep(0.2)

    print(hcol("=== CHARACTER RESTORATION REPORT ==="))
    time.sleep(0.1)
    print(hcol(f"• ENCODED LENGTH...... {enc['length']} chars"))
    print(hcol(f"• ENCODED VOWELS...... {enc['vowels']}"))
    print(hcol(f"• ENCODED CONSONANTS.. {enc['consonants']}"))
    print()
    print(hcol(f"• DECODED LENGTH...... {dec['length']} chars"))
    print(hcol(f"• DECODED VOWELS...... {dec['vowels']}"))
    print(hcol(f"• DECODED CONSONANTS.. {dec['consonants']}"))
    time.sleep(0.1)

    print(hcol("\n• PROCESSING TIME...... ") + f"{duration:.5f} seconds")
    print(hcol("=====================================\n"))
    time.sleep(0.2)