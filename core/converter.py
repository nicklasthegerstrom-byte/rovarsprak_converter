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


def input_rovarsprak():
    text = input("Skriv något du vill konvertera till Rövarspråk:")
    resultat = to_rovarsprak(text)
    print(f"Rövarspråk: {resultat}")

