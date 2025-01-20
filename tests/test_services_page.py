import allure

from pages.services_page import ServicesPage


class TestServicesPage:

    @allure.title("Проверка содержания страницы Услуги")
    def test_view_services_page(self, driver, open_site):
        services_page = ServicesPage(driver)
        services_page.go_to_page()
        title = services_page.get_text_on_page()
        services = services_page.get_services_list()
        assert title == 'услуги', "Неправильное название секции"
        assert services == ['разработка\nмобильных приложений', 'консалтинг\nв сфере мобильных разработок',
                            'аутстаффинг\nit-персонала и специалистов'], 'Неправильное название услуг'
