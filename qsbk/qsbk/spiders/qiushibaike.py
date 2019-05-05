# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector.unified import SelectorList


class QiushibaikeSpider(scrapy.Spider):
    name = 'qiushibaike'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/page/1/']

    def parse(self, response):
        duanzidivs = response.xpath("//div[@id='content-left']/div")
        self.log(type(duanzidivs))
        self.log(duanzidivs)

        for duanzidiv in duanzidivs:
            self.log(type(duanzidiv))
            author = duanzidiv.xpath('.//h2/text()').get().strip()
            self.log(author)
            content = duanzidiv.xpath('.//div[@class="content"]//text()').getall()
            content = " ".join(content).strip()
            self.log(content)
            duanzi = {'author': author, "content": content}
            yield duanzi
