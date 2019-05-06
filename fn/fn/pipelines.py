# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os

import requests


class FnPipeline(object):
    def process_item(self, item, spider):
        imgres = requests.get(item['src'])
        if os.path.exists(item['title']) == False:
            os.mkdir(item['title'])

        with open('./' + item['title']+'/' + item['id'] + '.jpg', 'wb') as f:
            f.write(imgres.content)
        return item
