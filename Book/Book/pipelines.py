# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql,requests

class BookPipeline(object):
    def process_item(self, item, spider):
        return item

class MysqlPipeline:
    def __init__(self):
        self.conn = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='123456',
            db='wechat',
            charset='utf8',
            use_unicode=True
        )
        self.cursor = self.conn.cursor()
    def process_item(self,item,spider):

        search_sql = "select isbn from book where isbn=%s"
        self.cursor.execute(search_sql,item['isbn'])
        if not self.cursor.fetchone():
            insert_sql = '''insert into book(isbn,title,author,pubdate,publisher,types,description,image_url) 
            VALUES(%s,%s,%s,%s,%s,%s,%s,%s)
            '''
            self.cursor.execute(insert_sql,(item['isbn'],item['title'],item['author'],item['pubdate'],item['publisher'],'story',item['description'],item['image_url']))
            self.conn.commit()
        # with open('D:\BookImages\storyimg\{}.jpg'.format(item['isbn']),'wb') as f:
        #     result = requests.get(item['image_url'])
        #     f.write(result.content)


