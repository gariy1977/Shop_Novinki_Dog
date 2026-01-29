# sources/custom_site.py
import json
import aiohttp
from bs4 import BeautifulSoup

from sources.base import BaseSource
from core.product import Product


class CustomSiteSource(BaseSource):
    name = "custom_sites"

    async def load_sites(self):
        try:
            with open("sites.json", "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []

    async def search(self, query: str):
        sites = await self.load_sites()
        results = []

        if not sites:
            return results

        async with aiohttp.ClientSession() as session:
            for site in sites:
                try:
                    url = site["search_url"].format(query=query)

                    async with session.get(url, timeout=10) as resp:
                        html = await resp.text()

                    soup = BeautifulSoup(html, "html.parser")

                    for card in soup.select(site["product_selector"]):
                        title_el = card.select_one(site["title_selector"])
                        price_el = card.select_one(site["price_selector"])
                        img_el = card.select_one(site["image_selector"])
                        link_el = card.select_one(site["link_selector"])

                        if not title_el or not price_el:
                            continue

                        title = title_el.text.strip()
                        price = price_el.text.strip()
                        img = img_el["src"] if img_el and img_el.has_attr("src") else ""
                        link = link_el["href"] if link_el and link_el.has_attr("href") else url

                        results.append(Product(
                            name=title,
                            description="",
                            price=price,
                            link=link,
                            images=[img] if img else [],
                            source=site.get("name", "custom_site")
                        ))

                except Exception as e:
                    print(f"⚠️ Ошибка сайта {site.get('name')}: {e}")

        return results
