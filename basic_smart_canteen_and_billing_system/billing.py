from database import MENU_FILE, ORDERS_FILE, BILLS_FILE, read_lines, append_line

TAX_RATE = 0.05


def generate_bill():
    orders = read_lines(ORDERS_FILE)
    menu = read_lines(MENU_FILE)

    if not orders:
        print("No orders available.")
        return

    order_id = input("Enter order ID to generate bill: ").strip()
    order = next((o for o in orders if o.split("|")[0] == order_id), None)

    if not order:
        print("Order not found.")
        return

    _, item_id, quantity = order
    item = next((m for m in menu if m.split("|")[0] == item_id), None)

    if not item:
        print("Menu item not found.")
        return

    _, name, price = item
    quantity = int(quantity)
    subtotal = float(price) * quantity
    tax = subtotal * TAX_RATE
    total = subtotal + tax

    bill_record = f"{order_id}|{subtotal:.2f}|{tax:.2f}|{total:.2f}"

    if any(line.split("|")[0] == order_id for line in read_lines(BILLS_FILE)):
        print("Bill for this order already exists.")
        return

    append_line(BILLS_FILE, bill_record)

    print("\n===== Bill =====")
    print(f"Order ID: {order_id}")
    print(f"Item: {name}")
    print(f"Quantity: {quantity}")
    print(f"Subtotal: ₹{subtotal:.2f}")
    print(f"Tax (5%): ₹{tax:.2f}")
    print(f"Total: ₹{total:.2f}")
