# -*- coding: utf-8 -*-
from urllib import request
from PIL import Image

import scrapy


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://accounts.douban.com/login']
    login_url = 'https://accounts.douban.com/login'
    profile_url = "https://www.douban.com/people/196062677/"

    def parse(self, response):
        formatdata = {
            'source': 'None',
            'redir': 'https://www.douban.com/',
            'form_email': '970138074@qq.com',
            'form_password': 'pythonspider',
            'remember': 'on',
            'login': '登录'
        }
        captcha_url = response.css('img#captcha_image::attr(src)').get()
        if captcha_url:
            captcha = self.regonize_captcha(captcha_url)
            formatdata['captcha-solution'] = captcha
            capthca_id = response.xpath("//input[@name='captcha-id']/@value").get()
            formatdata['captcha-id'] = capthca_id
        yield scrapy.FormRequest(url=self.login_url, formatdata=formatdata, callback=self.parse_after_login)

    def parse_after_login(self, response):
        if response.url == 'https://www.douban.com/':
            yield scrapy.Request(self.profile_url, callback=self.parse_profile)
            print('登录成功')
        else:
            print('登录失败')

    def parse_profile(self, response):
        print(response.url)
        if response.url == self.profile_url:
            print('进入到个人中心')
            ck = response.xpath("//input[@name='ck']/@value").get()
            formatdata = {
                'ck': ck,
                'signature': '我就是我，不一样的烟火~~'
            }
            yield scrapy.FormRequest(self.ed)
        else:
            print('没有进入到个人中心')

    def regonize_captcha(self, image_url):
        request.urlretrieve(image_url, 'captcha.png')
        image = Image.open('captcha.png')
        image.show()
        captcha = input('请输入验证码')
        return captcha
