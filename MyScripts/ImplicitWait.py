import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

        # 3. Експлицитно чекање копчето 'Резервирај' да стане кликабилно (максимум до 12 секунди)
        print("3. Се чека копчето 'Резервирај' да се овозможи (4-9 сек)...")
        wait = WebDriverWait(driver, 12)
        reserve_btn = wait.until(
            EC.element_to_be_clickable((By.ID, "reserveBtn"))
        )
        print("-> Копчето 'Резервирај' е успешно овозможено!")

        # 4. Кликување на копчето 'Резервирај'
        reserve_btn.click()

        # 5. Експлицитно чекање да се појави параграфот за успешна резервација (максимум до 8 секунди)
        print("5. Се чека потврдата за резервација (2-6 сек)...")
        success_msg_element = wait.until(
            EC.visibility_of_element_located((By.ID, "successMsg"))
        )

        # 6. Проверка и верификација на текстот
        result_text = success_msg_element.text
        print(f"-> Порака на екранот: '{result_text}'")

        assert "Успешна резервација" in result_text
        print("\n ТЕСТОТ Е УСПЕШНО ПОЛОЖЕН!")

    except Exception as e:
        print(f"\n Грешка за време на тестирањето: {e}")
    finally:
        # Пауза за визуелна потврда и затворање
        time.sleep(3)
        driver.quit()

if __name__ == "__main__":
    run_test()