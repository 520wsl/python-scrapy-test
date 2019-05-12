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


def biquge_spider():
    try:
        process = CrawlerProcess(get_project_settings())
        process.crawl('biquge')
        process.start()
    except Exception as e:
        print('--出现错误--', e)


def qidian_spider():
    try:
        process = CrawlerProcess(get_project_settings())
        process.crawl('qidian')
        process.start()
    except Exception as e:
        print('--出现错误--', e)


def main():
    print('= =' * 10 + ' 请输入小说网站ID ' + ('= =' * 10))
    print('\t0 : 笔趣阁 ( www.biquge.lu )')
    print('\t1 : 起点中文网 ( www.qidian.com )')
    print('= =' * 25)
    webid = int(input('请输入小说网站ID：'))

    if webid == 0:
        print('= =' * 10 + ' 0 : 笔趣阁 ( www.biquge.lu ) ' + ('= =' * 10))
        print('\n')
        biquge_spider()
    elif webid == 1:
        print('= =' * 10 + ' 1 : 起点中文网 ( www.qidian.com ) ' + ('= =' * 10))
        print('\n')
        qidian_spider()

    print('= =' * 10 + ' 小说爬取完成 ' + ('= =' * 10))
    input('回车关闭窗口 ==》')


if __name__ == '__main__':
    main()

# process = CrawlerProcess(get_project_settings())
#
# print('= =' * 10 + ' 请输入小说网站ID ' + ('= =' * 10))
# print('\t0 : 笔趣阁 ( www.biquge.lu )')
# print('\t1 : 起点中文网 ( www.qidian.com )')
# print('= =' * 25)
# webid = int(input('请输入小说网站ID：'))
#
# if webid == 0:
#     process.crawl('biquge')
# elif webid == 1:
#     process.crawl('qidian')
#
# print('= =' * 10 + ' 小说爬取完成 ' + ('= =' * 10))
#
#
#
# process.start()
