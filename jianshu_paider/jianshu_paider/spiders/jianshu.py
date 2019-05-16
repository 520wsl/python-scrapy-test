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

        read_count = response.xpath("//span[@class='views-count']/text()").get().split()[-1]
        word_count = response.xpath("//span[@class='wordage']/text()").get().split()[-1]
        comments_count = response.xpath("//span[@class='comments-count']/text()").get().split()[-1]
        like_count = response.xpath("//span[@class='likes-count']/text()").get().split()[-1]

        subjects = ','.join(response.xpath("//div[@class='include-collection']/a/div/text()").getall())

        yield JianshuPaiderItem(
            title=title,
            author=author,
            avatar=avatar,
            pub_time=pub_time,
            article_id=article_id,
            content=content,
            origin_url=response.url,
            read_count=read_count,
            word_count=word_count,
            like_count=like_count,
            comments_count=comments_count,
            subjects=subjects
        )
