# ===== NORMAL MODE COLORS =====
N_RESET = "\033[0m"
N_YELLOW = "\033[93m"
N_MAGENTA = "\033[95m"
N_RED = "\033[91m"
N_CYAN = "\033[96m"

def color(text: str, code: str) -> str:
    return f"{code}{text}{N_RESET}"
