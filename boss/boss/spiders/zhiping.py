# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from boss.items import BossItem


class ZhipingSpider(CrawlSpider):
    name = 'zhiping'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://www.zhipin.com/c100010000/?query=python&page=1&ka=page-1']

    rules = (
        # 匹配职位列表的规则
        Rule(LinkExtractor(allow=r'.+\?query=python&page=\d'), follow=True),
        # 匹配职位列表页的规则
        Rule(LinkExtractor(allow=r'.+job_detail/.+\.html'), callback='parse_job', follow=False),
    )

    def parse_job(self, response):
        name = response.xpath("//div[@class='name']/h1/text()").get().strip()
        salary = response.xpath("//div[@class='name']/span/text()").get().strip()
        job_info = response.xpath(
            "//div[contains(@class,'job-primary')]/div[@class='info-primary']/p[1]/text()").getall()
        city = job_info[0]
        work_years = job_info[1]
        education = job_info[2]
        company = response.xpath("//div[@class='company-info']/a[last()]/text()").get().strip()
        yield BossItem(name=name, salary=salary, city=city, work_years=work_years, education=education,
                       company=company)
