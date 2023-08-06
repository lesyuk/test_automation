import time
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Chrome Driver Manager
manager = ChromeDriverManager()

# Скачивает chromedriver и записывает путь к нему
CHROME_DRIVER_PATH = manager.install()

#
service = Service(executable_path=CHROME_DRIVER_PATH)

# ChromeOptions
# Опции нужно будет связать с драйвером браузера через передачу аргумента options
options = ChromeOptions() # Класс, которые управляет опциями
options.add_argument('--headless')  # Аргумент командной строки запуска браузера
# options.add_encoded_extension('') # Передача браузерных расширений, закодированные в base64

# Теперь при создании объекта класса Chrome передаем options
# При создании объекта этого класса автоматически запустится браузер
driver = Chrome(service=service, options=options)

driver.get('https://www.aviasales.ru/') # Принимает урл, который нужно открыть
time.sleep(1)

# Поиск элементов на странице
element = driver.find_element(By.CSS_SELECTOR, '[data-test-id="form-submit"]')
elements = driver.find_elements(By.CSS_SELECTOR, '[data-test-id="form-submit"]')

print('\n\n\n')
print('find_element', element)
print(type(element))
print()
print('find_elements', elements)
print(type(elements))
print('\n\n\n')

for _ in range(5):
    driver.refresh() # Обновляет страницу
    time.sleep(1)

print(driver.title) # Получает title страницы, на которой находимся
# driver.close() # в 4 селениуме работает так же как quit(). Раньше quit() закрывал браузер
# # close закрывал активную вкладку браузера: если последняя, то браузер закрывался;
# # если больше 1, то браузер продолжал висеть
driver.maximize_window() # Увеличивает окно браузера до размеров viewport. Но чаще мы захотим использовать set_window_size
time.sleep(1)
driver.set_window_size(888, 666) # Устанавливает конкретные размеры окна
# driver.execute_script('') # Выполняет JS на странице, так же, как можно сделать в девтулзах
driver.save_screenshot('test.png') # Сохраняет скриншот страницы
# driver.page_source # Возвращает html-код страницы
# driver.add_cookie() # Добавляет куки в браузерную сессию (например, для ускорения авторизации)
# driver.get_cookie() # Получает текущие куки
# driver.delete_cookie() # Удаляет куки
print(driver.current_url) # Содержит урл текущей открытой страницы

# driver.close()
driver.quit() # Закрывает браузер
