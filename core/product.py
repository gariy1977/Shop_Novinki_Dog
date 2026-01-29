# core/product.py
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Product:
    name: str
    description: str
    price: str
    link: str
    images: List[str] = field(default_factory=list)
    source: str = "unknown"
    rating: Optional[float] = None
    sales: Optional[int] = None
