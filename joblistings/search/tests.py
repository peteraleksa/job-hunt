from django.core.urlresolvers import resolve
from django.test import TestCase
from search.views import home_page

# Create your tests here.

class HomePageTest(TestCase):

	def test_root_url_resolves_to_home_page_view(self):
		round = resolve('/')
		self.assertEqual(found.func, home_page)