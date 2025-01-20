import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from data.urls import Urls
from pages.base_page import BasePage

@pytest.fixture(scope="class")
def driver():
    driver = webdriver.Chrome(options=webdriver.ChromeOptions(), service=ChromeService())
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope='class')
def open_site(driver):
    BasePage(driver).open()
