# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class EasySpider(CrawlSpider):
    name = 'easy'
    allowed_domains = ['www.qidian.com']
    start_urls = ['https://www.qidian.com/all?orderId=&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=0&page=1']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//*[@class='lbf-pagination-next']/@href")),
        Rule(LinkExtractor(restrict_xpaths='//ul[@class="all-img-list cf"]//li//h4/a/@href'), callback='parse_item'),
    )

    def parse_item(self, response):
        item = {}
        item['src'] = response.xpath('//ui[@class="cf"]//li/a/@href').get()
        # item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        # item['name'] = response.xpath('//div[@id="name"]').get()
        # item['description'] = response.xpath('//div[@id="description"]').get()
        return item
