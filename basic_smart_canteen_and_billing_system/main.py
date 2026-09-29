from menu import add_item, view_menu, search_item
from orders import place_order, view_orders
from billing import generate_bill
from reports import sales_report


def show_menu():
    print("\n===== Smart Canteen and Billing System =====")
    print("1. Add Menu Item")
    print("2. View Menu")
    print("3. Search Menu Item")
    print("4. Place Order")
    print("5. View Orders")
    print("6. Generate Bill")
    print("7. Sales Report")
    print("8. Exit")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_item()
        elif choice == "2":
            view_menu()
        elif choice == "3":
            search_item()
        elif choice == "4":
            place_order()
        elif choice == "5":
            view_orders()
        elif choice == "6":
            generate_bill()
        elif choice == "7":
            sales_report()
        elif choice == "8":
            print("Thank you for using the Smart Canteen and Billing System.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 8.")


if __name__ == "__main__":
    main()
