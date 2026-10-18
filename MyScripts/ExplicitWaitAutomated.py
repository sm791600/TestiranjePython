from datetime import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

LOG_FILE = "test_results.txt"
NUMBER_OF_RUNS = 5  # Колку пати да се повтори тестот


class DebugTimer:
    def __init__(self):
        self.last_time = time.time()

    def log(self, message: str):
        now_dt = datetime.now()
        timestamp = now_dt.strftime("%H:%M:%S") + f".{now_dt.microsecond // 1000:03d}"

        current_time = time.time()
        elapsed = current_time - self.last_time  # Време во секунди со милисекунди
        self.last_time = current_time  # Ресетирање за следниот чекор

        print(f"⏱️ [{timestamp}] (изминаа {elapsed:.3f}s) -> {message}")

timer = DebugTimer()
timer.log("Старт на тестот")
def log_result(status: str, message: str):
    """Ја запишува пораката во txt фајл со нов ред и точен датум и час."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] [{status}] {message}\n"

    # 'a' (append) режим за да се додава нов ред без да се брише претходното
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_entry)

    print(log_entry.strip())


def run_single_test(run_number):
    print(f"\n--- ИЗВРШУВАЊЕ ТЕСТ #{run_number} ---")
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # 1. Отворање на веб апликацијата
        driver.get("http://127.0.0.1:5000")

        # 2. Кликување на копчето 'Б'
        btn_b = driver.find_element(By.ID, "btnB")
        btn_b.click()
        timer.log("кликнато е Б")

        # 3. Експлицитно чекање копчето 'Резервирај' да стане кликабилно (максимум до 12 секунди)
        # wait = WebDriverWait(driver, 5,1,5)
        # reserve_btn = wait.until(
        #     EC.element_to_be_clickable((By.ID, "reserveBtn"))
        # )

        # Чека максимално 5 секунди
        wait = WebDriverWait(driver, 5)
        reserve_btn = wait.until(
            EC.element_to_be_clickable((By.ID, "reserveBtn"))
        )

        # 4. Кликување на копчето 'Резервирај'
        reserve_btn.click()
        timer.log("Кликнато е резервација")

        # 5. Експлицитно чекање да се појави параграфот за успешна резервација (максимум до 8 секунди)
        # success_msg_element = wait.until(
        #     EC.visibility_of_element_located((By.ID, "successMsg"))
        # )
        wait_for_msg = WebDriverWait(driver, 8)
        success_msg_element = wait_for_msg.until(
            EC.visibility_of_element_located((By.ID, "successMsg"))
        )
        timer.log("се дочека успешната порака")

        # 6. Проверка и верификација на текстот
        result_text = success_msg_element.text

        if "Успешна резервација" in result_text:
            log_result("PASSED", f"Тест #{run_number}: Успешна резервација. Порака: '{result_text}'")
        else:
            log_result("FAILED", f"Тест #{run_number}: Неочекуван текст на екранот: '{result_text}'")

    except Exception as e:
        # Доколку се појави грешка (timeout, елемент не е најден и сл.)
        log_result("FAILED", f"Тест #{run_number}: Грешка: {type(e).__name__} - {str(e).splitlines()[0]}")
    finally:
        driver.quit()
        timer.log("тест сесијата заврши")


if __name__ == "__main__":
    # Запишување заглавие во лог фајлот за новиот циклус
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(
            f"\n================ СТАРТ НА НОВИ ТЕСТОВИ ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')}) ================\n")

    # Повторување на тестот дефиниран број пати
    for i in range(1, NUMBER_OF_RUNS + 1):
        run_single_test(i)
        time.sleep(2)  # Пауза меѓу две извршувања