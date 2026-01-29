# core/filters.py
from core.product import Product


def filter_by_brand(product: Product, allowed_brands: list) -> bool:
    return any(b.lower() in product.name.lower() for b in allowed_brands)


def filter_by_price(product: Product, min_price: int, max_price: int) -> bool:
    try:
        price = int(''.join(filter(str.isdigit, product.price)))
        return min_price <= price <= max_price
    except:
        return False
