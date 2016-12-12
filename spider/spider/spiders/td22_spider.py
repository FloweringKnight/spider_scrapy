# -*- coding: utf-8 -*-


from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from spider.items import Td22Item


class Td22Spider(CrawlSpider):
    name = 'Td22'
    allowed_domains = ['td22.com']
    start_urls = [
        'http://cjyx.td22.com/news-0-1.html'
    ]
    rules = [Rule(LinkExtractor(r'/newinfo\-\d+\.html'), callback='parse_td22')]

    def parse_td22(self, response):
        news = Td22Item()
        news['url'] = response.url
        news['news_title'] = response.xpath('//h1/text()').extract()
        news['news_body'] = response.xpath('//div[@class="nc_bottom"]').extract()
        return news
