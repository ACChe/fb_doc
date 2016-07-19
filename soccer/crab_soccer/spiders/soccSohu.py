# -*- coding: utf-8 -*-
import scrapy
from utils import extract
from crab_soccer.items import Article


types=['zhongguozuqiu','zhongguonanzu','zhongguonvzhu','zhongchao','guojizutan','ecup','yijia','ac'
       'youwendongtai','guomidongtai','yingchao','qieerxi','manlian','asenna','xijia','huangma','bacailona'
       'haiwaiqiuyuan','zucai'
       ]

class SoccsohuSpider(scrapy.Spider):
    name = "soccSohu"
    allowed_domains = ["rss.sports.sohu.com"]
    start_urls = ['http://rss.sports.sohu.com/rss/%s.xml' % 
                  type for type in types]

    def parse(self, response):
        xxs= scrapy.Selector(response)
        source="sohu_"+extract(xxs.xpath('//channel/title/text()'))
        for xItem in xxs.xpath('//item'):
            item=Article()
            item['source']=source
            item['title']=extract( xItem.xpath('./title/text()'))
            item['link']= extract(xItem.xpath('./link/text()'))
            item['desc']= extract(xItem.xpath('./description/text()'))
            item['pubDate']= extract(xItem.xpath('./pubDate/text()'))
            yield item
