from database import MENU_FILE, ORDERS_FILE, read_lines, append_line
from validators import valid_quantity


def item_exists(item_id):
    return any(line.split("|")[0] == item_id for line in read_lines(MENU_FILE))


def place_order():
    item_id = input("Enter item ID: ").strip()

    if not item_exists(item_id):
        print("Item ID not found.")
        return

    quantity = input("Enter quantity: ").strip()

    if not valid_quantity(quantity):
        print("Quantity must be a positive whole number.")
        return

    order_id = len(read_lines(ORDERS_FILE)) + 1
    append_line(ORDERS_FILE, f"{order_id}|{item_id}|{int(quantity)}")
    print(f"Order placed successfully. Order ID: {order_id}")


def view_orders():
    orders = read_lines(ORDERS_FILE)

    if not orders:
        print("No orders found.")
        return

    print("\n----- Orders -----")
    for line in orders:
        order_id, item_id, quantity = line.split("|")
        print(f"Order ID: {order_id} | Item ID: {item_id} | Quantity: {quantity}")
