# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random
import time
from scrapy.http.response.html import HtmlResponse
from scrapy import signals
from selenium import webdriver


class SeleniumDownloadMiddleware(object):
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r'E:\soft\chromedriver.exe')

    def process_request(self, request, spider):
        self.driver.get(request.url)
        time.sleep(1)
        try:
            while True:
                showMore = self.driver.find_element_by_class_name('show-more')
                showMore.click()
                time.sleep(0.3)
                if not showMore:
                    break
        except:
            pass

        source = self.driver.page_source
        response = HtmlResponse(url=self.driver.current_url, body=source, request=request, encoding='utf-8')
        return response
