# -*- coding: utf-8 -*-
import scrapy
from bbb.items import HouseItem

class HouseSpider(scrapy.Spider):
	name = 'house'
	@property
	def start_urls(self):
		url_temp = 'https://xa.anjuke.com/sale//'
		return(url_temp.format (i) for i in range(1,10))

	def parse(self, response):
		for a in response.css("div#house-details"):
			item = HouseItem({
				'name': a.css('div#house-title a ::text').extract(),
				'size': a.css('div#house-item span ::text').extract(),
				'addr': a.css('div#house-item span#comm-address ::text').extract(),
				'describe': a.css('div#tags-bottom span ::text').extract(),
				'price': a.css('div#pro-price span ::text').extract()
				})
			yield item
