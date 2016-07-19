# -*- coding: utf-8 -*-
import scrapy
from crab_soccer.items import Article

from utils import extract

class SoccbaiduSpider(scrapy.Spider):
    name = "soccBaidu"
    allowed_domains = ["news.baidu.com"]
    start_urls = ['http://news.baidu.com/n?cmd=%d&class=%s&tn=rss' %(cmd,clazz) for cmd in[1,4] for clazz in['worldsoccer','chinasoccer']]

    def parse(self, response):
        xxs= scrapy.Selector(response)
        source="baidu_"+extract(xxs.xpath('//channel/title/text()'))
        for xItem in xxs.xpath('//item'):
            item=Article()
            item['source']=source
            item['title']=extract( xItem.xpath('./title/text()'))
            item['link']= extract(xItem.xpath('./link/text()'))
            item['desc']= extract(xItem.xpath('./description/text()'))
            item['pubDate']= extract(xItem.xpath('./pubDate/text()'))
            yield item
        
