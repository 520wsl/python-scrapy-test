# -*- coding: utf-8 -*-
from urllib import request
from PIL import Image

import scrapy


class DoubanSpider(scrapy.Spider):
    name = 'douban_login'
    allowed_domains = ['douban.com']
    start_urls = ['https://accounts.douban.com/passport/login']
    login_url = 'https://accounts.douban.com/j/mobile/login/basic'
    profile_url = "https://www.douban.com/people/196062677/"
    editsignature_url = "https://www.douban.com/j/people/196062677/edit_signature"

    def parse(self, response):
        formdata = {
            'ck': '',
            'name': '13625719920',
            'password': 'maddragon016613.',
            'remember': 'false',
            'ticket': ''
        }
        # captcha_url = response.css('img#captcha_image::attr(src)').get()
        # if captcha_url:
        #     captcha = self.regonize_captcha(captcha_url)
        #     formdata['captcha-solution'] = captcha
        #     capthca_id = response.xpath("//input[@name='captcha-id']/@value").get()
        #     formdata['captcha-id'] = capthca_id
        yield scrapy.FormRequest(url=self.login_url, formdata=formdata, callback=self.parse_after_login)

    def parse_after_login(self, response):
        if response.url == self.login_url:
            yield scrapy.Request(self.profile_url, callback=self.parse_profile)
            self.log('登录成功')
        else:
            self.log('登录失败')

    def parse_profile(self, response):
        self.log(response.url)
        if response.url == self.profile_url:
            self.log('进入到个人中心')
            ck = response.xpath("//input[@name='ck']/@value").get()
            formdata = {
                'ck': ck,
                'signature': '虽然年少轻狂，却只知道胜者为王'
            }
            yield scrapy.FormRequest(self.editsignature_url, formdata=formdata)
        else:
            self.log('没有进入到个人中心')

    def regonize_captcha(self, image_url):
        request.urlretrieve(image_url, 'captcha.png')
        image = Image.open('captcha.png')
        image.show()
        captcha = input('请输入验证码:')
        return captcha
