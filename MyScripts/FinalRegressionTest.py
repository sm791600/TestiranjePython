import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


def run_test_scenario():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 30)

    try:
        print("--- ЧЕКОР 1: Почеток на првата страна ---")
        driver.get("http://localhost:5005/")

        # 1. Читање на вредноста од екранот и пресметка (3 места помала во редоследот, заокружено надолу)
        givenLetter = (driver.find_element(By.ID, "givenLetterDisplay")).text

        # Дефинирање на азбуката и наоѓање на соодветната буква
        alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                    'U', 'V', 'W', 'X', 'Y', 'Z']

        # Наоѓање на редниот број на таа буква во азбуката (додаваме 1 бидејќи индексите почнуваат од 0)
        given_position = alphabet.index(givenLetter) + 1
        calculated_position = given_position // 3

        # Безбедно мапирање со индекс (одземaме 1 бидејќи индексите во листа почнуваат од 0)
        index = max(0, calculated_position - 1)
        found_letter = alphabet[index]
        print(f"Прочитан број: {givenLetter} -> Пресметана буква: {found_letter}")

        # 2. Внесување на буквата и клик на поднесување
        input_field = wait.until(EC.element_to_be_clickable((By.ID, "letterInput")))
        input_field.send_keys(found_letter)

        submit_btn = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        submit_btn.click()
        submit_btn = wait.until(EC.element_to_be_clickable((By.ID, "continueToReservation"))) #prodolzuva posle stranata za rezultati
        submit_btn.click()

        print("--- ЧЕКОР 2: Втора страница (Резервација) ---")
        # 3. Избор на едно од 3-те копчиња (на пр. копчето 'Б')
        btn_b = wait.until(EC.element_to_be_clickable((By.ID, "btnB")))
        btn_b.click()
        print("Избрано е копчето Б. Се чека овозможување на копчето за резервација...")

        # 4. Чекање копчето 'Резервирај' да стане кликабилно
        reserve_btn = wait.until(
            EC.element_to_be_clickable((By.ID, "reserveBtn"))
        )
        reserve_btn.click()
        print("Копчето 'Резервирај' е кликнато.")

        # 5. Потврда за успешна резервација
        success_msg = wait.until(
            EC.visibility_of_element_located((By.ID, "successMsg"))
        )
        print(f"Порака: {success_msg.text}")
        checkBox = wait.until(EC.element_to_be_clickable((By.ID, "robotCheck")))
        checkBox.click()
        textFields = (driver.find_element(By.ID, "fullName"))
        textFields.send_keys("First Name")
        textFields = (driver.find_element(By.ID, "address"))
        textFields.send_keys("old Road no.123")
        textFields = (driver.find_element(By.ID, "cardNumber"))
        textFields.send_keys("0123456789")
        dropDownMenu = (driver.find_element(By.ID, "country"))
        dropDown = Select(dropDownMenu)
        dropDown.select_by_visible_text("Јапан")
        radioMenu = (driver.find_element(By.ID, "express-shipping"))
        radioMenu.click()
        submitAndContinue = (driver.find_element(By.ID, "submitAndContinue"))
        submitAndContinue.click()

        print("--- ЧЕКОР 3: Трета страница (Одбројување до негативен број) ---")

        # Тука се чека елементот кој одбројува (пример ID: "countdownTimer") додека вредноста не стане помала од 0
        # Користиме custom Lambda услов за да провериме кога текстот ќе стане негативен (на пр. содржи '-')

        def is_countdown_negative(drv):
            try:
                resultMessage = (driver.find_element(By.ID, "statusText")).text
                if  "Системска грешка при обработка на редот!" in resultMessage:
                    return True
                return False

                # timer_element = drv.find_element(By.ID, "counterValue")
                # val = float(timer_element.text)
                # return val < 0

            except:
                return False

        # Чекаме максимум 30 секунди бројачот да стане негативен
        wait.until(is_countdown_negative)
        print("Бројачот стана негативен! Тестот е успешно завршен.")

    except Exception as e:
        print(f"Настана грешка за време на тестот: {type(e).__name__} -> {e}")
    finally:
        time.sleep(3)
        driver.quit()


if __name__ == "__main__":
    run_test_scenario()