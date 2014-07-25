from __future__ import division

from time import sleep

import scrapy
import json
from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from scrapy.http import Request
from scrapy.shell import inspect_response

from jobhunt.items import CLJobLinkItem, CLJobPostItem

import nltk, re, pprint

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

	post_urls = []

	# parses a craigslist listing page
	def parse(self, response):
		
		# ToDo: move these into a settings file for dynamic generation
		base_domain = 'http://newyork.craigslist.org'
		#skills = ['java', 'c#', 'android', 'php']
		#strike = ['senior', 'lead', 'principal', 'unpaid']

		selector = Selector(response=response)

		links = [] 

		#with open('posts.json', 'r') as infile:                                                                     
		#	for line in infile:                                                             
		#		json_data = json.loads(line)
		#		links.append(json_data['original_post_link'])

		count = 0
		
		for sel in selector.xpath('//p[@class="row"]'):

			link = base_domain + ''.join(sel.xpath('span/span[2]/a/@href').extract())

			if link in links:
				print 'skipping previously found link...'
				continue

			item = CLJobLinkItem()
			item['text'] = sel.xpath('span/span[2]/a/text()').extract()
			
# move filtering to django db query
#			words = set(w.lower() for w in item['text'][0].split())
#			suitable = False
#			for word in words:
#				if word in skills and word not in strike:
#					suitable = True
#			if suitable:
# end move filtering to django db query

			count += 1
			item['link'] = link
			yield Request(link, callback=self.post_parse)

		print 'Added ' + str(count) + ' new posts.'

	# parses a craigslist job post
	def post_parse(self, response):

# move to item pipeline
		def getKeywords(text, limit):
			common = open("common.txt").read().split('\n')
			word_dict = {}
			for word in text:
				if word not in common and word.isalnum() :
					if word not in word_dict:
						word_dict[word] = 1
					if word in word_dict:
						word_dict[word] += 1
			top_words = sorted(word_dict.items(), key=lambda(k,v):(v,k), reverse=True)[0:limit]
			top = []
			for w in top_words:
				top.append(w[0])
			return top
# end move to item pipeline

		selector = Selector(response=response)

		post = selector.xpath('//section["@class=body"]')

		#inspect_response(response)

		item = CLJobPostItem()
		item['title'] = post.xpath('h2/text()').extract()
		item['posted'] = post.xpath('section[1]/p/time/text()').extract()
		item['original_post_link'] = response.url
		#item['address'] = post.xpath('section["@class=mapaddress"]/text()').extract()
		item['text'] = post.xpath('//*[@id="postingbody"]/text()').extract()
		
# move to item pipeline		
		paragraphs = []
		tokenized_text = []

		for paragraph in item['text']:
			paragraphs.append(str(paragraph.encode('ascii', 'ignore')))

		# print paragraphs
		# sleep(1)

		for p in paragraphs:
			tokenized_text.extend(nltk.word_tokenize(p))

		item['tokenized_text'] = tokenized_text
		#item['keywords'] = getKeywords(tokenized_text, 4)
# end move to pipeline
		sleep(2)
		yield item
