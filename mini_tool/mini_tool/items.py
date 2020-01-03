# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MiniToolItem(scrapy.Item):
    index = scrapy.Field()
    status = scrapy.Field()
    company_name = scrapy.Field()
    beian_link_txt = scrapy.Field()
    beian_link = scrapy.Field()
    is_beian = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    keywords = scrapy.Field()
    description = scrapy.Field()
    time = scrapy.Field()


class CollectTotalItem(scrapy.Item):
    site = scrapy.Field()
    baidu_nums = scrapy.Field()
    baidu_site = scrapy.Field()
    so_nums = scrapy.Field()
    so_site = scrapy.Field()
