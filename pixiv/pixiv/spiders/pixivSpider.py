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




# 京东爬虫（有的内容爬取不到）
# class PixivspiderSpider(scrapy.Spider):
#     name = 'pixivSpider' #爬虫的名字
#     allowed_domains = ['search.jd.com'] #允许的域名
#     start_urls = ['https://search.jd.com/Search?keyword=自營&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=自營&stock=1&wtype=1&page=2&s=628&click=1/'] #爬出的网站入口地址

#     def parse(self, response):
#         list_imgs = response.xpath("//div[@id='J_goodsList']//ul//li")
#         if list_imgs:
#             # 循环条目  
#             for item in list_imgs:
#                 pixiv_item = PixivItem()
#                 # 数据的xpath路劲解析
#                 pixiv_item['title'] = item.xpath(".//div//a//em/text()").extract_first()
#                 pixiv_item['price'] = item.xpath(".//div[@class='p-price']//i//text()").extract_first()
#                 pixiv_item['link'] = item.xpath(".//div//a//@href").extract_first()
#                 pixiv_item['image_urls'] = item.xpath(".//div[@class='gl-i-wrap']//img//@src").extract_first()
#                 # print(pixiv_item['image_urls'],'-------------')
#                 if pixiv_item['image_urls']:
#                     yield pixiv_item                                    
#         pass
