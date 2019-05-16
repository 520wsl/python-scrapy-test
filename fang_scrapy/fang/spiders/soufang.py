# -*- coding: utf-8 -*-
import copy
import re

import scrapy
from fang.items import NewHouseItem, ESFHouseItem


class SoufangSpider(scrapy.Spider):
    name = 'sfw'
    allowed_domains = ['fang.com']
    start_urls = ['https://www.fang.com/SoufunFamily.htm']

    def parse(self, response):
        trs = response.xpath("//div[@class='outCont']//tr")
        province = None
        for tr in trs:
            tds = tr.xpath(".//td[not(@class)]")
            province_td = tds[0]
            province_text = province_td.xpath(".//text()").get()
            province_text = re.sub(r"\s", '', province_text)
            if province_text:
                province = province_text
            # 不爬取海外链接
            if province == '其它':
                continue

            city_td = tds[1]
            city_links = city_td.xpath('.//a')
            for city_link in city_links:
                city = city_link.xpath(".//text()").get()
                city_url = city_link.xpath(".//@href").get()
                domains = city_url.split(".")
                # self.log(domains)
                if 'bj' in domains[0]:
                    newhouse_url = 'https://newhouse.fang.com/house/s/'
                    esf_url = 'https://esf.fang.com/'
                else:
                    # 构建新房的url链接
                    newhouse = copy.deepcopy(domains)
                    newhouse.insert(1, 'newhouse')
                    newhouse_url = '.'.join(newhouse) + 'house/s/'

                    # 构建二手房的url链接
                    esf = copy.deepcopy(domains)
                    esf.insert(1, 'esf')
                    esf_url = '.'.join(esf)

                # self.log(province)
                # self.log(city)
                # self.log(city_url)
                #
                # self.log(newhouse_url)
                # self.log(esf_url)
                yield scrapy.Request(url=newhouse_url, callback=self.parse_newhouse, meta={"info": (province, city)})
                yield scrapy.Request(url=esf_url, callback=self.parse_esf, meta={"info": (province, city)})
                # break
            # break

    def parse_newhouse(self, response):
        province, city = response.meta.get('info')
        lis = response.xpath('//div[contains(@class,"nl_con")]/ul/li')
        for li in lis:
            name = li.xpath('.//div[@class="nlcd_name"]/a/text()').get()
            if not name:
                continue
            name = name.strip()
            # print(name)
            house_type_list = li.xpath('.//div[contains(@class,"house_type")]/a/text()').getall()
            house_type_list = list(map(lambda x: re.sub(r'\s', "", x), house_type_list))
            rooms = list(filter(lambda x: x.endswith("居"), house_type_list))
            # print(rooms)
            area = "".join(li.xpath('.//div[contains(@class,"house_type")]/text()').getall())
            area = re.sub(r"\s|－|/", "", area)
            # print(area)
            address = li.xpath(".//div[@class='address']/a/@title").get()
            # print(address)
            district_text = "".join(li.xpath(".//div[@class='address']/a//text()").getall())
            # print(district_text)
            try:
                district = re.search(r".*\[(.+)\].*", district_text).group(1)
            except:
                district = ''
            # print(district)
            sale = li.xpath(".//div[contains(@class,'fangyuan')]/span/text()").get()
            # print(sale)
            price = "".join(li.xpath(".//div[@class='nhouse_price']//text()").getall())
            price = re.sub(r"\s|广告", "", price)
            # print(price)
            origin_url = li.xpath(".//div[@class='nlcd_name']/a/@href").get()
            # print(origin_url)
            item = NewHouseItem(name=name, rooms=rooms, area=area, address=address, district=district, sale=sale,
                                price=price, origin_url=origin_url, city=city, province=province)
            yield item

        next_url = response.xpath("//div[@class='page']//a[@class='next']/@href").get()
        # print(next_url)

        if next_url:
            yield scrapy.Request(url=response.urljoin(next_url), callback=self.parse_newhouse,
                                 meta={"info": (province, city)})

    def parse_esf(self, response):
        province, city = response.meta.get('info')
        dls = response.xpath('//div[contains(@class,"hop_list")]/dl')
        for dl in dls:
            name = dl.xpath(".//p[@class='add_shop']/a/text()").get()
            if not name:
                continue
            item = ESFHouseItem(province=province, city=city)
            item['name'] = name.strip()
            # print(name)
            infos = dl.xpath(".//p[@class='tel_shop']/text()").getall()
            infos = list(map(lambda x: re.sub(r'\s', "", x), infos))
            # print(infos)
            for info in infos:
                if "厅" in info:
                    item['rooms'] = info
                elif "层" in info:
                    item['floor'] = info
                elif "向" in info:
                    item['toward'] = info
                elif "年建" in info:
                    item['year'] = info.replace("年建", "")
                elif "㎡" in info:
                    item['area'] = info
                else:
                    pass
            # print(item)
            item['address'] = dl.xpath(".//p[@class='add_shop']/span/text()").get()
            # print(address)
            item['price'] = "".join(dl.xpath(".//dd[@class='price_right']/span[1]//text()").getall())
            item['unit'] = dl.xpath(".//dd[@class='price_right']/span[2]/text()").get()
            detail_url = dl.xpath('.//h4[@class="clearfix"]/a/@href').get()
            item['origin_url'] = response.urljoin(detail_url)
            # print(item)
            yield item

        next_url = response.xpath("//div[@id='list_D10_15']/p[3]/a/@href").get()
        # print(next_url)

        if not next_url:
            url = response.xpath("//div[@id='list_D10_15']/p[1]/a/@href").get()
            if not url == '/house/':
                next_url = url
        # print(next_url)
        # print('=='*30)
        if next_url:
            yield scrapy.Request(url=response.urljoin(next_url), callback=self.parse_esf,
                                 meta={"info": (province, city)})
