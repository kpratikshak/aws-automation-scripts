from selenium import webdriver
import time 

web = webdriver.Chrome()
web.get('https://docs.google.com/forms/d/1y5Gn4r0JYwOZ4dVJ3bM9WjH0QxuJ3mM1d0G2M1d0G2M/viewform?edit_requested=true')

time.sleep(3)
LastName = "Aditya"
last = web.find_element_by_xpath(
    "/html/body/div[1]/div[2]/form/div[2]/div/div[1]/div[1]/div/div[1]/input")
last.send_keys(LastName)

FirstName = "Gupta"
first = web.find_element_by_xpath('//*[@id="i1"]/div[2]/div/div[1]/div[1]/div/div[1]/input')
first.send_keys(FirstName)

RadioButtonPeriod = web.find_element_by_xpath('//*[@id="i3"]/div[2]/div/div[1]/div[1]/div[1]/div[2]/span/div[1]/div[1]')
RadioButtonPeriod.click()

Submit = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div')
Submit.click()

get_confirmation_div_text = web.find_element_by_css_selector('.freebirdFormviewerViewFormConfirmationMessage')

print(get_confirmation_div_text.text)
if((get_confirmation_div_text.text) == 'Thanks for your submission!'):
    print('Test was successfull')
else:
    print('Test was not successfull')