from database import MENU_FILE, read_lines, append_line
from validators import valid_text, valid_price


def add_item():
    item_id = input("Enter item ID: ").strip()

    if not valid_text(item_id):
        print("Item ID cannot be empty.")
        return

    for line in read_lines(MENU_FILE):
        if line.split("|")[0] == item_id:
            print("An item with this ID already exists.")
            return

    name = input("Enter item name: ").strip()
    price = input("Enter price: ").strip()

    if not valid_text(name) or not valid_price(price):
        print("Enter a valid name and price.")
        return

    append_line(MENU_FILE, f"{item_id}|{name}|{float(price):.2f}")
    print("Menu item added successfully.")


def view_menu():
    items = read_lines(MENU_FILE)

    if not items:
        print("No menu items found.")
        return

    print("\n----- Canteen Menu -----")
    for line in items:
        item_id, name, price = line.split("|")
        print(f"ID: {item_id} | {name} | ₹{price}")


def search_item():
    keyword = input("Enter item name or ID: ").strip().lower()

    if not keyword:
        print("Search value cannot be empty.")
        return

    found = False
    for line in read_lines(MENU_FILE):
        item_id, name, price = line.split("|")
        if keyword in item_id.lower() or keyword in name.lower():
            print(f"ID: {item_id} | {name} | ₹{price}")
            found = True

    if not found:
        print("No matching item found.")
