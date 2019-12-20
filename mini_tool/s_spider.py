from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

# 这里是必须引入的
import scrapy.spiderloader
import scrapy.statscollectors
import scrapy.logformatter

import scrapy.extensions
import scrapy.extensions.corestats
import scrapy.extensions.telnet
import scrapy.extensions.memusage
import scrapy.extensions.memdebug
import scrapy.extensions.closespider
import scrapy.extensions.feedexport
import scrapy.extensions.logstats
import scrapy.extensions.spiderstate
import scrapy.extensions.throttle

import scrapy.core.scheduler
import scrapy.core.engine
import scrapy.core.scraper
import scrapy.core.spidermw
import scrapy.core.downloader
import scrapy.core.downloader.handlers.http
import scrapy.core.downloader.contextfactory
import scrapy.core.downloader.handlers.ftp

import scrapy.downloadermiddlewares.stats
import scrapy.downloadermiddlewares.httpcache
import scrapy.downloadermiddlewares.cookies
import scrapy.downloadermiddlewares.useragent
import scrapy.downloadermiddlewares.httpproxy
import scrapy.downloadermiddlewares.ajaxcrawl
import scrapy.downloadermiddlewares.decompression
import scrapy.downloadermiddlewares.defaultheaders
import scrapy.downloadermiddlewares.downloadtimeout
import scrapy.downloadermiddlewares.httpauth
import scrapy.downloadermiddlewares.httpcompression
import scrapy.downloadermiddlewares.redirect
import scrapy.downloadermiddlewares.retry
import scrapy.downloadermiddlewares.robotstxt

import scrapy.spidermiddlewares.depth
import scrapy.spidermiddlewares.httperror
import scrapy.spidermiddlewares.offsite
import scrapy.spidermiddlewares.referer
import scrapy.spidermiddlewares.urllength

import scrapy.pipelines
import scrapy.dupefilters
import scrapy.squeues

import queuelib


# 自己项目用到的
import xlwt
import xlrd

# 1: 网站备案链接检测工具
def beian_link_deteciton():
    try:
        process = CrawlerProcess(get_project_settings())
        process.crawl('beian_link_deteciton')
        process.start()
    except Exception as e:
        print('--出现错误--', e)


def main():
    print('= =' * 10 + ' Mini Tool ' + ('= =' * 10))
    print('\t @Name: 迷你工具箱')
    print('\t @Author : Mad Dragon')
    print('\t @Email: 395548460@qq.com')
    print('\t @Time: 2019年12月20日')
    print('= =' * 10 + ' Mini Tool ' + ('= =' * 10))

    print('= =' * 25)
    print('\n')
    print('\t ID : name')
    print('\t 1 : 网站备案链接检测工具')
    print('= =' * 25)

    print('\t 请在下方填写需要使用的工具ID')
    webid = int(input('请输入工具ID：'))

    if webid == 1:
        print('= =' * 10 + ' 1: 网站备案链接检测工具 ' + ('= =' * 10))
        print('\n')
        beian_link_deteciton()

    print('= =' * 10 + ' 本次服务到此结束，欢迎下次使用。 ' + ('= =' * 10))
    input('回车关闭窗口 ==》')


if __name__ == '__main__':
    main()
