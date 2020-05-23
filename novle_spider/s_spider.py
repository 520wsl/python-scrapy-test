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
import scrapy.core.downloader.handlers.datauri
import scrapy.core.downloader.handlers.file
import scrapy.core.downloader.handlers.s3

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


def hello():
    """
    打印欢迎界面
    """
    print('*' * 100)
    print('\t\t\t\tNovel Tool')
    print('\t\t @Author : Mad Dragon')
    print('\t\t @Email: 395548460@qq.com')
    print('\t\t @Version: 2.0.1')
    print('\t\t @Time: 2020年5月23日')
    print('*' * 100)


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
    hello()

    print('\n')
    print(' * =' * 25)
    print('\t\t\t\t 工具列表')
    print('\t\t ID\t:\t name')
    print('\t\t 0\t:\t退出程序')
    print('\t\t 1\t:\t笔趣阁 ( www.biquge.lu )')
    print('\t\t 2\t:\t起点中文网 ( www.qidian.com )')
    print(' * =' * 25)
    print('\n')

    print('请根据工具列表选择相对应的工具ID\n')
    ID = input('请输入ID (例如 1):')

    if ID:
        ID = int(ID)
    if ID == 0:
        print('*' * 20 + ' 本次服务到此结束，欢迎下次使用。 ' + ('*' * 20))
        input('回车关闭窗口 ==》')
        exit()

    elif ID == 1:
        print('= = ' * 20 + ' 1:  笔趣阁 ( www.biquge.lu ) ' + ('= = ' * 20))
        print('\n')
        biquge_spider()
        print('\n')
        print('= = ' * 20 + ' 1:  笔趣阁 ( www.biquge.lu )' + ('= = ' * 20))

    elif ID == 2:
        print('= = ' * 20 + ' 2: 起点中文网 ( www.qidian.com ) ' + ('= = ' * 20))
        print('\n')
        qidian_spider()
        print('\n')
        print('= = ' * 20 + ' 2: 起点中文网 ( www.qidian.com ) ' + ('= = ' * 20))

    main()


if __name__ == '__main__':
    main()
