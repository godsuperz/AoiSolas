# -*- coding: utf-8 -*-

"""
项目描述：《Scrapy采花大盗小爬虫》：本scrapy爬虫，教大家爬取整个妹纸网站，妹纸4000多，图片10W多，合计10G多数据量……
运行环境：win7 64 + python3.6 + scrapy1.4
运行方式：进入AoiSolas目录（scrapy.cfg所在目录)输入：

scrapy crawl AoiSola

代码详解：http://www.scrapyd.cn/example/176.html;
创建时间：2018年4月20日22:23:19
创建者：scrapy中文网（http://www.scrapyd.cn）；
"""
import base64


class AoisolasSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    def process_request(self, request, spider):
        """
        设置headers和切换请求头
        """
        referer = request.url
        if referer:
            request.headers['referer'] = referer


# 代理服务器
proxyServer = 'http-cla.abuyun.com:9030'

# 代理隧道验证信息
proxyUser = "HXU6KRZSR9S226BC"
proxyPass = "17CAC8FCE2CBD95D"

proxyAuth = "Basic " + base64.urlsafe_b64encode(bytes((proxyUser + ":" + proxyPass), "ascii")).decode("utf8")


class my_proxy(object):
    def process_request(self, request, spider):
        request.meta['proxy'] = proxyServer
        request.headers["Proxy-Authorization"] = proxyAuth
