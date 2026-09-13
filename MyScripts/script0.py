from time import sleep

from selenium import webdriver


driver = webdriver.Firefox()
driver.get("http://127.0.0.1:5000")
sleep(10)
driver.quit()