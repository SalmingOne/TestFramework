from selenium.webdriver.common.by import By


class ServicesPageLocators:
    SERVICES_PAGE_BUTTON = (By.XPATH, "//a[text()='[ Услуги ]']")
    SERVICES_PAGE_TITLE = (By.CSS_SELECTOR, 'div[field="tn_text_1680510339488"]')
    SERVICES_LIST = (By.CSS_SELECTOR, 'h2[class="tn-atom"]')