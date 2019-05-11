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

process = CrawlerProcess(get_project_settings())

process.crawl('qiandian_book')
process.start()
