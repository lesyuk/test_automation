import pytest
import time
import os
from uuid import uuid4
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

manager = ChromeDriverManager()
CHROME_DRIVER_PATH = manager.install()
service = Service(executable_path=CHROME_DRIVER_PATH)

# options = ChromeOptions()
# options.add_argument('--headless')
# caps = options.to_capabilities()


@pytest.fixture(scope='function')
def browser(request):
    options = ChromeOptions()
    prefs = {'download.default_directory': r'D:\tmp'}
    options.add_experimental_option('prefs', prefs)
    driver = Chrome(service=service, options=options)
    driver.get(request.config.getoption('--url'))
    driver.maximize_window()

    yield driver

    if ("call" not in request.node.stash) or request.node.stash["call"].failed:
        driver.save_screenshot(str(uuid4().hex) + '.png')

    driver.quit()


@pytest.mark.skip
@pytest.mark.parametrize('text', ['python', 'python3'])
def test_search(browser, text):
    browser.find_element(By.CSS_SELECTOR, '#APjFqb').send_keys(text)
    time.sleep(2)
    browser.find_element(By.CSS_SELECTOR, 'div > div > div > div > center > input[role="button"]').click()
    time.sleep(2)
    assert 'Welcome to Python.org' in browser.page_source, 'There is no string in search result'


@pytest.mark.skip
def test_slider(browser):
    # browser.implicitly_wait(12)

    wait = WebDriverWait(browser, 15)

    old_url = browser.current_url

    def wait_slider(driver):
        return driver.find_element(By.XPATH, "(//div[@class='slide-copy'])[2]//a").is_displayed()

    wait.until(wait_slider())
    browser.find_element(By.XPATH, "(//div[@class='slide-copy'])[2]//a").click()
    time.sleep(1)
    assert old_url != browser.current_url


def test_donwload(browser):
    browser.find_element(By.CSS_SELECTOR, '.download-for-current-os > .download-os-windows > p > a').click()

    wait = WebDriverWait(browser, 10)

    # Return a list containing the names of the files in the directory
    files = os.listdir(r'D:\tmp')
    print('\n\n\n')
    print(files)
    print('\n\n\n')

    # Will wait of new file appear in the /tmp folder
    def wait_file(_):
        return len(files) < len(os.listdir(r'D:\tmp'))

    wait.until(wait_file)
    time.sleep(60)
