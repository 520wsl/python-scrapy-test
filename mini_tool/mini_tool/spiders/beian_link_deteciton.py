# -*- coding: utf-8 -*-
import time

import scrapy
from mini_tool.items import MiniToolItem
import xlrd
import os, sys

#  网站备案链接检测工具
class BeianLinkDetecitonSpider(scrapy.Spider):
    handle_httpstatus_list = [404, 403, 500, 502]
    name = 'beian_link_deteciton'
    # allowed_domains = ['http://www.juchangcheng.com/']
    start_urls = []
    all_website = []

    def __init__(self):
        self.start()

    def start(self):
        time.sleep(3)
        path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'template')
        file_path = os.path.join(path, 'template.xls')
        book = xlrd.open_workbook(file_path)
        table = book.sheets()[0]  # 通过索引顺序获取
        nrows = table.nrows
        self.log(nrows)

        for i in range(nrows):
            if i == 0:  # 跳过第一行
                continue
            row_values = table.row_values(i)
            self.all_website.append({
                'index': row_values[0],
                'company_name': row_values[1],
                'website_url': row_values[2],
            })
            self.start_urls.append(row_values[2])
        self.log(self.all_website)

    def parse(self, response):
        self.log(response.url)
        self.log(response.status)

        dataInfo = {}
        dataInfo['status'] = response.status
        dataInfo['index'] = ''
        dataInfo['company_name'] = ''
        for item in self.all_website:
            if item['website_url'] == response.url:
                dataInfo['index'] = item['index']
                dataInfo['company_name'] = item['company_name']

        dataInfo['url'] = response.url

        if response.status == 403 and  response.status == 404 and response.status == 500 and response.status == 502:
            dataInfo['title'] = ''
            dataInfo['keywords'] = ''
            dataInfo['description'] = ''
            dataInfo['beian_link_txt'] = ''
            dataInfo['beian_link'] = ''
            dataInfo['is_beian'] = False
        else:
            dataInfo['title'] = response.xpath('//title/text()').get()
            dataInfo['keywords'] = response.xpath('//meta[@name="keywords"]/@content').get()
            dataInfo['description'] = response.xpath('//meta[@name="description"]/@content').get()
            dataInfo['beian_link_txt'] = " ".join(
                response.xpath('//a[contains(@href,"beian.miit.gov.cn")]//text()').getall()).strip()
            dataInfo['beian_link'] = response.xpath(
                '//a[contains(@href,"beian.miit.gov.cn")]/@href').get()
            dataInfo['is_beian'] = True
            if dataInfo['beian_link'] == None:
                self.log('未查询到本站点备案链接信息，请人工确认：' + dataInfo['url'])
                dataInfo['is_beian'] = False
        dataInfo['time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        # self.log(dataInfo)
        yield MiniToolItem(
            index=dataInfo['index'],
            status=dataInfo['status'],
            is_beian=dataInfo['is_beian'],
            company_name=dataInfo['company_name'],
            url=dataInfo['url'],
            beian_link_txt=dataInfo['beian_link_txt'],
            beian_link=dataInfo['beian_link'],
            title=dataInfo['title'],
            keywords=dataInfo['keywords'],
            description=dataInfo['description'],
            time=dataInfo['time']
        )
