# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class JaylowSpider(scrapy.Spider):
	name = 'JayLow'

	# allowed_domains = ['beyondbeautifuljlo.com']
	# allowed_domains = ['jlospain.net/']
	# start_urls = ['http://www.beyondbeautifuljlo.com/gallery', 'https://www.beyondbeautifuljlo.com/category/photos/']
	# start_urls = ['https://www.beyondbeautifuljlo.com/category/photos/']
	# start_urls = ['http://jlospain.net/']
	# allowed_domains = ['alamy.com/']
	# start_urls = ['https://www.alamy.com/stock-photo/enough-jennifer-lopez.html']
	allowed_domains = ['jenniferlopez.pl']
	start_urls = ['http://jenniferlopez.pl/galeria']

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