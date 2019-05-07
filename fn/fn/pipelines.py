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
        if os.path.exists("./images/" + item['chan_name'] + '_' + item['chan_id']) == False:
            os.makedirs("./images/" + item['chan_name'] + '_' + item['chan_id'])

        with open("./images/" + item['chan_name'] + '_' + item['chan_id'] + '/' + item['title'] + '_' + item['id'] + '.jpg', 'wb') as f:
            f.write(imgres.content)
        return item
