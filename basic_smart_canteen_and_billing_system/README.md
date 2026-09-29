# Smart Canteen and Billing System

A simple terminal-based Python application for managing canteen menu items, customer orders, bills, and basic sales reports.

## Features

- Add menu items
- View menu
- Search menu items
- Place orders
- View orders
- Generate bills with 5% tax
- Prevent duplicate bills
- View basic sales report
- Local text-file storage
- Input validation

## Requirements

- Python 3.x
- No external Python packages

## Run

```bash
python main.py
```

## Project Structure

```text
basic_smart_canteen_and_billing_system/
├── data/
│   ├── menu.txt
│   ├── orders.txt
│   └── bills.txt
├── main.py
├── menu.py
├── orders.py
├── billing.py
├── reports.py
├── database.py
├── validators.py
├── README.md
├── statement.md
├── TESTING.md
├── requirements.txt
└── .gitignore
```

## Storage Format

Menu:
`item_id|name|price`

Orders:
`order_id|item_id|quantity`

Bills:
`order_id|subtotal|tax|total`

## Author

Divyansh Chandra
