from dataclasses import dataclass
from typing import List


@dataclass
class Product:
    name: str
    description: str
    price: str
    link: str
    images: List[str]   # URL картинок
    source: str         # откуда найден
