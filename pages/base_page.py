import allure
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from data.urls import Urls


class BasePage:

    def __init__(self, driver, url=Urls.base_url):
        self.driver = driver
        self.url = url
    @allure.step('Открыть страницу')
    def open(self):
        self.driver.get(self.url)

    @allure.step('Элемент видим')
    def element_is_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))

    @allure.step('Элемент представлен на странице')
    def element_is_present(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located(locator))

    @allure.step('Элементы видимы')
    def elements_are_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(ec.visibility_of_all_elements_located(locator))

    @allure.step('Элемент отображен')
    def element_is_displayed(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
