import allure

from locators.services_page_locators import ServicesPageLocators
from pages.base_page import BasePage


class ServicesPage(BasePage):

    locators = ServicesPageLocators()

    @allure.step('Перейти на страницу Услуги')
    def go_to_page(self):
        self.element_is_visible(self.locators.SERVICES_PAGE_BUTTON).click()

    @allure.step('Получить текст на странице')
    def get_text_on_page(self):
        title = self.element_is_visible(self.locators.SERVICES_PAGE_TITLE).text
        return title

    @allure.step('Получить список услуг')
    def get_services_list(self):
        return [service.text.lower() for service in self.elements_are_visible(self.locators.SERVICES_LIST)]