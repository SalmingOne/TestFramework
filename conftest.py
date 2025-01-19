import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from data.urls import Urls

os.getenv()

@pytest.fixture
def driver():
    driver = webdriver.Chrome(options=webdriver.ChromeOptions(), service=ChromeService())
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def open_site(driver):
    driver.get(Urls.base_url)
    yield driver