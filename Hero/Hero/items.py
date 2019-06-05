# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# 英雄基本信息
# class HeroItem(scrapy.Item):
#     # define the fields for your item here like:
#     id = scrapy.Field()
#     url = scrapy.Field()
#     hero_name = scrapy.Field()
#     title = scrapy.Field()
#     tags = scrapy.Field()
#     skins_count = scrapy.Field()
#     info = scrapy.Field()
#     lore = scrapy.Field()
#     allytips = scrapy.Field()
#     enemytips = scrapy.Field()
#     version = scrapy.Field()
#     updated = scrapy.Field()

# 这里是英雄皮肤的数据
# class HeroSkinsItem(scrapy.Item):
#     skin_id = scrapy.Field()
#     skin_name = scrapy.Field()
#     skin_image = scrapy.Field()



# #英雄技能
class HeroSpellsItem(scrapy.Item):
    id = scrapy.Field()
    hero_name = scrapy.Field()
    passive_name = scrapy.Field()
    # passive_description = scrapy.Field()
    passive_image = scrapy.Field()
    Q_name = scrapy.Field()
    # Q_description = scrapy.Field()
    # Q_CD = scrapy.Field()
    # Q_damage_value = scrapy.Field()
    # Q_power = scrapy.Field()
    Q_image = scrapy.Field()
    W_name = scrapy.Field()
    # W_description = scrapy.Field()
    # W_CD = scrapy.Field()
    # W_damage_value = scrapy.Field()
    # W_power = scrapy.Field()
    W_image = scrapy.Field()
    E_name = scrapy.Field()
    # E_description = scrapy.Field()
    # E_CD = scrapy.Field()
    # E_damage_value = scrapy.Field()
    # E_power  = scrapy.Field()
    E_image = scrapy.Field()
    R_name = scrapy.Field()
    # R_description = scrapy.Field()
    # R_CD = scrapy.Field()
    # R_damage_value = scrapy.Field()
    # R_power = scrapy.Field()
    R_image = scrapy.Field()