from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://localhost:5005/")

sleep(2)
inputField = driver.find_element(By.ID, "numberInput")
inputField.send_keys("9") #9 is for I, 10 is for J to check detection errors
submitButton = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
submitButton.click()

wait_for_message = WebDriverWait(driver, 10)
success_result= wait_for_message.until(
    EC.visibility_of_element_located((By.ID, "mainresult"))
)

print(f"Expected: I, found: {success_result.text}")
if "I" in success_result.text:
    print(f"Success")
else:
    print(f"Error")
sleep(3)