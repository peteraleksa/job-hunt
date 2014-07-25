# Scrapy settings for jobhunt project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

SPIDER_MODULES = ['jobhunt.spiders']
NEWSPIDER_MODULE = 'jobhunt.spiders'

FEED_FORMAT = 'json'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'jobhunt (+http://www.yourdomain.com)'
