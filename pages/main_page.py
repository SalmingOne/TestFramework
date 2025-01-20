import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    locators = MainPageLocators()

    @allure.step('Перейти на главную страницу')
    def go_to_page(self):
        self.element_is_visible(self.locators.MAIN_PAGE_BUTTON).click()

    @allure.step('Получить текст на странице')
    def get_text_on_page(self):
        title = self.element_is_visible(self.locators.MAIN_PAGE_TITLE).text
        description = self.element_is_visible(self.locators.MAIN_PAGE_DESCRIPTION).text
        return title, description

