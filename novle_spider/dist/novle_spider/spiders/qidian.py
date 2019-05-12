# -*- coding: utf-8 -*-
import json
import time
from urllib.parse import urljoin

import scrapy
from scrapy.http import Request
from novle_spider.items import NovleSpiderItem


class QidianSpider(scrapy.Spider):
    name = 'qidian'
    start_urls = []
    book_info_path = 'https://book.qidian.com/info/{0}'
    catalog_path = 'https://read.qidian.com/ajax/book/category?_csrfToken=&bookId={0}'

    def __init__(self):
        self.start()

    def start(self):
        time.sleep(3)
        print('= =' * 10 + ' 请输入起点中文网 小说 ID ' + ('= =' * 10))
        bookId = input('请输入起点中文网 小说 ID ==>  ')
        path = self.book_info_path.format(int(bookId))

        print('= =' * 10 + ' 即将抓取书籍 【 ' + path + ' 】 ' + ('= =' * 10))
        print('==> 10 秒后 开始抓取小说')
        time.sleep(10)
        if not len(self.start_urls):
            self.start_urls.append(path)
        else:
            self.start_urls[0] = path

    def parse(self, response):
        name = response.xpath('//title/text()').get()

        if name == '起点中文网_阅文集团旗下网站':
            self.log('没有找到书籍，请确认后重新尝试。')
            self.start()

        bookId = response.url.split('/')[-1]
        path = self.catalog_path.format(int(bookId))

        self.log('==' * 30)
        self.log("==> 开始下载小说。。。")
        yield Request(url=path, meta={'bookId': bookId, 'name': name}, callback=self.parse_item)

    def parse_item(self, response):
        bookId = response.meta['bookId']
        name = response.meta['name']
        uuid = 1
        vnid = 1
        catalogs = []

        apiData = json.loads(response.text)
        # self.log(apiData)
        if apiData['data']['vs']:
            vss = apiData['data']['vs']
            for vs in vss:
                vn = str(vnid) + '_' + vs['vN']
                vnid += 1
                vip = vs['vS']
                for cs in vs['cs']:
                    catalogId = cs['id']
                    if vip == 0:
                        cU = urljoin(response.url, '/chapter/' + cs['cU'])
                    else:
                        cU = urljoin(response.url, '/chapter/' + str(bookId) + '/' + str(catalogId))
                        vn = vs['vN'] + '_VIP'
                    cN = str(uuid) + '_' + cs['cN']
                    # self.log(catalog)
                    catalogs.append({
                        'vn': vn,
                        'catalogId': catalogId,
                        'cU': cU,
                        'cN': cN,
                        'uuid': uuid,
                        'name': name,
                        'bookId': bookId
                    })
                    uuid += 1
            # self.log(catalogs)
        for catalog in catalogs:
            self.log(catalog)
            yield Request(url=catalog['cU'], meta=catalog, callback=self.catalog_txt)

    def catalog_txt(self, response):
        content = response.xpath('//div[contains(@class,"read-content")]/p/text()').getall()
        content = "\n".join(content)
        catalog = response.meta
        # self.log(content)
        yield NovleSpiderItem(content=content, vn=catalog['vn'], catalogId=catalog['catalogId'], cU=response.url,
                              cN=catalog['cN'], uuid=catalog['uuid'], bookId=catalog['bookId'], name=catalog['name'])
