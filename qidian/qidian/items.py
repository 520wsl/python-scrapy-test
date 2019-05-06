# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class QidianItem(Item):
    book_id = Field()
    src = Field()
    title = Field()
    img_url = Field()
    state = Field()
    author = Field()
    chan_name = Field()
    sub_name = Field()
    synoptic = Field()
