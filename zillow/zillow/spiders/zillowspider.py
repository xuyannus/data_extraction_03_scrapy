import scrapy
import json

from itemloaders import ItemLoader
from ..items import ZillowItem
from ..utils import URL, get_cookie, parse_new_url


class ZillowSpider(scrapy.Spider):
    name = 'zillow'
    allowed_domains = ['www.zillow.com']

    def start_requests(self):
        yield scrapy.Request(
            url=URL,
            callback=self.parse,
            cookies=get_cookie(),
            meta={
                'currentPage': 1
            }
        )

    def parse(self, response):
        current_page = response.meta['currentPage']
        json_resp = json.loads(response.text)
        houses = json_resp['cat1']['searchResults']['listResults']
        total_pages = json_resp['cat1']['searchList']['totalPages']

        for house in houses:
            loader = ItemLoader(item=ZillowItem())
            loader.add_value('id', house.get('id'))
            loader.add_value('image_urls', house.get('imgSrc'))
            loader.add_value('detail_url', house.get('detailUrl'))
            loader.add_value('status_type', house.get('statusType'))
            loader.add_value('status_text', house.get('statusText'))
            loader.add_value('price', house.get('price'))
            loader.add_value('address', house.get('address'))
            loader.add_value('beds', house.get('beds'))
            loader.add_value('baths', house.get('baths'))
            loader.add_value('area_sqft', house.get('area'))
            loader.add_value('latitude', house.get('latLong').get('latitude'))
            loader.add_value('longitude', house.get('latLong').get('longitude'))
            loader.add_value('broker_name', house.get('brokerName'))
            loader.add_value('broker_phone', house.get('brokerPhone'))
            yield loader.load_item()

        print({
            "houses": len(houses),
            "current_page": current_page,
            "total_pages": total_pages
        })

        if current_page <= total_pages:
            current_page += 1
            yield scrapy.Request(
                url=parse_new_url(URL, page_number=current_page),
                callback=self.parse,
                cookies=get_cookie(),
                meta={
                    'currentPage': current_page
                }
            )
