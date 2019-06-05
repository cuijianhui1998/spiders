import sys,os
from scrapy.cmdline import execute


sys.path.append(os.path.dirname(os.path.abspath(__file__)))
#print(os.path.dirname(os.path.abspath(__file__)))

#启动scrapy项目
execute(['scrapy','crawl','hero'])