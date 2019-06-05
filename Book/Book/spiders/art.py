# -*- coding: utf-8 -*-
import scrapy


class ArtSpider(scrapy.Spider):
    name = 'art'
    allowed_domains = ['http://book.dangdang.com/01.05.htm?ref=book-01-A']
    start_urls = ['http://book.dangdang.com/01.05.htm?ref=book-01-A']

    def parse(self, response):
        pass
