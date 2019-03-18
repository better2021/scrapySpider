# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy import Request
from scrapy import log

class DoubanPipeline(object):
    def process_item(self, item, spider):
        return item    


# 获取图片的管道
class DoubanImgDownloadPipeline(ImagesPipeline):
    default_headers = {
        'accept': 'image/webp,image/*,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, sdch, br',
        'accept-language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'cookie': 'bid=yQdC/AzTaCw',
        'referer': 'https://www.douban.com/photos/photo/2370443040/',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    }

    def get_media_requests(self, item, info):
        for image_url in [item['cover']]:  # item['cover']的外面加上 []才会成为数组，才能去遍历
            self.default_headers['referer'] = image_url
            yield Request(image_url, headers=self.default_headers)

    def item_completed(self, results, item, info):
        #在這通過debug可以看到results裏數據,分下載圖片成功和下載失敗兩種情況.
        #如果下載成功results的結果：[(True, {'url': 'http://pics.sc.chinaz.com/Files/pic/icons128/7152/f1.png', 'path': '人物頭像圖標下載/f1.png', 'checksum': 'eb7f47737a062a1525457e451c41cc99'})]
        #True:代表圖片下載成功
        #url：圖片的地址
        #path:圖片的存儲路徑
        #checksum:圖片內容的 MD5 hash加密字符串
        #如果下載失敗results的結果:[(False, <twisted.python.failure.Failure scrapy.pipelines.files.FileException: 'NoneType' object has no attribute 'split'>)]
        #False:代表下載失敗
        print(results,'-------------')
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item