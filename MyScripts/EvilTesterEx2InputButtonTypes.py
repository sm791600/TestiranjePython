from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://testpages.eviltester.com/pages/forms/text-inputs/")

inputField = driver.find_element(By.ID, "text-input")
inputField.send_keys("Ове е текст поле")

searchField = driver.find_element(By.ID, "search-input")
searchField.send_keys("Пребарување")

password = driver.find_element(By.ID, "password-input")
password.send_keys("pass123")

emailField = driver.find_element(By.ID, "email-input")
emailField.send_keys("exaple@mail.com")

urlField = driver.find_element(By.ID, "url-input")
urlField.send_keys("https://testpages.eviltester.com/")

telephoneField = driver.find_element(By.ID, "tel-input")
telephoneField.send_keys("070123456")

defaultTextField = driver.find_element(By.ID, "text-default-input")
defaultTextField.send_keys("default text")

sleep(5)

submit_button = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"][value="submit"]')

submit_button.click()

sleep(15)
driver.quit()