from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://localhost:5005/")

sleep(2)

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
            'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
            'U', 'V', 'W', 'X', 'Y', 'Z']
givenLetter = (driver.find_element(By.ID, "givenLetterDisplay")).text
i = 0
while i < len(alphabet):
    if alphabet[i] == givenLetter:
        givenLetter = alphabet[(i //3)-1]
        break
    else:
        i += 1

inputField = driver.find_element(By.ID, "letterInput")
inputField.send_keys(givenLetter)
submitButton = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
submitButton.click()

wait_for_message = WebDriverWait(driver, 10)
expected_result = wait_for_message.until(
    EC.visibility_of_element_located((By.ID, "mainresult"))
)
user_result = driver.find_element(By.ID, "userresult")

print(f"Expected: {expected_result.text}, Entered: {user_result.text}")

if expected_result.text == user_result.text:
    print("Success: Correct letter guessed!")
else:
    print("Result mismatch: Expected and user letters do not match.")

sleep(2)
driver.quit()