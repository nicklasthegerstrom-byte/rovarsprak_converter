from pathlib import Path

def print_converted_analys_normal(result: dict):
    
    orig_stats = result["orig_stats"]
    conv_stats = result["conv_stats"]
    duration = result["duration"]
    file = result["file"]
    new_txt_path = result["new_txt_path"]

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

def print_translated_analys_normal(result: dict):

    enc_stats = result["enc_stats"]
    dec_stats = result["dec_stats"]
    duration = result["duration"]
    file = result["file"]
    new_txt_path = result["new_txt_path"]

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