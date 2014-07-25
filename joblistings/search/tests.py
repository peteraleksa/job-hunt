from django.core.urlresolvers import resolve
from django.template.loader import render_to_string
from django.test import TestCase
from django.http import HttpRequest
from search.views import home_page
from search.views import results_page
from search.models import JobLink

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

class JobLinkModelTest(TestCase):

	def test_saving_and_retrieving_items(self):
		first_job_link = JobLink()
		first_job_link.text = "A cool job"
		#first_job_link.post_id = "1"
		first_job_link.summary = "This is a job that you totally want to have"
		first_job_link.save()

		second_job_link = JobLink()
		second_job_link.text = "A not cool job"
		#second_job_link.post_id = "2"
		second_job_link.summary = "You really don't want this job"
		second_job_link.save()

		saved_job_links = JobLink.objects.all()
		self.assertEqual(saved_job_links.count(), 2)

		first_saved_job_link = saved_job_links[0]
		second_saved_job_link = saved_job_links[1]
		self.assertEqual(first_saved_job_link.text, first_job_link.text)
		self.assertEqual(first_saved_job_link.post_id, 1)
		self.assertEqual(first_saved_job_link.summary, first_job_link.summary)
		self.assertEqual(second_saved_job_link.text, second_job_link.text)
		self.assertEqual(second_saved_job_link.post_id, 2)
		self.assertEqual(second_saved_job_link.summary, second_job_link.summary)