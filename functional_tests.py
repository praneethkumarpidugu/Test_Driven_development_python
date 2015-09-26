#Functional test for django application
#TODO
#1.import package
#2.we will initiate a browser for instance firefox
#3.get a localhost development server testing
#4.writing a assertion Browser title "Hello shrathank"

#We are going to build a site called TODO LISTS
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		#Shrathank has heard about a new site called to-do app. He goes to checkout its homepage
		self.browser.get('http://localhost:8001')

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

	#He hits enter, the page updates, and noe the page lists
	#"1.Buy peacock feathers" as an item in a to-do list table
		inputbox.send_keys(Keys.Enter)
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertTrue(
			any(row.text == '1: Buy peacock feathers' for row in rows)
			)

#There is still a text box inviting him a to add another item. He
#enters "Use peacock feathers to make a fly"
		self.fail('Finish the test!')

#The page updates again, and now shows both item on his list

#Shrathank wonders whether the site will remember his list. Then sees that the site has generated a Unique URL for him
#--There is some explanatory text to that effect

#He visits that URL- TO-DO list is still there.

#Then he exits his application

if __name__ == '__main__':
	unittest.main(warnings='ignore')
