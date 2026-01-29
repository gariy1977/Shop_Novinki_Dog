# sources/aliexpress.py
from sources.base import BaseSource
from core.product import Product


class AliExpressSource(BaseSource):
    name = "aliexpress"

    async def search(self, query: str):
        # TODO: заменить на реальный API / парсер
        demo_products = [
            Product(
                name=f"Nike Air Force 1 — {query}",
                description="Классические кроссовки, комфорт и стиль",
                price="59$",
                link="https://ref-link/airforce",
                images=[
                    "https://example.com/img1.jpg",
                    "https://example.com/img2.jpg"
                ],
                source=self.name
            ),
            Product(
                name=f"Adidas Superstar — {query}",
                description="Легендарные кеды Adidas",
                price="64$",
                link="https://ref-link/superstar",
                images=[
                    "https://example.com/img3.jpg"
                ],
                source=self.name
            )
        ]

        return demo_products
