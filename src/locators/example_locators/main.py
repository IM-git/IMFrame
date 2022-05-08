from selenium.webdriver.common.by import By


class Main:
    LINK = "https://www.wikipedia.org/"
    LINK_ENGLISH_VERSION = (By.CSS_SELECTOR, "#js-link-box-en")
    LINK_COMMUNITY_PORTAL = (By.CSS_SELECTOR, "#mp-other-content a:nth-child(1)")
