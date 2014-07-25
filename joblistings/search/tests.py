from django.core.urlresolvers import resolve
from django.template.loader import render_to_string
from django.test import TestCase
from django.http import HttpRequest

from pymongo import Connection

from search.views import home_page
from search.views import results_page

#from search.models import JobLink
#from search.models import JobPost

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

	# def test_home_page_redirects_to_results_on_submit(self):
	# 	request = HttpRequest()
	# 	request.method = 'POST'
	# 	request.POST['skillset'] = 'ninja'
	# 	response = home_page(request)
	# 	expected_html = render_to_string('results.html')
	# 	self.assertEqual(response.content.decode(), expected_html)

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

	#def test_database_lookup(self):

#class JobLinkModelTest(TestCase):

	# def test_saving_and_retrieving_job_links(self):
		# first_job_link = JobLink()
		# first_job_link.text = 'A cool job'
		# #first_job_link.post_id = "1"
		# first_job_link.summary = 'This is a job that you totally want to have'
		# first_job_link.save()

		# second_job_link = JobLink()
		# second_job_link.text = 'A not cool job'
		# #second_job_link.post_id = "2"
		# second_job_link.summary = 'You really don\'t want this job'
		# second_job_link.save()

		# saved_job_links = JobLink.objects.all()
		# self.assertEqual(saved_job_links.count(), 2)

		# first_saved_job_link = saved_job_links[0]
		# second_saved_job_link = saved_job_links[1]
		# self.assertEqual(first_saved_job_link.text, first_job_link.text)
		# self.assertEqual(first_saved_job_link.post_id, 1)
		# self.assertEqual(first_saved_job_link.summary, first_job_link.summary)
		# self.assertEqual(second_saved_job_link.text, second_job_link.text)
		# self.assertEqual(second_saved_job_link.post_id, 2)
		# self.assertEqual(second_saved_job_link.summary, second_job_link.summary)

	# def test_saving_and_retrieving_job_posts(self):
		# title = 'First Job'
		# posted = '2014-07-22  5:21pm'
		# keywords = ['c#', 'java', 'python']
		# original_post_link = 'http://localhost:8000'
		# location = ''
		# job_title = ''
		# address = ''
		# map_link = ''
		# compensation = ''
		# skills = []
		# experience = []
		# tokenized_text = ['Some', 'text', 'about', 'the', 'job']
		# text = 'Some text about the job'

		# first_job_post = JobPost()
		# first_job_post.title = title
		# first_job_post.keywords = keywords
		# first_job_post.original_post_link = original_post_link
		# first_job_post.location = location
		# first_job_post.job_title = job_title
		# first_job_post.address = address
		# first_job_post.map_link = map_link
		# first_job_post.compensation = compensation
		# first_job_post.skills = skills
		# first_job_post.experience = experience
		# first_job_post.tokenized_text = tokenized_text
		# first_job_post.text = text

		# first_job_id = first_job_post.save()

		# saved_job_posts = JobPosts.objects.findOne()
		# self.assertEqual(saved_job_posts.count(), 1)

		# first_saved_job_post = saved_job_posts[0]

		# self.assertEqual(first_saved_job_post.title, title)
		# self.assertEqual(first_saved_job_post.keywords, keywords)
		# self.assertEqual(first_saved_job_post.original_post_link, original_post_link)
		# self.assertEqual(first_saved_job_post.location, location)
		# self.assertEqual(first_saved_job_post.job_title, job_title)
		# self.assertEqual(first_saved_job_post.address, address)
		# self.assertEqual(first_saved_job_post.map_link, map_link)
		# self.assertEqual(first_saved_job_post.compensation, compensation)
		# self.assertEqual(first_saved_job_post.skills, skills)
		# self.assertEqual(first_saved_job_post.experience, experience)
		# self.assertEqual(first_saved_job_post.tokenized_text, tokenized_text)
		# self.assertEqual(first_saved_job_post.text, text)