# Libraries
import os

# -------------------------------- Directories ------------------------------- #

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(CURRENT_DIR, os.pardir))

DATA_DIR = os.path.join(PROJECT_DIR, 'data')

# -------------------------------- File Paths -------------------------------- #

TERMINAL_PATH = os.path.join(DATA_DIR, 'terminal.json')

STRINGS_PATH = os.path.join(DATA_DIR, 'strings.json')
