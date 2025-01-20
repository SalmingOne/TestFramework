from selenium.webdriver.common.by import By


class ProjectsPageLocators:
    PROJECTS_PAGE_BUTTON = (By.XPATH, "//a[text()='[ Проекты ]']")
    PROJECTS_PAGE_CAROUSEL = (By.CSS_SELECTOR, 'div[id="carousel_572838727"]')