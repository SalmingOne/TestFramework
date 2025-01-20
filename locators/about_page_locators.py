from selenium.webdriver.common.by import By


class AboutPageLocators:
    ABOUT_PAGE_BUTTON = (By.XPATH, "//a[text()='[ О нас ]']")
    ABOUT_PAGE_TITLE = (By.CSS_SELECTOR, 'div[field="tn_text_1680508197707"]')
    ABOUT_PAGE_DESCRIPTION_PART_ONE = (By.CSS_SELECTOR, 'div[field="tn_text_1680508197689"]')
    ABOUT_PAGE_DESCRIPTION_PART_TWO = (By.CSS_SELECTOR, 'div[field="tn_text_1680508197711"]')