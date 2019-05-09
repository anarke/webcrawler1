from selenium import webdriver
from selenium.webdriver.common.by import By
import time
browser = webdriver.Chrome()

browser.get("https://book.douban.com/top250")
for i in range(0,10):
	title = browser.find_element_by_xpath("//div[@id='content']//h1").text
	print(title)
	book_list = browser.find_elements_by_xpath("//tr[@class='item']")
	for ele in book_list:
	print(ele.text + "\n")
	print("------Page %s------"%(i+1))

	next_page = browser.find_element_by_class_name("next").click()
	time.sleep(5)
	print("\n")
