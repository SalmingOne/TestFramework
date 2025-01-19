import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class BasePage:

    def __init__(self, driver, url=None):
        self.driver = driver
        self.url = url
    @allure.step('Открыть страницу')
    def open(self):
        self.driver.get(self.url)

    @allure.step('Элемент видим')
    def element_is_visible(self, locator, timeout=10):
        return WebDriverWait(driver=self.driver, timeout=timeout).until(ec.visibility_of_element_located((locator)))

    @allure.step('Элемент представлен на странице')
    def element_is_present(self, locator, timeout=10):
        return WebDriverWait(driver=self.driver, timeout=timeout).until(ec.presence_of_element_located((locator)))

    @allure.step('Элементы видимы')
    def elements_are_visible(self, locator, timeout=10):
        return WebDriverWait(driver=self.driver, timeout=timeout).until(ec.visibility_of_all_elements_located(locator))
