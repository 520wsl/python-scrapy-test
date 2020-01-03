# -*- coding: utf-8 -*-
import re
import time
from urllib.parse import urlparse, urljoin

import scrapy
from mini_tool.items import MiniToolItem, CollectTotalItem
import xlrd
import os, sys


# 网站 收录情况 查询
class CollectTotalSpider(scrapy.Spider):
    name = 'collect_total'
    start_urls = [
        'https://www.baidu.com/s?wd=www.shuxinjixie.cn',
        'https://www.baidu.com/s?wd=灵动的艺术',
        'https://www.baidu.com/s?wd=www.zwdldj.com',
        'https://www.baidu.com/s?wd=www.yxguangyang.com',
        'https://www.baidu.com/s?wd=www.shuixianggushi.com',
        'https://www.baidu.com/s?wd=www.shuxinjixie.cn',
        'https://www.baidu.com/s?wd=www.enss.cn',
    ]
    all_website = []
    baidu_path = 'https://www.baidu.com/s?wd=%s'
    baidu_site_path = 'https://www.baidu.com/s?wd=site:%s'
    so_path = 'https://www.so.com/s?q=%s'
    so_site_path = 'https://www.so.com/s?q=site:%s'

    def parse(self, response):
        self.log(response.url)
        meta = {}
        urldict = urlparse(response.url)
        meta['site'] = urldict.query.replace('wd=', '').strip()
        try:
            meta['baidu_nums'] = ''.join(re.findall(r'\d+', response.xpath('//span[@class="nums_text"]/text()').get()))
        except:
            meta['baidu_nums'] = ''
        url = self.baidu_site_path % meta['site']
        yield scrapy.Request(url=url, meta=meta, callback=self.baidu_site)

    def baidu_site(self, response):
        meta = response.meta
        try:
            nums = response.xpath('//div[contains(@class,"op_site_domain")]//span//text()').getall()
            meta['baidu_site'] = ''.join(re.findall(r'\d+', ''.join(nums)))
        except:
            meta['baidu_site'] = ''
        url = self.so_path % meta['site']
        yield scrapy.Request(url=url, meta=meta, callback=self.so_nums)

    def so_nums(self, response):
        meta = response.meta
        try:
            meta['so_nums'] = ''.join(re.findall(r'\d+', response.xpath('//span[@class="nums"]/text()').get()))
        except:
            meta['so_nums'] = ''
        url = self.so_site_path % meta['site']
        yield scrapy.Request(url=url, meta=meta, callback=self.so_site)

    def so_site(self, response):
        meta = response.meta
        try:
            nums = ''.join(re.findall(r'该网站约(.*?)个网页被360搜索收录', response.text))
            meta['so_site'] = ''.join(re.findall(r'\d+', nums))
        except:
            meta['so_site'] = ''

        yield CollectTotalItem(
            site=meta['site'],
            baidu_nums=meta['baidu_nums'],
            baidu_site=meta['baidu_site'],
            so_nums=meta['so_nums'],
            so_site=meta['so_site']
        )
