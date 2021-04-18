#coding=utf-8
import scrapy
from scrapy.linkextractors import LinkExtractor

from scrapy.http import Request
from ..items import *

class CppentrySpider(scrapy.Spider):
    name = 'Cppentry' 
    allowed_domains = ['cppentry.com']
    start_urls = ['https://www.cppentry.com']
    
 
    def parse(self, response):
        link = LinkExtractor(allow=r'bencandy')
        links = link.extract_links(response)
        for link in links:
            yield Request(link.url,callback=self.parse_item)
        
        
        
    def parse_item(self,response):
        item=CppentryItem()
        item['title']=response.xpath("//div[@class='main_title']/text()").extract()[0]
        item['content']=response.xpath("//table[@class='content']").extract()[0]
        item['srcurl']=response.url
        yield item