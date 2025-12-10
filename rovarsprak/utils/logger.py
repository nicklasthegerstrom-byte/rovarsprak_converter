import logging
from pathlib import Path

# 1. Bestäm var loggar ska sparas
LOG_DIR = Path(__file__).resolve().parent.parent / "logs"

# 2. Se till att mappen finns
LOG_DIR.mkdir(exist_ok=True)

# 3. Bestäm loggfilens namn
LOG_FILE = LOG_DIR / "rovarsprak.log"

# 4. Konfigurera Python-loggning
logging.basicConfig(
    filename=LOG_FILE,
    filemode="a",     # "append" → behåll gamla loggar
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

# 5. Skapa en logger-instans
logger = logging.getLogger("rovarsprak")

