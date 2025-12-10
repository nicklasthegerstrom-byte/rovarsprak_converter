from rovarsprak.core.language import is_vokal, is_konsonant

def analyze_text(text: str) -> dict:
    vowels = 0
    consonants = 0

    for ch in text:
        if is_vokal(ch):
            vowels += 1
        elif is_konsonant(ch):
            consonants += 1

    return {
        "length": len(text),
        "vowels": vowels,
        "consonants": consonants,
    }