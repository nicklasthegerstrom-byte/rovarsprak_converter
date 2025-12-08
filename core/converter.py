from core.language import is_vokal, is_konsonant

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

