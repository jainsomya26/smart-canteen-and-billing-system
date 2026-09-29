def valid_text(value):
    return bool(value.strip())


def valid_price(value):
    try:
        return float(value) >= 0
    except ValueError:
        return False


def valid_quantity(value):
    try:
        return int(value) > 0
    except ValueError:
        return False
