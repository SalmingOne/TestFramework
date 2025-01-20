import allure

from locators.specialists_page_locators import SpecialistsPageLocators
from pages.base_page import BasePage


class SpecialistsPage(BasePage):

    locators = SpecialistsPageLocators()

    @allure.step('Перейти на страницу Специалисты')
    def go_to_page(self):
        self.element_is_visible(self.locators.SPECIALISTS_PAGE_BUTTON).click()

    @allure.step('Получить текст на странице')
    def get_text_on_page(self):
        return self.element_is_visible(self.locators.SPECIALISTS_PAGE_TITLE).text

    @allure.step('Получить список технологий')
    def get_stack_items(self):
        return [item.text for item in self.elements_are_visible(self.locators.LI_ITEMS)]
