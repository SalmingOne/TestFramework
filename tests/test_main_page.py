import time

import allure

from data.urls import Urls
from pages.main_page import MainPage


@allure.suite("Главная страница")
class TestMainPage:

    @allure.title("Проверка содержания главной страницы")
    def test_view_main_page(self, driver, open_site):
        main_page = MainPage(driver)
        main_page.go_to_page()
        title, description = main_page.get_text_on_page()
        assert title == 'Разработка\nмобильных приложений', 'Неверный заголовок страницы'
        assert description == 'Высококвалифицированные специалисты или целая команда под ваши задачи', \
            "Неверное описание страницы"
