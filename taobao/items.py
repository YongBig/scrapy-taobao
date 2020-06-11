# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TaobaoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # define the fields for your item here like:
    search_criteria = scrapy.Field()
    price = scrapy.Field()
    sales = scrapy.Field()
    title = scrapy.Field()
    nick = scrapy.Field()
    loc = scrapy.Field()
    detail_url = scrapy.Field()
    nid = scrapy.Field()
    sellerid = scrapy.Field()
