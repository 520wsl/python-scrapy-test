# -*- coding: utf-8 -*-
import scrapy
import json


class ApiSpider(scrapy.Spider):
    name = 'api'
    allowed_domains = ['read.qidian.com']
    start_urls = ['https://read.qidian.com/ajax/book/category?_csrfToken=&bookId=1004608738']

    def parse(self, response):
        js = json.loads(response.body)
        print(js)
