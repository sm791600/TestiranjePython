import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://testpages.eviltester.com/pages/basics/basic-web-page/")
driver.find_element(By.ID, "button1").click()

time.sleep(8)
driver.quit()