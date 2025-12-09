# Rövarspråkskonverterare

Ett Python-projekt som kan:

- konvertera text till Rövarspråk
- översätta tillbaka från Rövarspråk
- konvertera enskilda filer
- batch-konvertera flera filer
- analysera text
- logga alla händelser till en loggfil

Projektet är uppbyggt med en ren modulstruktur och använder `pathlib` och `logging`
för filhantering och loggning. Ingen extern dependency krävs.

---

## Installation

1. Klona projektet:
   git clone <repo>

2. Gå in i projektet:
   cd rovarsprak_converter

3. (valfritt) Skapa ett virtuellt environment:
   python3 -m venv venv
   source venv/bin/activate

4. Installera projektet i utvecklingsläge:
   pip install -e .

---

## Kör programmet

### Alternativ 1: Via Python-modul
python -m rovarsprak

### Alternativ 2: Via installerat CLI-kommando
rovar

---

## Projektstruktur

rovarsprak/
│
├── __init__.py
├── main.py
├── ui.py
├── config.py
│
├── core/
│   ├── converter.py
│   ├── filehandler.py
│   ├── language.py
│
├── utils/
│   └── logger.py
│
└── data/
    ├── input/
    └── output/

---

## Loggning

Alla loggar sparas i:
`rovarsprak/logs/rovarsprak.log`

Loggning används för att spåra:

- menyval
- filoperationer
- fel
- batchprocesser

---

## Batch-konvertering

Programmet kan automatiskt konvertera alla `.txt`-filer i `data/input/` och spara resultatet i `data/output/`.

---

## Textanalys

Projektet innehåller en enkel textanalysmodul som kan:

- räkna ord
- räkna vokaler / konsonanter
- hitta längsta ordet
- analysera längd och tecken

---

## Krav

Python 3.11 eller senare.

Inga externa dependencies krävs.