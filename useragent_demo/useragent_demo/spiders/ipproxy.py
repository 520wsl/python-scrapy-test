# -*- coding: utf-8 -*-
import json

import scrapy


class IpproxySpider(scrapy.Spider):
    name = 'ipproxy'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/ip']

    def parse(self, response):
        origin = json.loads(response.text)['origin']
        self.log('==' * 30)
        self.log(origin)
        self.log('==' * 30)
        yield scrapy.Request(self.start_urls[0], dont_filter=True)
