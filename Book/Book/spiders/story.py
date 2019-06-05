# -*- coding: utf-8 -*-
import scrapy,re
from scrapy import Request
from Book.items import BookItem

class StorySpider(scrapy.Spider):
    name = 'story'
    allowed_domains = ['http://book.dangdang.com/01.03.htm?ref=book-01-A']
    start_urls = ['http://book.dangdang.com/01.03.htm?ref=book-01-A']

    def parse(self, response):
        book_urls = response.xpath("//ul[@class='product_ul']/li/a/@href").extract()
        with open('D:\BookImages\imagesUrl\story_url.txt','w') as f:
            for url in book_urls:
                f.writelines(url+'\n')
        headers = {}
        for book in book_urls:
            yield Request(url=book,callback=self.detail_parse,headers=headers,dont_filter=True)
    def detail_parse(self,response):
        image_url = response.xpath("//img[@id='largePic']/@src").extract_first()
        title = response.xpath("//div[@class='name_info']/h1[1]/@title").extract_first()
        author = self._author(response.xpath("//span[@id='author']/a[1]/text()").extract())
        publisher = response.xpath("//div[@class='messbox_info']/span[2]/a[1]/text()").extract_first()
        pubdate = self._pubdate(response.xpath("//div[@class='messbox_info']/span[3]/text()").extract_first())
        isbn = self._isbn(response.xpath("//ul[@class='key clearfix']/li[5]/text()").extract_first())
        types = ','.join(response.xpath("//span[@class='lie']/a/text()").extract()[1:])
        description = self._description(response.xpath("//div[@class='name_info']/h2/span[1]/text()").extract_first())

        book = BookItem()
        book['title'] = title
        book['description'] = description
        book['isbn'] = isbn
        book['image_url'] = image_url
        book['types'] = types
        book['author'] = author
        book['publisher'] = publisher
        book['pubdate'] = pubdate

        yield book


    def _author(self,author):
        return ','.join(author)
    def _pubdate(self,pubdate):
        exep = r'.*([0-9]{4}).*([0-9]{2}).*'
        result = re.match(exep,pubdate)
        date = '{}-{}'.format(result.group(1),result.group(2))
        return date
    def _isbn(self,isbn):
        exep = r'.*?([0-9]{10,13}).*'
        result = re.match(exep,isbn)
        isbn = result.group(1)
        return isbn
    def _description(self,description):
        return ','.join(description.split())


