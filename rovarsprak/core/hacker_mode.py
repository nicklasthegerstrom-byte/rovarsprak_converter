# rovarsprak/core/hacker_mode.py

# ===== GLOBAL STATE =====
HACKER_MODE = False

# ===== COLORS FOR HACKER MODE =====
RESET         = "\033[0m"
HACKER_GREEN  = "\033[92m"
HACKER_AMBER  = "\033[93m"
HACKER_BG     = "\033[40m"   # svart bakgrund (80s terminal vibes)

# ===== STATE TOGGLE =====
def toggle() -> bool:
    """
    Växlar hacker mode mellan True och False.
    Returnerar det nya läget.
    """
    global HACKER_MODE
    HACKER_MODE = not HACKER_MODE
    return HACKER_MODE

# ===== COLOR WRAPPER =====
def color(text: str) -> str:
    """
    Returnerar färgad text om hacker mode är aktivt.
    Annars returneras texten ofärgad.
    """
    if HACKER_MODE:
        return f"{HACKER_GREEN}{text}{RESET}"
    return text