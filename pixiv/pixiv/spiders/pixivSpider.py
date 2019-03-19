# -*- coding: utf-8 -*-
import scrapy
import re
from pixiv.items import PixivItem

class PixivspiderSpider(scrapy.Spider):
    name = 'pixivSpider' #爬虫的名字
    allowed_domains = ['pixivision.net'] #允许的域名
    start_urls = ['https://www.pixivision.net/zh/c/illustration'] #爬出的网站入口地址

    def parse(self, response):
        list_imgs = response.xpath('//div[@class="sidebar-layout-container"]//ul[@class="main-column-container"]//li')
        if list_imgs:
            # 循环条目  
            for item in list_imgs:
                pixiv_item = PixivItem()
                # 数据的xpath路劲解析
                str_item = item.xpath('.//a//div[@class="_thumbnail"]//@style').extract_first()
                if str_item: # 过滤为空或null的url地址
                   url_item = re.findall('\((.*?)\)', str_item)[0]  # 过滤后获取()中的url地址    
                   pixiv_item['image_urls'] = url_item
                   yield pixiv_item                  
        pass
