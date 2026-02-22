# Rövarspråkskonverterare 3000

Ett modulärt Python-CLI som konverterar text till och från Rövarspråk.

Projektet är uppbyggt med tydlig separation mellan **core-logik** och **presentation (UI)**.  
Samma motor driver både ett normalt läge och ett alternativt *Ultra Hacker Mode*.

---

## Funktioner

- Konvertera text till Rövarspråk
- Översätta från Rövarspråk
- Konvertera enskilda textfiler
- Batch-konvertera flera filer
- Enkel textanalys (ord, vokaler, konsonanter, längd m.m.)
- Loggning av alla operationer

---

## Ultra Hacker Mode

Alternativt UI med glitch-animationer, terminaleffekter och tematiserad meny.

Detta är ett separat presentationslager som använder samma core-funktioner som normal-läget.  
Ingen duplicerad affärslogik — endast annorlunda rendering.

---

## Arkitektur

```
rovarsprak/
│
├── core/           # Konverteringslogik och filhantering
├── ui/             # Normal UI och Hacker UI
├── shared/         # Hjälpfunktioner
├── utils/          # Logger
├── config.py
└── data/
    ├── input/
    └── output/
```

Designprinciper:
- Separation mellan logik och UI
- Ingen extern dependency
- pathlib för filhantering
- logging för spårbarhet
- CLI-entrypoint via `python -m rovarsprak` eller installerat kommando

---

## Installation

```bash
git clone <repo-url>
cd rovarsprak_converter

python3 -m venv venv
source venv/bin/activate

pip install -e .
```

---

## Kör programmet

Via modul:

```bash
python -m rovarsprak
```

Via installerat CLI-kommando:

```bash
rovar
```

---

## Loggning

Loggar sparas i:

```
rovarsprak/logs/rovarsprak.log
```

Loggningen spårar:
- menyval
- filoperationer
- batchprocesser
- fel

---

## Krav

Python 3.11+

Inga externa dependencies.