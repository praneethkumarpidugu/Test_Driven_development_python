#Functional test for django application
#TODO
#1.import package
#2.we will initiate a browser for instance firefox
#3.get a localhost development server testing
#4.writing a assertion Browser title "Hello shrathank"

#We are going to build a site called TODO LISTS
from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		#Shrathank has heard about a new site called to-do app. He goes to checkout its homepage
		self.browser.get('http://localhost:8001')

	#He notices the page title and header mention to-do lists
		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish the test!')



#He is invited to enter a to-do item straight-away

#He types "Buy a cellphone" into a text box

#He hits enter, the page updates, and noe the page lists
#"1.Buy a cellphone" as an item in a to-do lists

#There is still a text box inviting him a to add another item. He
#enters "Use cellphone to call his mom first"

#The page updates again, and now shows both item on his list

#Shrathank wonders whether the site will remember his list. Then sees that the site has generated a Unique URL for him
#--There is some explanatory text to that effect

#He visits that URL- TO-DO list is still there.

#Then he exits his application

if __name__ == '__main__':
	unittest.main(warnings='ignore')
