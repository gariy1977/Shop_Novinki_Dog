# core/pipeline.py
from typing import List
from core.product import Product


class SearchPipeline:

    def __init__(self, sources: list, filters: list):
        self.sources = sources
        self.filters = filters

    async def run(self, query: str) -> List[Product]:
        results = []

        for source in self.sources:
            products = await source.search(query)

            for product in products:
                if all(f(product) for f in self.filters):
                    results.append(product)

        return results
