# -*- coding: utf-8 -*-
import socket
from urllib.parse import urljoin

import scrapy
from scrapy.http import Request
from scrapy.loader import ItemLoader

from qidian.items import QidianItem


class BasicSpider(scrapy.Spider):
    name = 'qidian'
    allowed_domains = ['www.qidian.com']
    start_urls = [
        'https://www.qidian.com/all?orderId=&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=0&page=1',
    ]

    def parse(self, response):
        item_selector = response.xpath('//ul[@class="all-img-list cf"]//li//h4/a/@href')
        for url in item_selector.extract():
            self.log('urljoin 2 ==>: %s' % urljoin(response.url, url))
            yield Request(urljoin(response.url, url), callback=self.catalog_item)

        next_selector = response.xpath('//*[@class="lbf-pagination-next "]/@href')
        for url in next_selector.extract():
            self.log('urljoin==>: %s' % urljoin(response.url, url))
            yield Request(urljoin(response.url, url))
        #
        # info = self.parse_item(response=response)
        # self.log('info : %s' % info)

    def parse_item(self, response):
        """  This function parses a property page.

        :param response: 请求
        :return:  人会
        @url http://vip.book.sina.com.cn/weibobook/cate.php?cate_id=1036&w=0&s=0&order=1&vt=4&page=3
        @returns items 1
        @scrapes book_id src title img_url state author chan_name synoptic platform platform_src

        """
        self.log('parse_item :=======> %s' % str(response))
        l = ItemLoader(item=QidianItem(), response=response)
        l.add_xpath('book_id', '//div[@class="book_list"]/ul//li/div[@class="book_info"]/p[@class="book_name"]/a/@href',
                    re='[0-9]+')
        l.add_xpath('src', '//div[@class="book_list"]/ul//li/div[@class="book_info"]/p[@class="book_name"]/a/@href')
        l.add_xpath('title', '//div[@class="book_list"]/ul//li/div[@class="book_info"]/p[@class="book_name"]/a/text()')
        l.add_xpath('img_url', '//div[@class="book_list"]/ul//li/div[@class="img_box"]/a/img/@src')
        l.add_xpath('state', '//div[@class="book_list"]/ul//li/div[@class="book_info"]/p[@class="book_author"]/text()',
                    re='(?<=【).*?(?=】)')
        l.add_xpath('author',
                    '//div[@class="book_list"]/ul//li/div[@class="book_info"]/p[@class="book_author"]/span/text()')
        l.add_xpath('chan_name', '//div[@class="all-fr-title"]/text()')
        l.add_xpath('synoptic', '//div[@class="book_list"]/ul//li/div[@class="book_info"]/p[@class="info"]/a/text()')
        l.add_value('platform', '新浪读书')
        l.add_value('platform_src', 'http://vip.book.sina.com.cn')
        return l.load_item()

    def catalog_item(self, response):
        next_selector = response.xpath('//ui[@class="cf"]//li/a/@href')
        self.log(next_selector)
        # for url in next_selector.extract():
        #     self.log('urljoin 3==>: %s' % urljoin(response.url, url))
            # yield Request(urljoin(response.url, url))
        return next_selector
