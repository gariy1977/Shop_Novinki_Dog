# sources/base.py
from abc import ABC, abstractmethod
from typing import List
from core.product import Product


class BaseSource(ABC):
    name: str = "unknown"

    @abstractmethod
    async def search(self, query: str) -> List[Product]:
        """
        Возвращает список товаров в формате Product
        """
        raise NotImplementedError("search() must be implemented in source")
