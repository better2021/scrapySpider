# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem

class DoubanSpiderSpider(scrapy.Spider):
    name = 'douban_spider'  # 爬虫的名字
    allowed_domains = ['movie.douban.com'] # 允许的域名
    start_urls = ['https://movie.douban.com/top250'] # 入口的url地址

    # 默认解析方法
    def parse(self, response):
        # print(response.text)
        moiveList = response.xpath("//div[@class='article']//ol[@class='grid_view']//li") 
        # 循环电影的条目
        for item in moiveList:
            douban_item = DoubanItem()
            # 写详细的xpath进行数据的解析
            douban_item['serial_number'] =  item.xpath(".//div[@class='item']//em/text()").extract_first()
            douban_item['moive_name'] = item.xpath(".//div[@class='info']//div[@class='hd']//a//span[1]/text()").extract_first()
            douban_item['introduce'] = item.xpath(".//div[@class='info']//div[@class='bd']//p[1]/text()").extract_first()
            douban_item['descript'] = item.xpath(".//div[@class='info']//div[@class='bd']//p[@class='quote']//span/text()").extract_first() 
            douban_item['evaluate'] = item.xpath(".//div[@class='bd']//div[@class='star']//span[@class='rating_num']/text()").extract_first()
            douban_item['comment_num'] = item.xpath(".//div[@class='bd']//div[@class='star']//span[4]/text()").extract_first()
            douban_item['cover'] = item.xpath(".//div[@class='item']//div[@class='pic']//a//img//@src").extract_first()
            print(douban_item)
            # 将数据yield到pipelines里面去，才能进行数据的存储操作
            yield douban_item

        # 解析下一页数据，取得后页的xpath
        next_link = response.xpath("//span[@class='next']/link/@href").extract()
        if next_link:
            next_link = next_link[0]
            yield scrapy.Request("https://movie.douban.com/top250"+next_link,callback=self.parse)    
        pass
