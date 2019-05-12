# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NovleSpiderItem(scrapy.Item):
    vn = scrapy.Field()
    uuid = scrapy.Field()
    name = scrapy.Field()
    bookId = scrapy.Field()
    cN = scrapy.Field()
    cU = scrapy.Field()
    catalogId = scrapy.Field()
    content = scrapy.Field()
