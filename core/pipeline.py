# core/pipeline.py
from typing import List, Callable
from core.product import Product
import logging


class SearchPipeline:

    def __init__(self, sources: list, filters: List[Callable]):
        self.sources = sources
        self.filters = filters

    async def run(self, query: str) -> List[Product]:
        results = []
        seen_links = set()

        for source in self.sources:
            try:
                products = await source.search(query)
            except Exception as e:
                logging.warning(f"⚠️ Ошибка источника {source}: {e}")
                continue

            for product in products:
                try:
                    if product.link in seen_links:
                        continue

                    if all(f(product) for f in self.filters):
                        results.append(product)
                        seen_links.add(product.link)

                except Exception as e:
                    logging.warning(f"⚠️ Ошибка фильтра товара {product}: {e}")

        return results
