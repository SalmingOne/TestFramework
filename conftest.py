import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from data.urls import Urls
from pages.base_page import BasePage

CI = os.getenv('CI')

@pytest.fixture(scope="class")
def driver():
    if CI == 'false':
        driver = webdriver.Chrome(service=Service(), options=Options())
        driver.maximize_window()
    else:
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        service = Service("/usr/bin/chromedriver")
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

@pytest.fixture(scope='class')
def open_site(driver):
    BasePage(driver).open()
