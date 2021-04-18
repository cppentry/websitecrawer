# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
class CppentryPipeline(object):
    def process_item(self, item, spider):
        f=codecs.open("/home/github/websitecrawer/cppentry/html/"+item['title'],"wb",'utf-8') 
        f.write(item['content'])
        f.close()
        return item
