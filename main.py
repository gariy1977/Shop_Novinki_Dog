# main.py
import asyncio
from sources.aliexpress import AliExpressSource
from core.pipeline import SearchPipeline
from core.filters import filter_by_brand


async def main():
    sources = [
        AliExpressSource()
    ]

    filters = [
        lambda p: filter_by_brand(p, ["nike", "adidas"])
    ]

    pipeline = SearchPipeline(sources, filters)
    products = await pipeline.run("кроссовки")

    for p in products:
        print(p)


if __name__ == "__main__":
    asyncio.run(main())
