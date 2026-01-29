# main.py
import asyncio
import logging

from sources.aliexpress import AliExpressSource
from core.pipeline import SearchPipeline
from core.filters import filter_by_brand
from sources.custom_site import CustomSiteSource

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

sources = [
    AliExpressSource(),
    CustomSiteSource()
]

async def run_search(query: str):
    logging.info(f"🔍 Поиск товаров: {query}")

    sources = [
        AliExpressSource(),
    ]

    filters = [
        lambda p: filter_by_brand(p, ["nike", "adidas"]),
    ]

    pipeline = SearchPipeline(sources, filters)
    products = await pipeline.run(query)

    logging.info(f"✅ Найдено товаров: {len(products)}")

    for product in products:
        logging.info(product)


async def main():
    try:
        await run_search("кроссовки")
    except Exception as e:
        logging.exception("❌ Ошибка в main:", exc_info=e)


if __name__ == "__main__":
    asyncio.run(main())
