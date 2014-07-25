# Scrapy settings for jobhunt project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

SPIDER_MODULES = ['jobhunt.spiders']
NEWSPIDER_MODULE = 'jobhunt.spiders'

DOWNLOAD_DELAY = 2
CONCURRENT_REQUESTS_PER_DOMAIN = 4

MONGODB_URI = 'mongodb://localhost:27017'
MONGODB_DATABASE = 'jobHunt'
MONGODB_COLLECTION = 'jobPosts'
#MONGODB_UNIQUE_KEY = 'postId'

ITEM_PIPELINES = [
	'scrapy_mongodb.MongoDBPipeline'
]

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'jobhunt (+http://www.yourdomain.com)'
