# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from sqlalchemy.orm import sessionmaker
from models import JobPost, db_connect, create_job_post_table, create_keyword_table, create_job_keyword_table
from processor import PostProcessor

class JobhuntPipeline(object):
	def __init__(self):
		"""
		Initializes db connection and session maker
		Creates jobPost table
		"""
		engine = db_connect()
		create_job_post_table(engine)
		create_keyword_table(engine)
		create_job_keyword_table(engine)
		self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
    	""" process and save job post in the db
    		called for every item in the pipeline
    	"""
    	session = self.Session()
    	post = JobPost(**item)

    	pp = PostProcessor()
    	keywords = pp.extract_keywords(item)

    	try:
    		pid = session.add(post)
    		session.commit()

    		try:
    			for keyword in keywords:
    				# add to keyword table
    				# need to check for previously found keywords
    				k = Keyword(**keyword)
    				kid = session.add(k)
    				
    				# add job keyword relationship
    				post_keyword = JobKeyword()
    				post_keyword.word_id = kid
    				post_keyword.post_id = pid
    				session.add(post_keyword)
    	except:
    		session.rollback()
    		raise
    	finally:
    		session.close()

        return item
        