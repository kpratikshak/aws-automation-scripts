from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import By 

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.google.com/")

search = driver.find_element(By.NAME, "q")
search.clear()
search.send_keys("Dress")

sleep(4)

driver.find_element(By.NAME, "btnK").click()

assert "dress" in driver.current_url.lower(),f"unexpected query {driver.current_url.lower()}""
print("Test passed")

driver.quit()