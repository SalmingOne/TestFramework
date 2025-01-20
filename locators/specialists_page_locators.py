from selenium.webdriver.common.by import By


class SpecialistsPageLocators:
    SPECIALISTS_PAGE_BUTTON = (By.XPATH, "//a[text()='Выбрать специалиста']")
    SPECIALISTS_PAGE_TITLE = (By.XPATH, "//div[contains(@class, 't1095')]//div[contains(@class, 't-section__title')]")
    LI_ITEMS = (By.XPATH, "//div[contains(@class, 't1095')]//li")