# -*- coding: utf-8 -*-
import json
from urllib.parse import urljoin
from fn.items import FnItem

import scrapy
import os

class FengniaoSpider(scrapy.Spider):
    name = 'fengniao'
    allowed_domains = ['fengniao.com']
    start_urls = ['https://tu.fengniao.com/ajax/ajaxTuPicList.php?page=1&tagsId=13&action=getPicLists']

    def parse(self, response):
        photos = json.loads(response.body)
        for item in photos['photos']['photo']:
            print(item)
            src = urljoin(item['src'], '?imageView2/2/w/1800/q/90/ignore-error/1/')
            title = item['title']
            id = item['id']
            yield FnItem(src=src, title=title, id=id)
