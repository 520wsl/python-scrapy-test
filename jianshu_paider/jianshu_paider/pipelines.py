# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class JianshuPaiderPipeline(object):
    def __init__(self):
        dbparams = {
            'host': '172.30.34.155',
            'port': 3306,
            'user': 'root',
            'password': '123456',
            'database': 'jianshu_dev',
            'charset': 'utf8'
        }
        self.conn = pymysql.connect(**dbparams)
        self.cursor = self.conn.cursor()
        self._sql = None

    def process_item(self, item, spider):
        self.cursor.execute(self.sql, (
            item['title'], item['content'], item['author'], item['avatar'], item['pub_time'], item['origin_url'],
            item['article_id']
        ))
        self.conn.commit()
        return item

    @property
    def sql(self):
        if not self._sql:
            self._sql = """
            insert into article(id,title,content,author,avatar,pub_time,origin_url,article_id) values(null,%s,%s,%s,%s,%s,%s,%s)
            """
            return self._sql
        return self._sql


from twisted.enterprise import adbapi
from pymysql import cursors


class jianshuTwistedPipeline(object):
    def __init__(self):
        dbparams = {
            'host': '172.30.34.155',
            'port': 3306,
            'user': 'root',
            'password': '123456',
            'database': 'jianshu_dev',
            'charset': 'utf8mb4',
            'cursorclass': cursors.DictCursor
        }
        self.dbpool = adbapi.ConnectionPool('pymysql', **dbparams)
        self._sql = None

    @property
    def sql(self):
        if not self._sql:
            self._sql = """
                insert into article(id,title,content,author,avatar,pub_time,origin_url,article_id) values(null,%s,%s,%s,%s,%s,%s,%s)
                """
            return self._sql
        return self._sql

    def process_item(self, item, spider):
        defer = self.dbpool.runInteraction(self.insert_item, item)
        defer.addErrback(self.handle_error, item, spider)

    def insert_item(self, cursor, item):
        cursor.execute(self.sql, (
            item['title'], item['content'], item['author'], item['avatar'], item['pub_time'], item['origin_url'],
            item['article_id']
        ))
        # self.conn.commit()

    def handle_error(self, error, item, spider):
        print('=' * 10 + "error" + '=' * 10)
        print(error)
        print('=' * 10 + "error" + '=' * 10)
