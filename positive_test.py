from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

# Инициализация драйвера (убедитесь, что ChromeDriver доступен)
driver = webdriver.Chrome()

try:
    # 1. Зайти на сайт Википедии
    driver.get("https://ru.wikipedia.org")

    # Ожидание загрузки страницы и поля поиска
    wait = WebDriverWait(driver, 10)
    search_input = wait.until(EC.presence_of_element_located((By.ID, "searchInput")))

    # 2. Вбить в поиск «Земля»
    search_input.send_keys("Земля")
    search_input.send_keys(Keys.RETURN)

    # 3. Перейти на страницу статьи «Земля»
    article_link = wait.until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Земля"))
    )
    article_link.click()

    # 4. Найти информацию о содержании кислорода в атмосфере
    # Ищем текст страницы
    body_text = driver.find_element(By.TAG_NAME, "body").text

    # Регулярное выражение для поиска процентного содержания кислорода
    # Ищем шаблоны вроде «21%», «20,95%», «около 21%» и т. п.
    pattern = r'(?:около|приблизительно|примерно\s+)?(\d+(?:[,\.]\d+)?)\s*%\s*(?:кислорода|O₂)'
    match = re.search(pattern, body_text, re.IGNORECASE)

    if match:
        oxygen_percent = match.group(1)  # Извлекаем числовое значение
        print(f"Содержание кислорода в атмосфере: {oxygen_percent}%")
    else:
        print("Содержание кислорода в атмосфере: не найдено")

finally:
    # Закрытие браузера
    driver.quit()
