from __future__ import division
from time import sleep

import scrapy
from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from scrapy.http import Request
from scrapy.shell import inspect_response
from scrapy.contrib.loader import ItemLoader

from jobhunt.items import CLJobLinkItem, CLJobPostItem

class CraigslistSpider(Spider):
	name = "craigslist"
	allowed_domains = ["craigslist.org"]
	start_urls = [
		"http://newyork.craigslist.org/eng/",
		"http://newyork.craigslist.org/sof/",
		"http://newyork.craigslist.org/sad/",
		"http://newyork.craigslist.org/web/",
		"http://newyork.craigslist.org/cpg/"
	]

	def parse(self, response):
		""" parses a craigslist listing page """
		base_domain = 'http://newyork.craigslist.org'
		selector = Selector(response=response)
		count = 0
		
		for sel in selector.xpath('//p[@class="row"]'):

			link = base_domain + ''.join(sel.xpath('span/span[2]/a/@href').extract())

			item = CLJobLinkItem()
			item['text'] = sel.xpath('span/span[2]/a/text()').extract()
			item['link'] = link

			count += 1

			yield Request(link, callback=self.post_parse)

		print 'Added ' + str(count) + ' new posts.'

	def post_parse(self, response):
		""" parses a craigslist job post """
		#inspect_response(response)
		selector = Selector(response=response)
		post = selector.xpath('//section["@class=body"]')

		item = ItemLoader(item='CLJobPostItem', response=response)
		item.add_xpath('title', '//section["@class=body"]h2/text()')
		item.add_xpath('posted','//section["@class=body"]/section[1]/p/time/text()'
		item.add_value('original_post_link', response.url)
		#item['address'] = post.xpath('section["@class=mapaddress"]/text()').extract()
		item.add_xpath('text', '//*[@id="postingbody"]/text()')

		sleep(2)
		yield item.load_item()
