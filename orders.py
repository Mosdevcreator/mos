from pricing import line_total


def summarize_order(lines: list[tuple[int, int]]) -> dict[str, int]:
    total_cents = sum(line_total(unit_price_cents, quantity) for unit_price_cents, quantity in lines)
    return {"line_count": len(lines), "total_cents": total_cents}
