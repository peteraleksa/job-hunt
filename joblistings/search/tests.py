from django.core.urlresolvers import resolve
from django.template.loader import render_to_string
from django.test import TestCase
from django.http import HttpRequest
#from django.test.simple import DjangoTestSuiteRunner

from pymongo import Connection

from search.views import home_page, results_page

#from search.models import JobLink
from search.models import JobPost, Keyword, Skill, Experience
from search.models import JobKeyword, JobSkill, JobExperience

# Create your tests here.

class HomePageTest(TestCase):

	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)

	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = home_page(request)
		expected_html = render_to_string('home.html')
		self.assertEqual(response.content.decode(), expected_html)

	def test_results_page_can_receive_a_POST_request(self):
		request = HttpRequest()
		request.method = 'POST'
		request.POST['skillset'] = 'ninja'
		response = results_page(request)
		self.assertIn('ninja', response.content.decode())
		expected_html = render_to_string(
			'results.html',
			{'skillset': 'ninja'}
		)
		self.assertEqual(response.content.decode(), expected_html)

class DbConnectTest(TestCase):

	def test_database_connection(self):
		databaseName = 'jobHunt-dev'
		connection = Connection()

		db = connection[databaseName]
		job_posts = db['jobPosts']

		count = job_posts.count()

		self.assertIsNotNone(count)

# 	#def test_database_lookup(self):

class JobModelTest(TestCase):

	def test_saving_and_retrieving_job_posts(self):
		title = 'First Job'
		posted = '2014-07-22  5:21pm'
		#keywords = ['c#', 'java', 'python']
		original_post_link = 'http://localhost:8000'
		location = ''
		job_title = ''
		address = ''
		map_link = ''
		compensation = ''
		text = 'Some text about the job'

		first_job_post = JobPost()
		first_job_post.title = title
		first_job_post.original_post_link = original_post_link
		first_job_post.location = location
		first_job_post.job_title = job_title
		first_job_post.address = address
		first_job_post.map_link = map_link
		first_job_post.compensation = compensation
		first_job_post.text = text

		first_job_id = first_job_post.save()

		saved_job_posts = JobPost.objects.all()
		self.assertEqual(saved_job_posts.count(), 1)

		first_saved_job_post = saved_job_posts[0]

		self.assertEqual(first_saved_job_post.title, title)
		self.assertEqual(first_saved_job_post.original_post_link, original_post_link)
		self.assertEqual(first_saved_job_post.location, location)
		self.assertEqual(first_saved_job_post.job_title, job_title)
		self.assertEqual(first_saved_job_post.address, address)
		self.assertEqual(first_saved_job_post.map_link, map_link)
		self.assertEqual(first_saved_job_post.compensation, compensation)
		self.assertEqual(first_saved_job_post.text, text)

	def test_save_and_retrieve_keyword(self):
		word = 'junior'
		word_1 = Keyword()
		word_1.word = word
		word_1.save()

		saved_words = Keyword.objects.all()
		self.assertEqual(saved_words.count(), 1)

		saved_word_1 = saved_words[0]

		self.assertEqual(saved_word_1.word, word)

	def test_save_and_retrieve_skill(self):
		skill = 'python'
		
		skill_1 = Skill()
		skill_1.skill = skill
		skill_1.save()

		saved_skills = Skill.objects.all()
		self.assertEqual(saved_skills.count(), 1)

		saved_skill_1 = saved_skills[0]

		self.assertEqual(saved_skill_1.skill, skill)

	def test_save_and_retrieve_experience(self):
		experience = '3+ years of programming'
		
		experience_1 = Experience()
		experience_1.experience = experience
		experience_1.save()

		saved_experiences = Experience.objects.all()
		self.assertEqual(saved_experiences.count(), 1)

		saved_experience_1 = saved_experiences[0]

		self.assertEqual(saved_experience_1.experience, experience)

	def test_save_and_retrieve_job_keyword(self):
		word_id = 1
		post_id = 2

		job_keyword_1 = JobKeyword()
		job_keyword_1.word_id = word_id
		job_keyword_1.post_id = post_id
		job_keyword_1.save()

		saved_job_keywords = JobKeyword.objects.all()
		self.assertEqual(saved_job_keywords.count(), 1)

		saved_job_keyword_1 = saved_job_keywords[0]

		self.assertEqual(saved_job_keyword_1.word_id, word_id)
		self.assertEqual(saved_job_keyword_1.post_id, post_id)

	def test_save_and_retrieve_job_skill(self):
		skill_id = 3
		post_id = 4

		job_skill_1 = JobSkill()
		job_skill_1.skill_id = skill_id
		job_skill_1.post_id = post_id
		job_skill_1.save()

		saved_job_skills = JobSkill.objects.all()
		self.assertEqual(saved_job_skills.count(), 1)

		saved_job_skill_1 = saved_job_skills[0]

		self.assertEqual(saved_job_skill_1.skill_id, skill_id)
		self.assertEqual(saved_job_skill_1.post_id, post_id)

	def test_save_and_retrieve_job_experience(self):
		experience_id = 5
		post_id = 6

		job_experience_1 = JobExperience()
		job_experience_1.experience_id = experience_id
		job_experience_1.post_id = post_id
		job_experience_1.save()

		saved_job_experiences = JobExperience.objects.all()
		self.assertEqual(saved_job_experiences.count(), 1)

		saved_job_experience_1 = saved_job_experiences[0]

		self.assertEqual(saved_job_experience_1.experience_id, experience_id)
		self.assertEqual(saved_job_experience_1.post_id, post_id)


# class NoSQLTestRunner(DjangoTestSuiteRunner):
# 	def setup_databases(self):
# 		pass
# 	def teardown_databases(self, *args):
# 		pass

# class NoSQLTestCase(TestCase):
# 	def _fixture_setup(self):
# 		pass

# 	def _fixture_teardown(self):
# 		pass

# 	def test_saving_and_retrieving_job_links(self):
# 		first_job_link = JobLink()
# 		first_job_link.text = 'A cool job'
# 		first_job_link.post_id = 1
# 		first_job_link.summary = 'This is a job that you totally want to have'
# 		first_job_link.save()

# 		second_job_link = JobLink()
# 		second_job_link.text = 'A not cool job'
# 		second_job_link.post_id = 2
# 		second_job_link.summary = 'You really don\'t want this job'
# 		second_job_link.save()

# 		saved_job_links = JobLink.objects.all()
# 		self.assertEqual(saved_job_links.count(), 2)

# 		first_saved_job_link = saved_job_links[0]
# 		second_saved_job_link = saved_job_links[1]
# 		self.assertEqual(first_saved_job_link.text, first_job_link.text)
# 		self.assertEqual(first_saved_job_link.post_id, 1)
# 		self.assertEqual(first_saved_job_link.summary, first_job_link.summary)
# 		self.assertEqual(second_saved_job_link.text, second_job_link.text)
# 		self.assertEqual(second_saved_job_link.post_id, 2)
# 		self.assertEqual(second_saved_job_link.summary, second_job_link.summary)

# class DbTest(NoSQLTestCase):

# 	def test_save_and_retrieve_job_post(self):
# 		post = JobPost(
# 			title='First Job Post',
# 			posted='2014-07-24  2:22pm',
# 			keywords=['c#, java, python'],
# 			original_post_link='',
# 			location='DUMBO',
# 			job_title='awesome coder',
# 			address='150 water st',
# 			map_link='',
# 			compensation='$50,000',
# 			skills=['c#', 'java', 'python'],
# 			experience=[],
# 			text="This is like the coolest job, hope you get it!!! save teh worldddddd"
# 		)
# 		post.save()

# 		retrieved_post = JobPost.objects(title__contains='First Job Post')
# 		self.assertEqual(retrieved_post.title, post.title)
# 		self.assertEqual(retrieved_post.posted, post.posted)
# 		self.assertEqual(retrieved_post.keywords, post.keywords)
# 		self.assertEqual(retrieved_post.original_post_link, post.original_post_link)
# 		self.assertEqual(retrieved_post.location, post.location)
# 		self.assertEqual(retrieved_post.job_title, post.job_title)
# 		self.assertEqual(retrieved_post.address, post.address)
# 		self.assertEqual(retrieved_post.map_link, post.map_link)
# 		self.assertEqual(retrieved_post.compensation, post.compensation)
# 		self.assertEqual(retrieved_post.skills, post.skill)
# 		self.assertEqual(retrieved_post.experience, post.experience)
# 		self.assertEqual(retrieved_post.text, post.text)
