# sources/custom_site.py
import json
import aiohttp
from bs4 import BeautifulSoup
from sources.base import BaseSource
from core.product import Product


class CustomSiteSource(BaseSource):
    name = "custom_sites"

    async def search(self, query: str):
        with open("sites.json", "r", encoding="utf-8") as f:
            sites = json.load(f)

        results = []

        async with aiohttp.ClientSession() as session:
            for site in sites:
                url = site["search_url"].format(query=query)

                async with session.get(url) as resp:
                    html = await resp.text()

                soup = BeautifulSoup(html, "html.parser")

                for card in soup.select(site["product_selector"]):
                    title = card.select_one(site["title_selector"])
                    price = card.select_one(site["price_selector"])
                    img = card.select_one(site["image_selector"])

                    if not title or not price or not img:
                        continue

                    results.append(Product(
                        name=title.text.strip(),
                        description="",
                        price=price.text.strip(),
                        link=url,
                        images=[img["src"]],
                        source=site["name"]
                    ))

        return results
