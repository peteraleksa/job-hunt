# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class JobhuntItem(Item):
	# define the fields for your item here like:
    # name = Field()
    pass

class CLJobPostItem(Item):
    title = Field()
    posted = Field()
    keywords = Field()
    original_post_link = Field()
    location = Field()
    job_title = Field()
    address = Field()
    map_link = Field()
    compensation = Field()
    skills = Field()
    experience = Field()
    tokenized_text = Field()
    text = Field()

class CLJobLinkItem(Item):
	text = Field()
	link = Field()