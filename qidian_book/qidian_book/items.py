# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QidianBookItem(scrapy.Item):
    vn = scrapy.Field()
    id = scrapy.Field()
    cU = scrapy.Field()
    cN = scrapy.Field()
    uuid = scrapy.Field()
    content = scrapy.Field()
    bookId = scrapy.Field()
