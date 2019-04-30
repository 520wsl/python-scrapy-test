# -*- coding: utf-8 -*-
import socket

import scrapy
from scrapy.loader import ItemLoader

from qidian.items import QidianItem


class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['vip.book.sina.com.cn']
    start_urls = (
        'http://vip.book.sina.com.cn/weibobook/cate.php?cate_id=1036&w=0&s=0&order=1&vt=4&page=1',
        'http://vip.book.sina.com.cn/weibobook/cate.php?cate_id=1036&w=0&s=0&order=1&vt=4&page=2',
        'http://vip.book.sina.com.cn/weibobook/cate.php?cate_id=1036&w=0&s=0&order=1&vt=4&page=3',
        'http://vip.book.sina.com.cn/weibobook/cate.php?cate_id=1036&w=0&s=0&order=1&vt=4&page=1000',
    )

    def parse(self, response):
        """  This function parses a property page.

        :param response: 请求
        :return:  人会
        @url http://vip.book.sina.com.cn/weibobook/cate.php?cate_id=1036&w=0&s=0&order=1&vt=4&page=3
        @returns items 1
        @scrapes book_id src title img_url state author chan_name synoptic platform platform_src

        """

        l = ItemLoader(item=QidianItem(), response=response)
        l.add_xpath('book_id', '//div[@class="book_list"]/ul//li/div[@class="book_info"]/p[@class="book_name"]/a/@href',re='[0-9]+')
        l.add_xpath('src', '//div[@class="book_list"]/ul//li/div[@class="book_info"]/p[@class="book_name"]/a/@href')
        l.add_xpath('title', '//div[@class="book_list"]/ul//li/div[@class="book_info"]/p[@class="book_name"]/a/text()')
        l.add_xpath('img_url', '//div[@class="book_list"]/ul//li/div[@class="img_box"]/a/img/@src')
        l.add_xpath('state', '//div[@class="book_list"]/ul//li/div[@class="book_info"]/p[@class="book_author"]/text()',re='(?<=【).*?(?=】)')
        l.add_xpath('author',
                    '//div[@class="book_list"]/ul//li/div[@class="book_info"]/p[@class="book_author"]/span/text()')
        l.add_xpath('chan_name', '//div[@class="all-fr-title"]/text()')
        l.add_xpath('synoptic', '//div[@class="book_list"]/ul//li/div[@class="book_info"]/p[@class="info"]/a/text()')
        l.add_value('platform','新浪读书')
        l.add_value('platform_src','http://vip.book.sina.com.cn')
        return l.load_item()