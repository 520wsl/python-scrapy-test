# -*- coding: utf-8 -*-
import scrapy
from qidian.items import QidianItem


class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['vip.book.sina.com.cn']
    start_urls = (
        'http://vip.book.sina.com.cn/weibobook/cate.php?cate_id=1036&w=0&s=0&order=1&vt=4&page=1',
        'http://vip.book.sina.com.cn/weibobook/cate.php?cate_id=1036&w=0&s=0&order=1&vt=4&page=2',
        'http://vip.book.sina.com.cn/weibobook/cate.php?cate_id=1036&w=0&s=0&order=1&vt=4&page=3',
    )

    def parse(self, response):
        item = QidianItem()

        item['book_id'] = response.xpath('//div[@class="book_list"]/ul//li/div[@class="book_info"]/p[@class="book_name"]/a/@href').extract()
        item['src'] = response.xpath('//div[@class="book_list"]/ul//li/div[@class="book_info"]/p[@class="book_name"]/a/@href').extract()
        item['title'] = response.xpath('//div[@class="book_list"]/ul//li/div[@class="book_info"]/p[@class="book_name"]/a/text()').extract()
        item['img_url'] = response.xpath('//div[@class="book_list"]/ul//li/div[@class="img_box"]/a/img/@src').extract()
        item['state'] = response.xpath('//div[@class="book_list"]/ul//li/div[@class="book_info"]/p[@class="book_author"]/text()').extract()
        item['author'] = response.xpath('//div[@class="book_list"]/ul//li/div[@class="book_info"]/p[@class="book_author"]/span/text()').extract()
        item['chan_name'] = response.xpath('//div[@class="all-fr-title"]/text()').extract()
        item['synoptic'] = response.xpath('//div[@class="book_list"]/ul//li/div[@class="book_info"]/p[@class="info"]/a/text()').extract()

        return item

        # self.log('book_id:  %s' % response.xpath(
        #     '//div[@class="book_list"]/ul//li/div[@class="book_info"]/p[@class="book_name"]/a/@href').extract())
        # self.log('src:  %s' % response.xpath(
        #     '//div[@class="book_list"]/ul//li/div[@class="book_info"]/p[@class="book_name"]/a/@href').extract())
        # self.log('title:  %s' % response.xpath(
        #     '//div[@class="book_list"]/ul//li/div[@class="book_info"]/p[@class="book_name"]/a/text()').extract())
        # self.log('img_url:  %s' % response.xpath(
        #     '//div[@class="book_list"]/ul//li/div[@class="img_box"]/a/img/@src').extract())
        # self.log('state:  %s' % response.xpath(
        #     '//div[@class="book_list"]/ul//li/div[@class="book_info"]/p[@class="book_author"]/text()').extract())
        # self.log('author:  %s' % response.xpath(
        #     '//div[@class="book_list"]/ul//li/div[@class="book_info"]/p[@class="book_author"]/span/text()').extract())
        # self.log('chan_name:  %s' % response.xpath('//div[@class="all-fr-title"]/text()').extract())
        # self.log('synoptic:  %s' % response.xpath(
        #     '//div[@class="book_list"]/ul//li/div[@class="book_info"]/p[@class="info"]/a/text()').extract())
