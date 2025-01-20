from selenium.webdriver.common.by import By


class ReviewsPageLocators:
    REVIEWS_PAGE_BUTTON = (By.XPATH, "//a[text()='[ Отзывы ]']")
    REVIEWS_PAGE_TITLE = (By.CSS_SELECTOR, 'div[class="t730__topsection"]')
    REVIEWS_PAGE_CAROUSEL = (By.CSS_SELECTOR, 'div[id="carousel_699930013"]')