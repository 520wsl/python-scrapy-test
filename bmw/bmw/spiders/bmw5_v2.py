# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bmw.items import BmwItem


class Bmw5Spider(CrawlSpider):
    name = 'bmw5_v2'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/65.html']

    rules = (
        Rule(LinkExtractor(allow=r"https://car.autohome.com.cn/pic/series/65-.+"), callback="parse_page", follow=True),
    )

    def parse_page(self, response):
        category = response.xpath('//div[@class="uibox"]/div/text()').get()
        # self.log(category)
        srcs = response.xpath("//div[contains(@class,'uibox-con')]/ul/li//img/@src").getall()
        srcs = list(map(lambda x: response.urljoin(x.replace('t_', '')), srcs))
        # self.log(srcs)
        yield BmwItem(category=category, image_urls=srcs)

    def test_parse(self, response):
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
