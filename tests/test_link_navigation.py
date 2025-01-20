import allure
import pytest

from pages.about_page import AboutPage
from pages.contacts_page import ContactsPage
from pages.projects_page import ProjectsPage
from pages.reviews_page import ReviewsPage
from pages.services_page import ServicesPage
from pages.specialists_page import SpecialistsPage


@allure.suite("Навигация по сайту")
class TestLinkNavigation:

    @pytest.mark.parametrize("page, expected_url", [
        (AboutPage, "https://effective-mobile.ru/#about"),
        (ServicesPage, "https://effective-mobile.ru/#moreinfo"),
        (ProjectsPage, "https://effective-mobile.ru/#cases"),
        (ReviewsPage, "https://effective-mobile.ru/#Reviews"),
        (ContactsPage, "https://effective-mobile.ru/#contacts"),
        (SpecialistsPage, "https://effective-mobile.ru/#specialists"),
    ], ids=['About', 'Services', 'Projects', 'Reviews', 'Contacts', 'Specialists'])
    @allure.title("Проверка переходов по страницам")
    def test_link_navigation(self, driver, open_site, page, expected_url):
        page(driver).go_to_page()
        assert driver.current_url == expected_url
