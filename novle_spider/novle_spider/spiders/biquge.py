# -*- coding: utf-8 -*-
import time

import scrapy
from scrapy.http import Request

from novle_spider.items import NovleSpiderItem


class BiqugeSpider(scrapy.Spider):
    name = 'biquge'
    allowed_domains = ['biquge.lu']
    start_urls = []
    book_info_path = 'https://www.biquge.lu/book/{0}/'

    def __init__(self):
        self.start()

    def start(self):
        time.sleep(3)
        print('= =' * 10 + ' 请输入笔趣阁 小说 ID ' + ('= =' * 10))
        bookId = input('请输入笔趣阁 小说 ID ==>  ')
        path = self.book_info_path.format(int(bookId))

        print('= =' * 10 + ' 即将抓取书籍 【 ' + path + ' 】 ' + ('= =' * 10))
        print('==> 10 秒后 开始抓取小说')
        time.sleep(10)
        if not len(self.start_urls):
            self.start_urls.append(path)
        else:
            self.start_urls[0] = path

    def parse(self, response):
        self.log(response.url)

        name = response.xpath('//title/text()').get()
        bookId = response.url.split('/')[-2]
        if name == '404 - 找不到文件或目录。':
            self.log('没有找到书籍，请确认后重新尝试。')
            self.start()
        htmls = response.xpath("//div[@class='listmain']/dl/dt|//div[@class='listmain']/dl/dd")
        catalogs = []
        vn = ''
        uuid = 1
        vnid = 1
        for html in htmls:
            # self.log(html)
            title = html.xpath("./a/text()").get()
            if not title:
                vn = html.xpath("./text()").get()
                vn = str(vnid) + '_' + vn
                vnid += 1

            if title:
                cN = str(uuid) + '_' + title
                url = html.xpath("./a/@href").get()
                cU = response.urljoin(url)
                catalogId = url.split('/')[-1].split('.')[-2]
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
        for catalog in catalogs:
            self.log(catalog)
            yield Request(url=catalog['cU'], meta=catalog, callback=self.catalog_txt)

    def catalog_txt(self, response):
        content = response.xpath('//div[@id="content"]/text()').getall()
        content = "\n".join(content).strip()
        catalog = response.meta
        self.log(content)
        yield NovleSpiderItem(content=content, vn=catalog['vn'], catalogId=catalog['catalogId'], cU=response.url,
                              cN=catalog['cN'], uuid=catalog['uuid'], bookId=catalog['bookId'],
                              name=catalog['name'])
