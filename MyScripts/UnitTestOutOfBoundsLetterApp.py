from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://localhost:5005/")

sleep(2)
RandomGivenLetter = driver.find_element(By.ID, "randomPositionDisplay")
calculatedLetter = int(RandomGivenLetter.text)
calculatedLetter = round(calculatedLetter / 3)
foundLetter = "z"

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
            'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
            'U', 'V', 'W', 'X', 'Y', 'Z']
i=1
while i>=1 and i <=26:
    if i == calculatedLetter:
        foundLetter = alphabet[i-1]
        print("the given letter is:" , RandomGivenLetter.text, "the calculated letter is:"
              , calculatedLetter,  alphabet[i-1])
        break
    else:
        i = i + 1

inputField = driver.find_element(By.ID, "letterInput")
inputField.send_keys(foundLetter)
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

sleep(3)
driver.quit()