import allure

from pages.projects_page import ProjectsPage


@allure.suite("Страница Проекты")
class TestProjectsPage:

    @allure.title("Проверка содержания страницы Проекты")
    def test_view_projects_page(self, driver, open_site):
        projects_page = ProjectsPage(driver)
        projects_page.go_to_page()
        assert projects_page.projects_carousel_is_displayed(), 'Слайдер проектов не отображен на странице'