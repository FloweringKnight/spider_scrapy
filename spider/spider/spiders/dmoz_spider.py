# -*- coding: utf-8 -*-

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import  LinkExtractor
from spider.items import DmozItem


class DomzSpider(CrawlSpider):
    name = 'Dmoz'
    allowed_domains = ['dmoz.org']
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]
    rules = [Rule(LinkExtractor(r''), callback='parse_dmoz')]

    def parse_dmoz(self, response):
        neirong = DmozItem()
        for sel in response.xpath('//div[@class="site-item "]'):
            neirong['title'] = sel.xpath('//div[@class="site-title"]/text()').extract()
            neirong['link'] = sel.xpath('//a[@target="_blank"]/@href').extract()
            neirong['desc'] = sel.xpath('//div[@class="site-descr "]/text()').extract()
        return neirong
