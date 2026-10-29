from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome()
driver.get("http://localhost:5005/")
sleep(2)
submitButton = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
submitButton.click()
sleep(3)