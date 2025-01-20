from selenium.webdriver.common.by import By


class MainPageLocators:
    MAIN_PAGE_BUTTON = (By.XPATH, "//a[text()='Effective Mobile']")
    MAIN_PAGE_TITLE = (By.CSS_SELECTOR, "h1[class='tn-atom']")
    MAIN_PAGE_DESCRIPTION = (By.XPATH, "//h1[@class='tn-atom']/../following-sibling::div[1]")