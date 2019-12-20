# -*- coding: utf-8 -*-
import scrapy


class BeianLinkDetecitonSpider(scrapy.Spider):
    name = 'beian_link_deteciton'
    allowed_domains = ['http://www.juchangcheng.com/']
    start_urls = ['http://http://www.juchangcheng.com//']

    def parse(self, response):
        pass
