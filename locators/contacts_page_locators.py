from selenium.webdriver.common.by import By


class ContactsPageLocators:
    CONTACTS_PAGE_BUTTON = (By.XPATH, "//a[text()='[ Контакты ]']")
    CONTACTS_PAGE_TITLE = (By.CSS_SELECTOR, 'div[field="tn_text_1680516225306"]')
    CONTACTS_PAGE_DESCRIPTION_PART_ONE = (By.CSS_SELECTOR, 'div[field="tn_text_1680515874720"]')
    CONTACTS_PAGE_DESCRIPTION_PART_TWO = (By.CSS_SELECTOR, 'div[field="tn_text_1681390572339"]')