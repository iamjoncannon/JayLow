# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class JaylowSpider(scrapy.Spider):
	name = 'JayLow'
	allowed_domains = ['beyondbeautifuljlo.com']
	start_urls = ['http://www.beyondbeautifuljlo.com/gallery']

	def parse(self, response):

		images = response.css('img::attr(src)').getall()

		for item in images:

			if item.startswith('http') == False:
				item = response.urljoin(item)

			returned = { 'image_urls': [item]}
			yield returned 

		aTags = response.css('a::attr(href)').getall()

		if aTags is not None:
			for a in aTags:
				a = response.urljoin(a)
				yield scrapy.Request(a, self.parse)