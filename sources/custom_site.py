# sources/custom_site.py
import json
import aiohttp
from bs4 import BeautifulSoup
from urllib.parse import urljoin

from sources.base import BaseSource
from core.product import Product


class CustomSiteSource(BaseSource):
    name = "custom_sites"
    sites_file = "sites.json"

    async def load_sites(self):
        try:
            with open(self.sites_file, "r", encoding="utf-8") as f:
                data = json.load(f)

                # Поддержка формата: список или {"sites": [...]}
                if isinstance(data, dict):
                    return data.get("sites", [])

                return data if isinstance(data, list) else []
        except Exception as e:
            print(f"⚠️ Не удалось загрузить sites.json: {e}")
            return []

    async def fetch_html(self, session, url: str):
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        async with session.get(url, headers=headers, timeout=15) as resp:
            return await resp.text()

    async def parse_site(self, site: dict, html: str, base_url: str):
        soup = BeautifulSoup(html, "html.parser")
        results = []

        selector = site.get("product_selector")
        if not selector:
            return results

        for card in soup.select(selector):
            try:
                title_el = card.select_one(site.get("title_selector"))
                price_el = card.select_one(site.get("price_selector"))
                img_el = card.select_one(site.get("image_selector"))
                link_el = card.select_one(site.get("link_selector"))

                if not title_el:
                    continue

                title = title_el.text.strip()
                price = price_el.text.strip() if price_el else ""

                img = ""
                if img_el and img_el.has_attr("src"):
                    img = urljoin(base_url, img_el["src"])

                link = base_url
                if link_el and link_el.has_attr("href"):
                    link = urljoin(base_url, link_el["href"])

                results.append(Product(
                    name=title,
                    description="",
                    price=price,
                    link=link,
                    images=[img] if img else [],
                    source=site.get("name", "custom_site")
                ))

            except Exception as e:
                print(f"⚠️ Ошибка парсинга карточки ({site.get('name')}): {e}")

        return results

    async def search(self, query: str):
        sites = await self.load_sites()
        results = []

        if not sites:
            return results

        async with aiohttp.ClientSession() as session:
            for site in sites:
                try:
                    raw_url = site.get("search_url")
                    if not raw_url:
                        continue

                    url = raw_url.format(query=query)

                    html = await self.fetch_html(session, url)
                    parsed = await self.parse_site(site, html, url)

                    results.extend(parsed)

                except Exception as e:
                    print(f"⚠️ Ошибка сайта {site.get('name')}: {e}")

        return results
