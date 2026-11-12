def line_total(unit_price_cents: int, quantity: int) -> int:
    if unit_price_cents < 0 or quantity < 0:
        raise ValueError("Prices and quantities must be nonnegative")
    return unit_price_cents * quantity
