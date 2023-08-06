import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

manager = ChromeDriverManager()
CHROME_DRIVER_PATH = manager.install()
service = Service(executable_path=CHROME_DRIVER_PATH)


def test_search():
    driver = Chrome(service=service)
    search_value = 'foobar'
    driver.get('http://www.google.com/')
    assert 'https://www.google.com/' in driver.current_url, 'Неправильный урл!'
    assert 'Google' in driver.title, 'Неправильный тайтл!'
    search_field = driver.find_element(By.CSS_SELECTOR, 'textarea[type="search"]')
    search_field.clear()
    time.sleep(0.5)
    search_field.send_keys(search_value)
    time.sleep(0.5)
    search_button = driver.find_element(By.CSS_SELECTOR, 'div > div  > div > div > center > input[role="button"]')
    search_button.click()
    time.sleep(5)
    assert search_value in driver.title, 'Неправильный тайтл!'
    assert f'q={search_value}' in driver.current_url, 'Неправильный урл!'
    search_elements = driver.find_elements(By.CSS_SELECTOR, '[data-async-context="query:foobar"] > div')
    for el in search_elements:
        el_lower = el.text.lower()
        assert 'foobar' in el_lower, f'Текста {search_value} нет в элементе {el}!'
    driver.quit()
