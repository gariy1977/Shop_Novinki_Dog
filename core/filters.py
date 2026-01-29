# core/filters.py
from core.product import Product
import re


def normalize_text(text: str) -> str:
    return text.lower().strip()


def filter_by_brand(product: Product, allowed_brands: list) -> bool:
    if not product.name:
        return False

    name = normalize_text(product.name)
    return any(normalize_text(b) in name for b in allowed_brands)


def extract_price(price_str: str) -> int | None:
    try:
        digits = re.findall(r"\d+", price_str.replace(" ", ""))
        return int("".join(digits)) if digits else None
    except:
        return None


def filter_by_price(product: Product, min_price: int, max_price: int) -> bool:
    price = extract_price(product.price)
    if price is None:
        return False
    return min_price <= price <= max_price
