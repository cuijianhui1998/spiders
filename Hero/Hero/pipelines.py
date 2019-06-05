# -*- coding: utf-8 -*-
import pymysql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class HeroPipeline(object):
    def process_item(self, item, spider):
        return item

class MysqlTwistedPipeline:
    def __init__(self):
        self.conn = pymysql.connect(
            host = 'localhost',
            user = 'root',
            password = '123456',
            port = 3306,
            db = 'spider',
            charset='utf8',
            use_unicode=True
        )
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        #将数据存入数据库,如果已经存在,就不再进行存储,这里没有一个好的主键识别唯一性,勉强用title
        # search_sql = 'select id from hero_spells where id=%s'
        # self.cursor.execute(search_sql,item['id'])
        # if not self.cursor.fetchone():

            #这是英雄基础信息的插入
            # insert_sql = """
            #     insert into hero(id,url,hero_name,title,tags,skins_count,info,lore,allytips,enemytips,version,updated)
            #     VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            # """
            # self.cursor.execute(insert_sql, (item['id'], item['url'], item['hero_name'],item['title'],
            #                                  item['tags'],item['skins_count'],item['info'],item['lore'],
            #                                  item['allytips'], item['enemytips'],item['version'],item['updated'])
            #                     )

            # 这里是英雄皮肤的插入
            # insert_sql = """
            #                 insert into hero_skins(skin_id,skin_name,skin_image)
            #                 VALUES (%s,%s,%s)
            #             """
            # self.cursor.execute(insert_sql, (item['skin_id'], item['skin_name'], item['skin_image']))


            #这里是英雄技能的插入
            # insert_sql = """
            #                 insert into hero_spells(id,hero_name,passive_name,passive_description,passive_image,
            #                                             Q_name,Q_description,Q_CD,Q_damage_value,Q_power,Q_image,
            #                                             W_name,W_description,W_CD,W_damage_value,W_power,W_image,
            #                                             E_name,E_description,E_CD,E_damage_value,E_power,E_image,
            #                                             R_name,R_description,R_CD,R_damage_value,R_power,R_image)
            #                 VALUES (%s,%s,%s,%s,%s,
            #                         %s,%s,%s,%s,%s,
            #                         %s,%s,%s,%s,%s,
            #                         %s,%s,%s,%s,%s,
            #                         %s,%s,%s,%s,%s,
            #                         %s,%s,%s,%s)
            #             """
            insert_sql = """
                                    insert into hero_spells(id,hero_name,passive_name,passive_image,Q_name,Q_image,
                                                              W_name,W_image,E_name,E_image,R_name,R_image)
                                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                                """
            self.cursor.execute(insert_sql, (item['id'],item['hero_name'],item['passive_name'],item['passive_image'],
                                            item['Q_name'],item['Q_image'],item['W_name'],item['W_image'],
                                            item['E_name'],item['E_image'],item['R_name'],item['R_image'])
                                )
            self.conn.commit()