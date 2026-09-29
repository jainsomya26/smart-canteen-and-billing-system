from database import MENU_FILE, ORDERS_FILE, BILLS_FILE, read_lines


def sales_report():
    menu = read_lines(MENU_FILE)
    orders = read_lines(ORDERS_FILE)
    bills = read_lines(BILLS_FILE)

    print("\n===== Sales Report =====")
    print(f"Menu Items: {len(menu)}")
    print(f"Orders: {len(orders)}")
    print(f"Generated Bills: {len(bills)}")

    total_sales = sum(float(line.split("|")[3]) for line in bills)
    print(f"Total Sales: ₹{total_sales:.2f}")
