# -*- coding: utf-8 -*-
import scrapy
from taobao.items import TaobaoItem
from urllib.parse import quote
import json
class TaobaoSpider(scrapy.Spider):
    # 设置name
    name = "taobao"
    Quote = input('请输入要搜索的商品名>>>')
    allowed_domains = ['s.taobao.com','taobao.com','passport.alibaba.com']
    total_page = int(input('请输入爬取页数>>>'))
    start_urls = []
    for i in range(total_page):
        start_urls.append("https://s.taobao.com/search?q={}&ie=utf8&s={}".format(quote(Quote,'utf-8'),i*44))
    str1 = '\r\n'.join(start_urls)
    print("爬虫网站地址：{}".format(str1))

    def parse(self, response):
        self.logger.info("*"*50)
        # g_page_config 为获取商品信息
        p = 'g_page_config = ({.*?});'
        g_page_config = response.selector.re(p)[0]
        g_page_config = json.loads(g_page_config)
        auctions = g_page_config['mods']['itemlist']['data']['auctions']
        for auction in auctions:
            item = TaobaoItem()
            item['search_criteria'] = self.Quote
            item['price'] = auction['view_price']
            item['sales'] = auction['view_sales']
            item['title'] = auction['raw_title']
            item['nick'] = auction['nick']
            item['loc'] = auction['item_loc']
            item['detail_url'] = auction['detail_url']
            item['nid'] = auction['nid']
            item['sellerid'] = auction['user_id']
            yield item