# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from sqlalchemy.orm import sessionmaker
from bbb.models import House, engine
class BbbPipeline(object):
	def process_item(self, item, spider):
		self.session.add(House(**item))
		return item
	
	def open_spider(self, spider):
		Session = sessionmaker(bind = engine)
		self.session = Session()
	
	def close_spider(self, spider):
		self.session.commit()
		self.session.close()
