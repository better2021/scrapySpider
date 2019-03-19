# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy import Request

class PixivPipeline(object):
    def process_item(self, item, spider):
        return item

# 定制图片管道
class MyImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for image_url in [item['image_urls']]: # 数组循环
            # print(image_url,'---------')
            yield Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        print(results,'-------')
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item