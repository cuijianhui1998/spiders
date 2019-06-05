# -*- coding: utf-8 -*-
import scrapy


class ItSpider(scrapy.Spider):
    name = 'it'
    allowed_domains = ['http://book.dangdang.com/01.54.htm?ref=book-01-A']
    start_urls = ['http://book.dangdang.com/01.54.htm?ref=book-01-A']

    def parse(self, response):
        pass
