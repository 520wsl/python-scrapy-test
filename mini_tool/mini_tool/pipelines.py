# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import time

import xlwt

from mini_tool.items import MiniToolItem, CollectTotalItem


class MiniToolPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, MiniToolItem):
            print(1)
        elif isinstance(item, CollectTotalItem):
            print(2)

        return item

    # def __init__(self):
    #     self.path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'result_dev')
    #     if not os.path.exists(self.path):
    #         os.mkdir(self.path)
    #     self.file_path = os.path.join(self.path,
    #                                   time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()) + '-beianLinkDeteciton.xls')
    #     self.wbook = xlwt.Workbook()
    #     self.first_sheet = self.wbook.add_sheet(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()),
    #                                             cell_overwrite_ok=True)
    #     self.row = 0
    #
    # def open_spider(self, spider):
    #     row = ['导入序号', '网站状态', '是否备案', '公司名', "站点网址", '备案信息', '备案链接', "站点title", "站点关键词", "站点描述", '查询时间']
    #     self.style = xlwt.XFStyle()
    #     pattern = xlwt.Pattern()
    #     pattern.pattern = xlwt.Pattern.SOLID_PATTERN
    #     pattern.pattern_fore_colour = xlwt.Style.colour_map['red']  # 设置单元格背景色为黄色
    #     self.style.pattern = pattern
    #
    #     self.style2 = xlwt.XFStyle()
    #     pattern2 = xlwt.Pattern()
    #     pattern2.pattern = xlwt.Pattern.SOLID_PATTERN
    #     pattern2.pattern_fore_colour = xlwt.Style.colour_map['yellow']  # 设置单元格背景色为黄色
    #     self.style2.pattern = pattern2
    #
    #     for i in range(len(row)):
    #         self.first_sheet.write(0, i, row[i])
    #
    # def process_item(self, item, spider):
    #     self.row += 1
    #
    #     for j, job in enumerate(item):
    #         if item['is_beian']:
    #             self.first_sheet.write(self.row, j, item[job])
    #         elif item['status'] != 200:
    #             self.first_sheet.write(self.row, j, item[job], style=self.style)
    #         else:
    #             self.first_sheet.write(self.row, j, item[job], style=self.style2)
    #
    #     self.wbook.save(self.file_path)
    #     return item
    #
    # def close_spider(self, spider):
    #     print('爬虫结束。。。。。。。。。')
