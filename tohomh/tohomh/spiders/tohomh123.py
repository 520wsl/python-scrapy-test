# -*- coding: utf-8 -*-
import json
from urllib.parse import urlencode

import scrapy
from scrapy.http.request import Request
from tohomh.items import TohomhItem, ContentItem


class Tohomh123Spider(scrapy.Spider):
    name = 'tohomh123'
    allowed_domains = ['tohomh123.com']
    start_urls = ['https://www.tohomh123.com/zhenhunjie/', 'https://www.tohomh123.com/shengxu/']

    def parse(self, response):
        info = response.xpath("//div[@class='info']")
        name = info.xpath("./h1/text()").get()
        author = info.xpath("./p[@class='subtitle']/text()").get().split('：')[-1]
        comicUrl = response.url
        comicStatus = info.xpath("./p/span[@class='block']/span/text()").get()
        category = ','.join(info.xpath("./p/span[contains(@class,'ticai')]/a/text()").getall())
        synoptic = info.xpath("./p[@class='content']/text()").get()
        yield TohomhItem(name=name, author=author, comicUrl=comicUrl,
                         comicStatus=comicStatus, category=category, synoptic=synoptic)

        chapters = response.xpath("//div[@id='chapterlistload']/ul[2]//li")
        for chapter in chapters:
            chapter_name = chapter.xpath('./a/text()').get()
            chapter_url = chapter.xpath('./a/@href').get()
            if chapter_url:
                yield Request(url=response.urljoin(chapter_url), callback=self.get_content,
                              meta={'info': (name, comicUrl, chapter_name)})

    def get_content(self, response):
        comicName, comicUrl, chapter = response.meta.get('info')
        javascript = ''.join(response.xpath('//script[@type="text/javascript"]/text()').getall()).split(';')
        did = javascript[1].split('did=')[-1]
        sid = javascript[2].split('sid=')[-1]
        count = int(javascript[5].split(' = ')[-1]) + 1
        bq = int(javascript[8].split(' = ')[-1])

        if bq == 1:
            self.log('= ' * 15 + ' 版权问题，无法下载 : ' + comicName + ' =' * 15)
            return

        for iid in range(1, count):
            params = {
                'did': did,
                'sid': sid,
                'iid': iid
            }
            url = response.urljoin('/action/play/read' + '?' + urlencode(params))
            chapters = response.url.split('/')[-1].split('.')[0] + '_' + chapter
            yield Request(url=url, callback=self.get_image, meta={'info': (comicName, comicUrl, chapters)})

    def get_image(self, response):
        comicName, comicUrl, chapter = response.meta.get('info')
        response_json = json.loads(response.text)
        url = response_json['Code']
        name = comicUrl.split('/')[-2] + '_' + chapter + '_' + url.split('/')[-1]
        yield ContentItem(comicName=comicName, comicUrl=comicUrl, chapter=chapter, url=url, name=name)
