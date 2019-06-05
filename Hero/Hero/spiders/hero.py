# -*- coding: utf-8 -*-
import scrapy,json,requests,re
from scrapy import Request
from Hero.items import HeroSpellsItem
#from Hero.items import HeroItem,HeroSkinsItem


class HeroSpider(scrapy.Spider):
    name = 'hero'
    allowed_domains = ['http://lol.qq.com/data/info-heros.shtml']
    start_urls = ['http://lol.qq.com/biz/hero/champion.js',]



    def parse(self, response):

        all_hero = requests.get(self.start_urls[0])
        all_hero.encoding = 'utf-8'
        hero_data = json.loads(all_hero.text.replace('if(!LOLherojs)var LOLherojs={};LOLherojs.champion=','')[:-1])
        hero_list = hero_data['keys']
        for key,value in hero_list.items():
            one_hero_url = 'http://lol.qq.com/biz/hero/'+value+'.js'
            yield Request(url=one_hero_url,callback=self.parse_detail,dont_filter=True,meta={'hero_name':value})

    def parse_detail(self,response):
        data = json.loads(response.text.replace(('if(!LOLherojs)var LOLherojs={champion:{}};LOLherojs.champion.'+response.meta.get('hero_name')+'='),'')[:-1].encode('utf-8'))
        id = data['data']['key']
        url = response.url
        hero_name = data['data']['name']
        title = data['data']['title']
        tags = ','.join(data['data']['tags'])
        skins_count = len(data['data']['skins'])-1
        info = ','.join('%s' %id for id in self.info_deal(data['data']['info'])) #关于英雄的上手难度,返回的是一个字典
        lore = self.description_deal(data['data']['lore'])  # 背景故事
        allytips = ','.join(self.allytips_deal(data['data']['allytips'] )) # 你在使用英雄时的技巧,返回的是一个列表
        enemytips = ','.join(self.allytips_deal(data['data']['enemytips']))  # 你在面对这个英雄时的技巧,返回的是一个列表
        version = data['version']
        updated = data['updated']
        #
        skins_name = [skin['name'] for skin in data['data']['skins'][1:]]
        skins_id = [skin['id'] for skin in data['data']['skins'][1:]]
        skins_images = [('http://ossweb-img.qq.com/images/lol/web201310/skin/big'+skin+'.jpg') for skin in skins_id]
        skins = self.skins_deal(skins_name,skins_id,skins_images)

        spells = {
            'Q':{
                'id': data['data']['spells'][0]['id'],
                'name':data['data']['spells'][0]['name'],
                'description':self.description_deal(data['data']['spells'][0]['tooltip']),
                'CD':self.CD_deal(data['data']['spells'][0]),
                'damage_value':self.damage_deal(data['data']['spells'][0]),
                'power':self.power_deal(data['data']['spells'][0]),
                'image':'//ossweb-img.qq.com/images/lol/img/spell/' + data['data']['spells'][0]['image']['full']
            },
            'W':{
                'id': data['data']['spells'][1]['id'],
                'name': data['data']['spells'][1]['name'],
                'description': self.description_deal(data['data']['spells'][1]['tooltip']),
                'CD': self.CD_deal(data['data']['spells'][1]),
                'damage_value': self.damage_deal(data['data']['spells'][1]),
                'power':self.power_deal(data['data']['spells'][1]),
                'image': '//ossweb-img.qq.com/images/lol/img/spell/' + data['data']['spells'][1]['image']['full']
            },
            'E':{
                'id': data['data']['spells'][2]['id'],
                'name': data['data']['spells'][2]['name'],
                'description': self.description_deal(data['data']['spells'][2]['tooltip']),
                'CD': self.CD_deal(data['data']['spells'][2]),
                'damage_value': self.damage_deal(data['data']['spells'][2]),
                'power': self.power_deal(data['data']['spells'][2]),
                'image': '//ossweb-img.qq.com/images/lol/img/spell/' + data['data']['spells'][2]['image']['full']
            },
            'R':{
                'id': data['data']['spells'][3]['id'],
                'name': data['data']['spells'][3]['name'],
                'description': self.description_deal(data['data']['spells'][3]['tooltip']),
                'CD': self.CD_deal(data['data']['spells'][3]),
                'damage_value': self.damage_deal(data['data']['spells'][3]),
                'power': self.power_deal(data['data']['spells'][3]),
                'image': '//ossweb-img.qq.com/images/lol/img/spell/' + data['data']['spells'][3]['image']['full']
            }
        }
        passive = {
            'name': data['data']['passive']['name'],
            'description': self.description_deal(data['data']['passive']['description']),
            'image': '//ossweb-img.qq.com/images/lol/img/passive/' + data['data']['passive']['image']['full']
        }#被动


        # hero = HeroItem()
        #hero_skins = HeroSkinsItem()
        hero_spells = HeroSpellsItem()
        #
        # hero['id'] = id
        # hero['url'] = url
        # hero['hero_name'] = hero_name
        # hero['title'] = title
        # hero['tags'] = tags
        # hero['skins_count'] = skins_count
        # hero['info'] = info
        # hero['lore'] = lore
        # hero['allytips'] = allytips
        # hero['enemytips'] = enemytips
        # hero['version'] = version
        # hero['updated'] = updated

        # yield hero

        #皮肤
           # for elem in skins:
        #     hero_skins['skin_name'] = elem['name']
        #     hero_skins['skin_id'] = elem['id']
        #     hero_skins['skin_image'] = elem['skins_image']
        #     yield hero_skins

        #技能
        hero_spells['id'] = id
        hero_spells['hero_name'] = hero_name

        hero_spells['passive_name'] = passive['name']
        # hero_spells['passive_description'] = passive['description']
        hero_spells['passive_image'] = passive['image']

        hero_spells['Q_name'] = spells['Q']['name']
        # hero_spells['Q_description'] = spells['Q']['description']
        # hero_spells['Q_CD'] = spells['Q']['CD']
        # hero_spells['Q_damage_value'] = spells['Q']['damage_value']
        # hero_spells['Q_power'] = spells['Q']['power']
        hero_spells['Q_image'] = spells['Q']['image']

        hero_spells['W_name'] = spells['W']['name']
        # hero_spells['W_description'] = spells['W']['description']
        # hero_spells['W_CD'] = spells['W']['CD']
        # hero_spells['W_damage_value'] = spells['W']['damage_value']
        # hero_spells['W_power'] = spells['W']['power']
        hero_spells['W_image'] = spells['W']['image']

        hero_spells['E_name'] = spells['E']['name']
        # hero_spells['E_description'] = spells['E']['description']
        # hero_spells['E_CD'] = spells['E']['CD']
        # hero_spells['E_damage_value'] = spells['E']['damage_value']
        # hero_spells['E_power'] = spells['E']['power']
        hero_spells['E_image'] = spells['E']['image']

        hero_spells['R_name'] = spells['R']['name']
        # hero_spells['R_description'] = spells['R']['description']
        # hero_spells['R_CD'] = spells['R']['CD']
        # hero_spells['R_damage_value'] = spells['R']['damage_value']
        # hero_spells['R_power'] = spells['R']['power']
        hero_spells['R_image'] = spells['R']['image']

        yield hero_spells






    def description_deal(self,data):
        a = re.match('.*(<.*>).*(<.*>).*', data)
        if a:
            result = data.replace(a.group(1),'').replace(a.group(2),'')
            return result
        return data
    def skins_deal(self,x,y,z):
        skins = []
        for name, id, skins_image in zip(x, y, z):
            skins.append({
                'name': name,
                'id': id,
                'skins_image': skins_image
            })
        return skins
    def allytips_deal(self,data):
        result = [elem.replace('-','').replace(' ','').replace('【','').replace('】','').replace('\n','') for elem in data]
        return result
    def info_deal(self,data):
        values = []
        for value in data.values():
            values.append(value)
        return values
    def CD_deal(self,data):
        try:
            return data['leveltip']['effect'][1]
        except:
            return '无CD'
    def power_deal(self,data):
        try:
            return data['resource']
        except:
            return '无消耗'

    def damage_deal(self,data):
        try:
            return data['leveltip']['effect'][0]
        except:
            return '无消耗'







