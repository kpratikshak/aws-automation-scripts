from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import sleep 
import csv 

url= 'https://www.linkedin.com/jobs/search/?keywords=python&location=india&geoId=101174742&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'
driver.get(url)
sleep(3)

email_field = driver.find_element('id','session_key')
email_field.send_keys('Your Email Here')
sleep(3)

password_field = driver.find_element('id','session_password')
password_field.send_keys('Your Password Here')
sleep(3)


login_field = driver.find_element('xpath','//*[@id="main-content"]/section[1]/div/form/div[3]/button')
login_field.click()
sleep(3)

search_field = driver.find_element('id','jobs-search-box-keyword-id-ember7')
search_field.send_keys('Keys.RETURN')
sleep(3)

search_field.send_keys(Keys.ENTER)
sleep(3)

job_list = driver.find_elements('class name','jobs-search-results__list-item')