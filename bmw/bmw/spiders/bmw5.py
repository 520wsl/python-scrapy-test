# -*- coding: utf-8 -*-
import scrapy
from bmw.items import BmwItem


class Bmw5Spider(scrapy.Spider):
    name = 'bmw5'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/65.html']

    def parse(self, response):
        uiboxs = response.xpath("//div[@class='uibox']")[1:]
        for uibox in uiboxs:
            category = uibox.xpath(".//div[@class='uibox-title']/a/text()").get()
            urls = uibox.xpath(".//ul/li/a/img/@src").getall()
            # for url in urls:
            #     url = response.urljoin(url)
            #     self.log(url)
            # self.log(category)
            # self.log(urls)
            # pass
            urls = list(map(lambda url: response.urljoin(url), urls))
            item = BmwItem(category=category, urls=urls)
            yield item
