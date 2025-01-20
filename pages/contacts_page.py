import allure

from locators.contacts_page_locators import ContactsPageLocators
from pages.base_page import BasePage


class ContactsPage(BasePage):

    locators = ContactsPageLocators()

    @allure.step('Перейти на страницу Контакты')
    def go_to_page(self):
        self.element_is_visible(self.locators.CONTACTS_PAGE_BUTTON).click()

    @allure.step('Получить текст на странице')
    def get_text_on_page(self):
        title = self.element_is_visible(self.locators.CONTACTS_PAGE_TITLE).text
        description_part_1 = self.element_is_visible(self.locators.CONTACTS_PAGE_DESCRIPTION_PART_ONE).text
        description_part_2 = self.element_is_visible(self.locators.CONTACTS_PAGE_DESCRIPTION_PART_TWO).text
        # остальные элементы на странице ...
        return title, description_part_1, description_part_2