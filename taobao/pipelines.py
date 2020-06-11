# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

class TaobaoPipeline(object):
    def process_item(self, item, spider):
        print("*"*25)
        self.q.update({'nid': item['nid']}, {'$set': dict(item)}, True)
        return item

    def open_spider(self, spider):
        client = pymongo.MongoClient("mongodb://root:123456@127.0.0.1:27017/")
        db = client['taobao']
        self.q = db['product']