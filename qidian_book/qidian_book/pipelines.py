# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os


class QidianBookPipeline(object):
    def __init__(self):
        self.path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'book_dev')
        if not os.path.exists(self.path):
            os.mkdir(self.path)

    def process_item(self, item, spider):
        # print(item)
        vn = item['vn']
        cN = item['cN']
        bookId = item['bookId']
        name = item['name']
        content = item['content']
        book_path = os.path.join(self.path, name + '_' + bookId)
        if not os.path.exists(book_path):
            os.mkdir(book_path)

        vm_path = os.path.join(book_path, vn)
        if not os.path.exists(vm_path):
            os.mkdir(vm_path)

        with open(os.path.join(vm_path, cN + '.txt'), 'w', encoding='utf-8') as fp:
            fp.write(content)
        return item
