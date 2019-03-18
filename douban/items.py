# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
# 此文件中是需要爬虫爬取的目标

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 电影的序号
    serial_number = scrapy.Field()
    # 电影的名称
    moive_name = scrapy.Field()
    # 电影的介绍
    introduce = scrapy.Field()
    # 电影的评论数
    comment_num = scrapy.Field()
    # 电影的评分
    evaluate = scrapy.Field()
    # 电影的描述
    descript = scrapy.Field()
    # 电影的封面
    cover = scrapy.Field()
    image_paths = scrapy.Field()
    images = scrapy.Field()
    pass
