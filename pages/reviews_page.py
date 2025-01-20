import allure

from locators.reviews_page_locators import ReviewsPageLocators
from pages.base_page import BasePage


class ReviewsPage(BasePage):

    locators = ReviewsPageLocators()

    @allure.step('Перейти на страницу Отзывы')
    def go_to_page(self):
        self.element_is_visible(self.locators.REVIEWS_PAGE_BUTTON).click()

    @allure.step('Получить текст на странице')
    def get_text_on_page(self):
        title = self.element_is_visible(self.locators.REVIEWS_PAGE_TITLE).text
        return title.lower()

    @allure.step('Карусель отзывов отображена')
    def reviews_carousel_is_displayed(self):
        return self.element_is_displayed(self.locators.REVIEWS_PAGE_CAROUSEL)