from selenium.webdriver.common.by import By

from .base import Base


class Login(Base):
    """
    This class created to work with authorization form.
    """

    LINK = Base.LINK

    LOGIN_BUTTON = (By.CSS_SELECTOR, '')
    LOGIN_INPUT = (By.CSS_SELECTOR, '')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '')
