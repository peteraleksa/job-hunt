from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def testRetriveJobListings(self):
		# open up the main page
		self.browser.get('http://localhost:8000')
		self.assertIn('Job Hunt', self.browser.title)

		# all skills are selected by default
		skills = self.browser.find_elements_by_name('skillset')
		for skill in skills:
			self.assertTrue(skill.is_selected())

		# click search button
		search_button = self.browser.find_element_by_id('search_btn')
		search_button.click

		# see results with summarys
		self.browser.implicitly_wait(3)
		self.assertIn('Results', self.browser.title)

		# change sort by to date posted

		# filter by post date

		# click on result link to see posts
		result_link = self.browser.find_element_by_class('result_link')
		result_link.click

		# see a post

		self.fail('Finish the test!')

if __name__ == '__main__':
	unittest.main()