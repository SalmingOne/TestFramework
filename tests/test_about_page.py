import allure

from pages.about_page import AboutPage


class TestAboutPage:
    @allure.title("Проверка содержания страницы О нас")
    def test_view_about_page(self, driver, open_site):
        about_page = AboutPage(driver)
        about_page.go_to_page()
        title, description_1, description_2 = about_page.get_text_on_page()
        assert title == 'о нас', "Неправильное название секции"
        assert description_1 == 'Effective Mobile — это команда экспертов, которая поможет создать ' \
                                'собственное мобильное приложение или оперативно внедрить на ваш проект ' \
                                'лучших специалистов в сфере IT.', 'Неверный текст первой части описания'
        assert description_2 == 'Наша цель — обеспечить ваш бизнес IT решениями и опытными специалистами.', \
            'Неверный текст второй части описания'
