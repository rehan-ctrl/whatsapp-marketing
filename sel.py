from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
import sys
import csv

browser = webdriver.Chrome("C:\\Users\\CASSIXCOM3\\Downloads\\chromedriver_win32\\chromedriver.exe")

browser.get("https://web.whatsapp.com")
browser.maximize_window()
time.sleep(5)
wait = WebDriverWait(browser, 600)
string = 'Give your paintings a super finish at our Colour Blending Canvas Painting Workshop. Book here: https://bit.ly/31DDDWv'
with open('C:\\Users\\CASSIXCOM3\\Downloads\\test-csv.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter= ',')
	for row in csv_reader:
		# browser.find_element_by_class_name("_2zCfw").clear()
		try:
			inp_xpath_search = "//input[@title='Search or start new chat']"
			# clear search bar for contacts
			browser.find_element_by_xpath(inp_xpath_search).clear()
			input_box_search = WebDriverWait(browser,50).until(lambda driver: browser.find_element_by_xpath(inp_xpath_search))
			input_box_search.click()
			time.sleep(2)
			contact = row[0]
			# search for contact list
			browser.find_element_by_xpath(inp_xpath_search).send_keys(contact)
			time.sleep(4)

			# contact name select from search list
			selected_contact = browser.find_element_by_xpath("//span[@title='"+contact+"']")
			selected_contact.click()

			# message box
			inp_xpath = '//div[@class="_3u328 copyable-text selectable-text"][@contenteditable="true"][@data-tab="1"]'
			input_box = browser.find_element_by_xpath(inp_xpath)

			# attach three dots clicked
			clipButton = browser.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/div/span')
			clipButton.click()
			time.sleep(2)

		    # To send Videos and Images.
			mediaButton = browser.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/span/div/div/ul/li[1]/button/input')

			# field=browser.find_element_by_xpath("//input[@accept='image/*,video/mp4,video/3gpp,video/quicktime']")
			mediaButton.send_keys('C:\\Users\\CASSIXCOM3\\Downloads\\Color Blending Canvas Painting.png')

			time.sleep(3)
			# click to send attahments
			browser.find_element_by_class_name('_1g8sv').click()
			input_box.send_keys(string)
			# wait until message typed
			time.sleep(2)
			# message send
			browser.find_element_by_class_name('_3M-N-').click()
			time.sleep(1)
		except NoSuchElementException:
			print("Message couldn't sent to", format(row[0]))
			# end of the script
	browser.close()