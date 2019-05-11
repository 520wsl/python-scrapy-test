# -*- coding: utf-8 -*-
from urllib.parse import urljoin

import scrapy
import json
from scrapy.http import Request
from qidian_book.items import QidianBookItem


class QiandianBookSpider(scrapy.Spider):
    name = 'qiandian_book'
    allowed_domains = ['read.qidian.com', 'book.qidian.com']
    start_urls = ['https://read.qidian.com']
    book_info_path = 'https://book.qidian.com/info/{0}'
    catalog_path = 'https://read.qidian.com/ajax/book/category?_csrfToken=&bookId={0}'

    def parse(self, response):
        bookId = input('请输入起点中文网 小说id：')
        path = self.book_info_path.format(int(bookId))
        self.log(path)
        yield Request(url=path, meta={'bookId': bookId}, callback=self.parse_book, errback=self.error_book)

    def error_book(self, response):
        self.log('没有找到书籍，请确认后重新尝试。')
        yield Request(url=self.start_urls[0], callback=self.parse)

    def parse_book(self, response):
        # self.log(response)
        name = response.xpath('//title/text()').get()

        if name == '起点中文网_阅文集团旗下网站':
            self.log('没有找到书籍，请确认后重新尝试。')
            yield Request(url=self.start_urls[0], callback=self.parse)

        bookId = response.meta['bookId']
        path = self.catalog_path.format(int(bookId))
        yield Request(url=path, meta={'bookId': bookId, 'name': name}, callback=self.parse_item)

    def parse_item(self, response):
        bookId = response.meta['bookId']
        name = response.meta['name']
        uuid = 1
        vnid = 1

        apiData = json.loads(response.text)
        # self.log(apiData)
        if apiData['data']['vs']:
            vss = apiData['data']['vs']
            for vs in vss:
                # self.log(vs)
                vn = str(vnid) + '_' + vs['vN']
                vnid += 1
                vip = vs['vS']
                for cs in vs['cs']:
                    bookId = bookId
                    id = cs['id']
                    if vip == 0:
                        cU = urljoin(response.url, '/chapter/' + cs['cU'])
                    else:
                        cU = urljoin(response.url, '/chapter/' + str(bookId) + '/' + str(id))
                        vn = vs['vN'] + '_VIP'
                    cN = str(uuid) + '_' + cs['cN']
                    catalog = {
                        'vn': vn,
                        'id': id,
                        'cU': cU,
                        'cN': cN,
                        'uuid': uuid,
                        'name': name,
                        'bookId': bookId
                    }
                    uuid += 1
                    # self.log(catalog)
                    yield Request(url=catalog['cU'], meta=catalog, callback=self.catalog_txt)

    def catalog_txt(self, response):
        content = response.xpath('//div[contains(@class,"read-content")]/p/text()').getall()
        content = "\n".join(content)
        catalog = response.meta
        # self.log(content)
        yield QidianBookItem(content=content, vn=catalog['vn'], id=catalog['id'], cU=response.url, cN=catalog['cN'],
                             uuid=catalog['uuid'], bookId=catalog['bookId'], name=catalog['name'])
