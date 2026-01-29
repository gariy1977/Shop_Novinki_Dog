from sources.base import BaseSource
from core.product import Product


class AliExpressSource(BaseSource):

    async def search(self, query: str):
        # ПОКА ЗАГЛУШКА
        return [
            Product(
                name="Nike Air Force 1",
                description="Классические кроссовки",
                price="59$",
                link="https://ref-link",
                images=[
                    "https://example.com/img1.jpg",
                    "https://example.com/img2.jpg"
                ],
                source="aliexpress"
            )
        ]
