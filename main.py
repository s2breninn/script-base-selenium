from pathlib import Path
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# Chrome Options
# https://peter.sh/experiments/chromium-command-line-switches/

# Caminho para a raiz do projeto
ROOT_FOLDER = Path(__file__).parent
# Caminho para a pasta onde o chromedrive está
CHROME_DRIVER_PATH = ROOT_FOLDER / 'drivers' / 'chromedriver'

def make_chrome_browser(*options: str) -> webdriver.Chrome:
    try:
        chrome_options = webdriver.ChromeOptions()

        # chrome_options.add_argument('--headless')
        if options is not None:
            for option in options:
                chrome_option.add_argument(option) # type: ignore

        chrome_service = Service(
            executable_path=str(CHROME_DRIVER_PATH),
        )

        browser = webdriver.Chrome(
            service=chrome_service,
            options=chrome_options,
        )
    except ExceptionGroup as e:
        print(f'Error: {e}')

    return browser

if __name__ == '__main__':
    TIME_TO_WAIT = 10

    # Example
    # options = '--headless', '--disable-gpu'
    options = ()
    browser = make_chrome_browser(*options)

    # Como antes
    browser.get('https://www.google.com/')

    # Espere para encontrar o input
    try:
        search_input = WebDriverWait(browser, TIME_TO_WAIT).until(
            ec.presence_of_element_located(
                (By.NAME, 'q')
            )
        )
    except ExceptionGroup as e:
        print(f'Elemento não identificado: {e}')

    search_input.send_keys('Hello world')

    # Dorme por 10s
    sleep(TIME_TO_WAIT)