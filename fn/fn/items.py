# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FnItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    src = scrapy.Field()
    title = scrapy.Field()
    id = scrapy.Field()

    chan_name = scrapy.Field()
    chan_id = scrapy.Field()
