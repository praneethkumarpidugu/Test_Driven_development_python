#Functional test for django application
#TODO
#1.import package
#2.we will initiate a browser for instance firefox
#3.get a localhost development server testing
#4.writing a assertion Browser title "Hello shrathank"
from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://localhost:8000')
assert 'Django' in browser.title