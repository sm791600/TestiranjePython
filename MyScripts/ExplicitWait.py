import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def run_test():
    # Стартување на Google Chrome прелистувачот
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # 1. Отворање на веб апликацијата
        print("1. Отворање на веб апликацијата...")
        driver.get("http://127.0.0.1:5000")

        # 2. Кликнуваме на копчето 'Б'
        print("2. Кликување на копчето 'Б'...")
        btn_b = driver.find_element(By.ID, "btnB")
        btn_b.click()
        sleep(7)

        # 3. Експлицитно чекање копчето 'Резервирај' да стане кликабилно (максимум до 12 секунди)
        wait = WebDriverWait(driver, 12)
        reserve_btn = driver.find_element(By.ID, "reserveBtn")

        # 4. Кликување на копчето 'Резервирај'
        reserve_btn.click()
        sleep(7)

        # 5. Експлицитно чекање да се појави параграфот за успешна резервација (максимум до 8 секунди)
        print("5. Се чека потврдата за резервација (2-6 сек)...")
        success_msg_element = driver.find_element(By.ID, "successMsg")
        # success_msg_element.click()



        # 6. Проверка и верификација на текстот
        result_text = success_msg_element.text
        print(f"-> Порака на екранот: '{result_text}'")

        assert "Успешна резервација" in result_text
        print("\n ТЕСТОТ Е УСПЕШНО ПОЛОЖЕН!")

    except Exception as e:
        print(f"\n Грешка за време на тестирањето: {e}")
    finally:
        # Пауза за визуелна потврда и затворање
        time.sleep(2)
        driver.quit()

if __name__ == "__main__":
    run_test()