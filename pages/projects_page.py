import allure

from locators.projects_page_locators import ProjectsPageLocators
from pages.base_page import BasePage


class ProjectsPage(BasePage):

    locators = ProjectsPageLocators()

    @allure.step('Перейти на страницу Проекты')
    def go_to_page(self):
        self.element_is_visible(self.locators.PROJECTS_PAGE_BUTTON).click()

    @allure.step('Карусель проектов отображена')
    def projects_carousel_is_displayed(self):
        return self.element_is_displayed(self.locators.PROJECTS_PAGE_CAROUSEL)
