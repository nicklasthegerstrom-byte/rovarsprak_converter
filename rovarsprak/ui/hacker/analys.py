import time
import random
from rovarsprak.core.hacker_mode import color as hcol


# ==========================================================
# Helper animations
# ==========================================================

def _glitch_block(lines=12, width=40, speed=0.02):
    for _ in range(lines):
        glitch = "".join(random.choice("█▓▒░▚▞▘▙▖#%@") for _ in range(width))
        print(hcol(glitch))
        time.sleep(speed)

def _stat(label, value):
    print(hcol(f"   {label:<20} {value}"))


def _ascii_bar(value, max_val=100, width=25):
    """Sjuk enkel ASCII-bar för effekter."""
    ratio = min(value / max_val, 1.0)
    filled = int(ratio * width)
    return "[" + "█" * filled + " " * (width - filled) + "]"


def _fake_warning():
    warnings = [
        "⚠ PACKET LOSS DETECTED IN SECTOR 7G...",
        "⚠ ENTROPY SPIKE DETECTED...",
        "⚠ UNIDENTIFIED DATA SIGNATURE FOUND...",
        "⚠ BUFFER OVERFLOW IN NODE ∆42...",
        "⚠ HEURISTIC FILTER DESYNCHRONIZED...",
    ]
    print(hcol(random.choice(warnings)))
    time.sleep(0.2)


def _fake_hex_signature():
    sig = "".join(random.choice("0123456789ABCDEF") for _ in range(32))
    print(hcol(f"   SIGNATURE: {sig}"))


def _entropy_prediction(stats):
    """Lite fejk ML-prediktion baserat på textens proportioner."""
    vowels = stats["vowels"]
    cons = stats["consonants"]
    total = stats["total_chars"]
    if total == 0:
        return 0

    ratio = (cons / total) * 100
    prediction = int(min(max(ratio * 1.3, 2), 98))
    return prediction


# ==========================================================
# Conversion Analysis (Encode)
# ==========================================================

def print_converted_analys_hacker(result: dict):
    print(hcol("\n> INITIATING ADVANCED POST-PROCESS ANALYSIS...\n"))
    _glitch_block(6, 35)

    file = result["file"].name
    out = result["new_txt_path"].name
    dur = f"{result['duration']:.4f}s"

    orig = result["orig_stats"]
    conv = result["conv_stats"]

    # ----------------------------
    print(hcol("> PAYLOAD METADATA:"))
    _stat("INPUT FILE........", file)
    _stat("OUTPUT FILE.......", out)
    _stat("PROCESS TIME......", dur)

    _fake_hex_signature()
    print()

    # ----------------------------
    print(hcol("> CHARACTER TRANSFORMATION REPORT:"))
    _stat("INPUT LENGTH......", orig["total_chars"])
    _stat("OUTPUT LENGTH.....", conv["total_chars"])
    _stat("VOCALS............", conv["vowels"])
    _stat("CONSONANTS........", conv["consonants"])
    _stat("SYMBOLS...........", conv["symbols"])
    print()

    # ----------------------------
    print(hcol("> ENTROPY INDEX ESTIMATION (ML MODE):"))
    entropy = _entropy_prediction(conv)
    print(hcol(f"   PREDICTED ENCRYPTION ENTROPY: {entropy}%"))
    print(hcol("   " + _ascii_bar(entropy, max_val=100)))
    print()

    # ----------------------------
    print(hcol("> PERFORMING ANOMALY SCAN..."))
    _glitch_block(5, 30, speed=0.015)
    if random.random() < 0.25:
        _fake_warning()
        _fake_warning()
        print(hcol("   → AUTO-CORRECTION APPLIED.\n"))
    else:
        print(hcol("   → NO ANOMALIES DETECTED.\n"))

    time.sleep(0.2)


# ==========================================================
# Decryption Analysis (Decode)
# ==========================================================

def print_translated_analys_hacker(result: dict):
    print(hcol("\n> INITIATING DECRYPTION INTEGRITY VERIFICATION...\n"))
    _glitch_block(7, 40, speed=0.018)

    file = result["file"].name
    out = result["new_txt_path"].name
    dur = f"{result['duration']:.4f}s"

    enc = result["enc_stats"]
    dec = result["dec_stats"]

    # ----------------------------
    print(hcol("> PAYLOAD METADATA:"))
    _stat("ENCRYPTED FILE....", file)
    _stat("OUTPUT FILE.......", out)
    _stat("PROCESS TIME......", dur)
    _fake_hex_signature()
    print()

    # ----------------------------
    print(hcol("> TEXT RESTORATION REPORT:"))
    _stat("ENC LENGTH........", enc["total_chars"])
    _stat("DEC LENGTH........", dec["total_chars"])
    _stat("VOCALS............", dec["vowels"])
    _stat("CONSONANTS........", dec["consonants"])
    _stat("SYMBOLS...........", dec["symbols"])
    print()

    # ----------------------------
    print(hcol("> SIGNAL CONSISTENCY CHECK:"))
    stability = random.randint(72, 99)
    print(hcol(f"   SIGNAL STABILITY: {stability}%"))
    print(hcol("   " + _ascii_bar(stability)))
    print()

    # ----------------------------
    print(hcol("> RUNNING QUANTUM NOISE SCAN..."))
    _glitch_block(4, 32, speed=0.012)
    if stability < 80:
        _fake_warning()
        print(hcol("   → MANUAL INTERVENTION REQUIRED — BUT AUTO-PATCH APPLIED.\n"))
    else:
        print(hcol("   → SIGNAL VERIFIED. DECRYPTION SUCCESSFUL.\n"))

    time.sleep(0.2)