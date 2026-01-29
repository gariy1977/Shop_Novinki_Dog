from abc import ABC, abstractmethod
from typing import List
from core.product import Product


class BaseSource(ABC):

    @abstractmethod
    async def search(self, query: str) -> List[Product]:
        """
        Ищет товары по запросу
        """
        pass
