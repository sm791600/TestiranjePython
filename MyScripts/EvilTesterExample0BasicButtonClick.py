from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://testpages.eviltester.com/pages/basics/basic-web-page/")
driver.find_element(By.ID, "button1").click()

sleep(8)
driver.quit()
#driver. quit izgldea kako da e opcionalen bidejki se gasi i vaka i taka