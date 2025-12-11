import time
import sys
import random
from rovarsprak.core.hacker_mode import color as hcol

def hacker_intro_animation():
    text = ">>> CALIBRATING LASER KEYS… READY <<<"
    for char in text:
        print(hcol(char), end="", flush=True)
        time.sleep(0.03)
    print()
    time.sleep(0.2)


GLITCH_CHARS = ["#", "%", "&", "@", "$", "∑", "Ø", "Ψ", "¤", "§", "?", "!", "╳"]

def hacker_logo_glitch():
    logo = "RÖVARSPRÅKCONVERTER 5000 INITIALIZING"
    build = [" "] * len(logo)

    # Glitch-faser
    for _ in range(12):
        glitch_output = ""

        for i in range(len(logo)):
            if random.random() < 0.3:
                build[i] = logo[i]
            else:
                build[i] = random.choice(GLITCH_CHARS)

            glitch_output += build[i]

        sys.stdout.write("\r" + hcol(glitch_output))
        sys.stdout.flush()
        time.sleep(0.07)

    # Rensa rad
    sys.stdout.write("\r")
    sys.stdout.flush()

    # Skriv upp byggd text långsamt
    final_text = ""
    for char in logo:
        final_text += char
        sys.stdout.write(hcol("\r" + final_text))
        sys.stdout.flush()
        time.sleep(0.03)

    print(hcol(" ✓"))
    time.sleep(0.3)

def hacker_glitch_line(width: int = 40, delay: float = 0.0):
    """Printar en rad glitchig text i hacker-stil."""
    line = "".join(random.choice("▒▓█░#%@$&Ø*") for _ in range(width))
    print(line)
    if delay > 0:
        time.sleep(delay)

def hacker_self_destruct():
    steps = [
        "ARMING FAILSAFE PROTOCOLS",
        "REVERSING POLARITY COILS",
        "PURGING RÖVARSPRÅK RAM RESIDUE",
        "IGNITING THERMO-CORE",
        "DISENGAGING SAFETY LIMITERS",
        "SELF-DESTRUCT READY"
    ]

    # Dramatic startup sequence
    for step in steps:
        line = hcol(f">>> {step}...")
        print(line)
        time.sleep(0.4)

    print()
    print(hcol("   *** SELF-DESTRUCT SEQUENCE INITIATED ***"))
    time.sleep(0.5)
    print()

    # Countdown with glitch
    for i in range(5, 0, -1):
        scrambled = "".join(random.choice(GLITCH_CHARS) for _ in range(12))
        sys.stdout.write(
            color(f"\rT-{i}   SYSTEM FRAGMENTATION: {scrambled}")
        )
        sys.stdout.flush()
        time.sleep(0.7)

    print(hcol("\n\n🔥 CORE OVERLOAD COMPLETE 🔥"))
    time.sleep(0.3)
    print(hcol(">> SHUTTING DOWN SYSTEM CHANNELS..."))
    time.sleep(0.3)
    print(hcol(">> CONNECTION TERMINATED"))
    time.sleep(0.2)
    print()


def self_destruct_animation():
    intro = [
        "SYSTEMET INITIERAR SJÄLVDESTRUKTION...",
        "SOSySStotomomemometot INONitotiotieroraror SOSjjojälolvvododesostrotororukoktotionon..."
    ]

    for s in intro:
        print(s)
        time.sleep(0.9)

    steps = [
        "⚠ BYPASSING SAFETY PROTOCOLS...",
        "⚠ DISABLING FIREWALLS...",
        "⚠ OVERCLOCKING CORE SYSTEMS...",
        "⚠ COMPILING EXPLOSION MODULES...",
        "⚠ ARMING THERMONUCLEAR PAYLOAD...",
        "⚠ FINAL LOCK ENGAGED.",
    ]

    print()
    for s in steps:
        print(s)
        time.sleep(0.55)

    print("\nCOMMENCING COUNTDOWN...\n")
    time.sleep(0.4)

    for i in range(5, 0, -1):
        print(f"{i}...")
        time.sleep(0.5)

    print("\nSYSTEM OVERLOAD DETECTED...\n")
    time.sleep(0.4)

    # Glitch-storm (ren kaos)
    for _ in range(25):
        line = "".join(random.choice("▒▓█░#%@$&Ø*") for _ in range(random.randint(40, 70)))
        print(line)
        time.sleep(0.03)

    # Enkel, tydlig BOOM – utan ASCII-font
    time.sleep(0.3)
    print()
    print("***************")
    print("***  BOOM!  ***")
    print("***************")
    time.sleep(1.0)

    print("\n>>> SYSTEM TERMINATED <<<")
    time.sleep(0.4)

    sys.exit(0)