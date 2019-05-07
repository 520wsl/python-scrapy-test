# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os

import requests
from scrapy.exporters import JsonLinesItemExporter


class FnPipeline(object):
    # def __init__(self):
    #     self.fp = open('fengniao.txt', 'a', encoding='utf-8')
    #     self.exporter = JsonLinesItemExporter(self.fp, ensure_ascii=False, encoding='utf-8')
    #
    #
    # def process_item(self, item, spider):
    #     # self.exporter.export_item(item=item)
    #     self.fp.write('\n'+item['src'])
    #     return item
    #
    # def close_spider(self, spider):
    #     self.fp.close()
    #     print('爬虫结束。。。。。。。。。')


    def process_item(self, item, spider):
        imgres = requests.get(item['src'])
        if os.path.exists("./images/" + item['chan_name'] + '_' + item['chan_id']) == False:
            os.makedirs("./images/" + item['chan_name'] + '_' + item['chan_id'])

        with open("./images/" + item['chan_name'] + '_' + item['chan_id'] + '/' + item['title'] + '_' + item['id'] + '.jpg', 'wb') as f:
            f.write(imgres.content)
        return item

