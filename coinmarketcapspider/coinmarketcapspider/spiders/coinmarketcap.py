import scrapy
from scrapy.spiders import CrawlSpider , Rule
from scrapy.linkextractors import LinkExtractor

from coinmarketcapspider.items import DoaminItem


class CoinmarketcapSpider(CrawlSpider):
    name = 'coinmarketcap'
    allowed_domains = ['coinmarketcap.com']
    start_urls = ['https://coinmarketcap.com/']

    rules = [

        Rule(LinkExtractor(allow='/?page=\d+'),follow=True),
        Rule(LinkExtractor(restrict_xpaths="//table/tbody",allow='/currencies/\w+/'),callback='parse_items')

    ]

    def parse_items(self, response):
        domain=response.selector.xpath("//a[@class='link-button']/@href").extract()
        item=DoaminItem()
        item["url"]=domain
        yield item
