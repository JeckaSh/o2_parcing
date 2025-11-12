from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import re
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

driver = webdriver.Chrome()

def test_negative_scenarios():
    try:
        # СЦЕНАРИЙ 1: попытка поиска на несуществующей странице
        logger.info("Сценарий 1: заход на некорректный URL")
        driver.get("https://ru.wikipedia.org/wrong-page")  # заведомо неверный адрес

        try:
            search_input = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.ID, "searchInput"))
            )
            logger.error("Ошибка: поле поиска найдено на несуществующей странице!")
        except TimeoutException:
            logger.info("Сценарий 1 пройден: страница не загрузилась, поле поиска отсутствует")

    except Exception as e:
        logger.error(f"Неожиданная ошибка в тесте: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_negative_scenarios()
