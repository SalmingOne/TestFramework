import allure

from locators.about_page_locators import AboutPageLocators
from pages.base_page import BasePage


class AboutPage(BasePage):
    locators = AboutPageLocators()

    @allure.step('Перейти на страницу О нас')
    def go_to_page(self):
        self.element_is_visible(self.locators.ABOUT_PAGE_BUTTON).click()

    @allure.step('Получить текст на странице')
    def get_text_on_page(self):
        title = self.element_is_visible(self.locators.ABOUT_PAGE_TITLE).text
        description_part_1 = self.element_is_visible(self.locators.ABOUT_PAGE_DESCRIPTION_PART_ONE).text
        description_part_2 = self.element_is_visible(self.locators.ABOUT_PAGE_DESCRIPTION_PART_TWO).text
        # остальные элементы на странице ...
        return title, description_part_1, description_part_2
