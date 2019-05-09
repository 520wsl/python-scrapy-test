# -*- coding: utf-8 -*-
import json

import scrapy


class HttpbinSpider(scrapy.Spider):
    name = 'httpbin'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/user-agent']

    def parse(self, response):
        user_agent = json.loads(response.text)['user-agent']
        self.log('==' * 30)
        self.log(user_agent)
        self.log('==' * 30)

        yield scrapy.Request(self.start_urls[0], dont_filter=True)
