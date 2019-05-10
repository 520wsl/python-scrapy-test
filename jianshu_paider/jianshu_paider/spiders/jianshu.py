# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from jianshu_paider.items import JianshuPaiderItem


class JianshuSpider(CrawlSpider):
    name = 'jianshu'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://www.jianshu.com/']

    rules = (
        Rule(LinkExtractor(allow=r'.*/p/[0-9a-z]{12}.*'), callback='parse_detail', follow=True),
    )

    def parse_detail(self, response):
        item = {}
        title = response.xpath("//h1[@class='title']/text()").get()
        avatar = response.xpath("//div[@class='avatar']/img/@src").get()
        author = response.xpath("//div[@class='author']//span[@class='name']/a/text()").get()
        pub_time = response.xpath("//span[@class='publish-time']/text()").get()
        url = response.url
        url1 = url.split('?')[0]
        article_id = url1.split('/')[-1]
        content = response.xpath("//div[@class='show-content']").get()

        yield JianshuPaiderItem(
            title=title,
            author=author,
            avatar=avatar,
            pub_time=pub_time,
            article_id=article_id,
            content=content,
            origin_url=response.url
        )
