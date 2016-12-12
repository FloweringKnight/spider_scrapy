# -*- coding:utf-8 -*-

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from spider.items import MininovaItem


class MininovaSpider(CrawlSpider):
    name = 'Mininova'
    allowed_domains = ['mininova.org']
    start_urls = ['http://www.mininova.org/yesterday']
    rules = [Rule(LinkExtractor(allow=[r'/tor/\d+']), callback='parse_mininova')]

    def parse_mininova(self, response):
        torrent = MininovaItem()
        torrent['url'] = response.url
        torrent['name'] = response.xpath('//h1/text()').extract()
        torrent['description'] = response.xpath('//div[@id="description"]/text()').extract()
        torrent['size'] = response.xpath('//div[@id="specifications"]/p[2]/text()[2]').extract()
        return torrent
