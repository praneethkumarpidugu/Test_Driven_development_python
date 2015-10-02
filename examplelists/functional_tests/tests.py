#Functional test for django application
#TODO
#1.import package
#2.we will initiate a browser for instance firefox
#3.get a localhost development server testing
#4.writing a assertion Browser title "Hello shrathank"

#We are going to build a site called TODO LISTS
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(LiveServerTestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def check_for_row_in_list_table(self, row_text):
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])

	def test_can_start_a_list_and_retrieve_it_later(self):
		#Shrathank has heard about a new site called to-do app. He goes to checkout its homepage
		self.browser.get(self.live_server_url)

	#He notices the page title and header mention to-do lists
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)
		
	
	#He is invited to enter a to-do item straight-away
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
			)

	#He types "Buy peacock feathers" into a text box.
		inputbox.send_keys('Buy peacock feathers')

	#He hits enter, the page updates, and now the page lists
	#"1.Buy peacock feathers" as an item in a to-do list table
		inputbox.send_keys(Keys.ENTER)
		edith_list_url = self.browser.current_url
		self.assertRegex(edith_list_url, '/lists/.+')
		self.check_for_row_in_list_table('1: Buy peacock feathers')

#There is still a text box inviting him a to add another item. He
#enters "Use peacock feathers to make a fly"
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Use peacock feathers to make a fly')
		inputbox.send_keys(Keys.ENTER)

#The page updates again, and now shows both item on his list
		self.check_for_row_in_list_table('1: Buy peacock feathers')
		self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')
#Now a user, Pradeep, comes along to the site

##We use a new browser session to make sure that no information
##of Shrathank's is coming thorugh from cookies etc
		self.browser.quit()
		self.browser = webdriver.Firefox()
#Pradeep Visits the home page. There is no sign of Shrathanks list
		self.browser.get(self.live_server_url)
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Buy peacock feathers', page_text)
		self.assertNotIn('make a fly', page_text)
#Pradeep starts a new list by entering a new item. He is less
# interesting than Shrathank..
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Buy milk')
		inputbox.send_keys(Keys.ENTER)

#Pradeep gets hi own unique URL
		francis_list_url = self.browser.current_url
		self.assertRegex(francis_list_url, '/list/.+')
		self.assertNotIn('Buy peacock feathers', page_text)
		self.assertIn('Buy milk', page_text)

#Then he exits his application

