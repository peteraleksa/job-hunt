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

		# open up the settings page
		self.assertIn('Settings', self.browser.title)

		self.fail('Finish the test!')

if __name__ == '__main__':
	unittest.main()