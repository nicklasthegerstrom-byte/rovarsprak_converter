from rovarsprak.ui.normal.ui import run_normal_ui
from rovarsprak.core.hacker_mode import HACKER_MODE
from rovarsprak.ui.hacker.ui import run_hacker_ui

def main():
    while True:
        if HACKER_MODE:
            result = run_hacker_ui()
        else:
            result = run_normal_ui()

        if result == "EXIT":
            break