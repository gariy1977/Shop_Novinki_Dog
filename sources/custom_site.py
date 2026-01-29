
from sources.base import BaseSource
from core.product import Product


class CustomSiteSource(BaseSource):
    name = "custom_site"

    async def search(self, query: str):
        # TODO: реализовать парсер сайта / API
        return []
