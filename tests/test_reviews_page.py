import allure

from pages.reviews_page import ReviewsPage


class TestReviewsPage:

    @allure.title("Проверка содержания страницы Отзывы")
    def test_view_reviews_page(self, driver, open_site):
        reviews_page = ReviewsPage(driver)
        reviews_page.go_to_page()
        title = reviews_page.get_text_on_page()
        assert title == 'отзывы клиентов', "Неправильное название секции"
        assert reviews_page.reviews_carousel_is_displayed(), 'Слайдер отзывов не отображается'
