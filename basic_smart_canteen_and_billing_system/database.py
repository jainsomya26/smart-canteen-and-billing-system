from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"
MENU_FILE = DATA_DIR / "menu.txt"
ORDERS_FILE = DATA_DIR / "orders.txt"
BILLS_FILE = DATA_DIR / "bills.txt"

DATA_DIR.mkdir(exist_ok=True)


def read_lines(file_path):
    if not file_path.exists():
        return []
    with open(file_path, "r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]


def append_line(file_path, line):
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(line + "\n")
