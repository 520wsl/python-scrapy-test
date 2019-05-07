# -*- coding: utf-8 -*-
import json
from urllib.parse import urljoin
from fn.items import FnItem

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class FengniaoSpider(CrawlSpider):
    name = 'fengniao_crawl'
    allowed_domains = ['fengniao.com']
    start_urls = ['https://tu.fengniao.com/13']
    rules = (
        # Rule(LinkExtractor(allow=r'/\d/'), follow=True),
        Rule(LinkExtractor(allow=r'https://tu.fengniao.com/ajax/ajaxTuPicList.php?page=1&tagsId=\d&action=getPicLists'), callback='parse_detail', follow=False),
    )

    def parse_detail(self, response):
        print(response)
        photos = json.loads(response.body)
        for item in photos['photos']['photo']:
            # print(item)
            src = urljoin(item['src'], '?imageView2/2/w/1800/q/90/ignore-error/1/')
            title = item['title']
            id = item['id']
            yield FnItem(src=src, title=title, id=id)
        yield response
