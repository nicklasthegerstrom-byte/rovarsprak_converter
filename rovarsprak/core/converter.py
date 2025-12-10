from rovarsprak.core.language import is_vokal, is_konsonant
from rovarsprak.core.filehandler import (
    read_file,
    write_file,
    make_output_filename,
    make_decoded_output_filename
)
from rovarsprak.core.analyzer import analyze_text
import time

def to_rovarsprak(text: str) -> str:
    rovarsprak = ""
    for t in text:
        if is_konsonant(t):
            rovarsprak += t + "o" + t
        elif is_vokal(t):
            rovarsprak += t
        else:
            rovarsprak += t
    return rovarsprak

def from_rovarsprak(text: str) -> str:
    result = ""
    i = 0

    while i < len(text):

        # Kontrollera om vi har ett rövarspråksblock
        if (
            i + 2 < len(text)
            and is_konsonant(text[i])
            and text[i+1] == "o"
            and text[i+2] == text[i]
        ):
            result += text[i]
            i += 3
        else:
            result += text[i]
            i += 1

    return result

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
    
    orig_stats = analyze_text(text_from_file)
    conv_stats = analyze_text(converted)

    return {
        "file": selected_file,
        "converted": converted,
        "duration": duration,
        "orig_stats": orig_stats,
        "conv_stats": conv_stats,
        "new_txt_path": new_txt_path
    }

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

    return {
        "file": selected_file,
        "decoded": translated,
        "duration": duration,
        "enc_stats": enc_stats,
        "dec_stats": dec_stats,
        "new_txt_path": new_txt_path
    }
