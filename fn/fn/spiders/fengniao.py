# -*- coding: utf-8 -*-
import json
import re
import time
from urllib.parse import urljoin
from fn.items import FnItem
from scrapy import Request
import scrapy
import os


class FengniaoSpider(scrapy.Spider):
    name = 'fengniao'
    allowed_domains = ['fengniao.com']
    start_urls = [
        'https://tu.fengniao.com/',
    ]
    base_img_api = "https://tu.fengniao.com/ajax/ajaxTuPicList.php?page={0}&tagsId={1}&action=getPicLists"
    max_page_num = 200

    def parse(self, response):
        # self.log(response)
        tagsIds = response.xpath("//div[@class='labelMenu module90']/a/@href").getall()
        titles = response.xpath("//div[@class='labelMenu module90']/a/text()").getall()
        # self.log(tagsIds)
        for tagsId, title in zip(tagsIds, titles):
            # self.log(urljoin(response.url, tagsId))
            # yield scrapy.Request(urljoin(response.url, tagsId), callback=self.parse_item)
            m = re.search('[0-9]+', tagsId)
            if m:
                id = m.group()
                index = 1  # 起始页码设置为1
                while True:
                    url = self.base_img_api.format(index, id)
                    if index > self.max_page_num:
                        self.log('当前页码:[ %s ] - [ %s ] - [ %s ]  : 只抓取前 %s 页数据 url : [ %s ]' % (
                            title, id, index, self.max_page_num, url))
                        break
                    # self.log(url)
                    index += 1
                    yield Request(url=url, meta={
                        'title': title,
                        'id': id
                    }, callback=self.parse_item_img)

    def parse_item_img(self, response):
        meta = response.meta
        info = []
        photos = json.loads(response.body)
        # self.log(photos)
        for item in photos['photos']['photo']:
            # print(item)
            src = urljoin(item['src'], '?imageView2/2/w/1800/q/90/ignore-error/1/')
            title = item['title']
            id = item['id']
            chan_name = meta['title']
            chan_id = meta['id']
            yield FnItem(src=src, title=title, id=id, chan_name=chan_name, chan_id=chan_id)
