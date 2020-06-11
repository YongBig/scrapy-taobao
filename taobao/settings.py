# -*- coding: utf-8 -*-

# Scrapy settings for taobao project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'taobao'

SPIDER_MODULES = ['taobao.spiders']
NEWSPIDER_MODULE = 'taobao.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'taobao (+http://www.yourdomain.com)'

# Obey robots.txt rules
#ROBOTSTXT_OBEY = True
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False
COOKIES_ENABLED = False
# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'Accept-Language': 'zh,en;q=0.9,zh-CN;q=0.8',
  'cookie': 'thw=cn; hng=CN%7Czh-CN%7CCNY%7C156; OUTFOX_SEARCH_USER_ID_NCOO=2025860937.8947263; enc=Cw4hu001HPyoAg4XciEYzoOoL4qIE9Q1IKJ5jk2lZHum%2FfFvmNXnM1UZ8jXhlS%2BhpLZgyJ%2BhtyWRhLHMgXk4XQ%3D%3D; UM_distinctid=1709f08f4b1411-04feb7493c4527-6a547d2e-1fa400-1709f08f4b2a4a; Hm_lvt_eaa57ca47dacb4ad4f5a257001a3457c=1584328853,1584329889; _fbp=fb.1.1589348457426.376849931; _samesite_flag_=true; cookie2=14270b49bd811abc6b773d4a481f25c6; t=8f3cb0d63aa9ff36fbf9e274eb3782c8; _tb_token_=e33a384fbb3e5; _m_h5_tk=8ba742064c405d3116d78e8310c3e073_1591787987236; _m_h5_tk_enc=d13f20202d3c30f5ce1a24e26a571be4; sgcookie=EIFJGOB9qd%2FuCUotW00TR; tracknick=; cna=zWrvFtMe92YCAdpeXz59Bv1z; v=0; tfstk=cJ1fBFTAkmmfx52ZgZayQ4Zsm3OOZG0B5-tclTXW8sJnsnbfiwheAUucIchJpU1..; mt=ci=-1_0; uc1=cookie14=UoTV7X3Ws1EHfQ%3D%3D; JSESSIONID=F9A0E5670BC55C06A0B7EF1A69D2B1FF; alitrackid=world.taobao.com; lastalitrackid=world.taobao.com; l=eBILXcc7qZk4KGisBO5CFurza77TuIRb8sPzaNbMiInca6HO9Eex9NQDDy2eWdtj_tffDetPOzL1BRhW7Fadg2HvCbKrCyCl-xJ6-; isg=BN7eZM7rDOn7AFsvh-gGypzjL3Qgn6IZxJqAiohn1iFSq3-F8CwIKRsJo7-nk5ox'
}
# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'taobao.middlewares.TaobaoSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'taobao.middlewares.TaobaoDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'taobao.pipelines.TaobaoPipeline': 300,
#}
ITEM_PIPELINES = {
   'taobao.pipelines.TaobaoPipeline': 300,
}
# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
