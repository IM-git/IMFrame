import pytest

from tools import Browser
from tools import DataSettings

from pages import LoginPage
from src import Login

from settings import LOGIN_STANDARD, PASSWORD


@pytest.fixture(scope='session')
def browser():
    """
    Initialization browser driver.
    """
    data = DataSettings.config_data()
    driver = Browser.browser_(data)
    driver.implicitly_wait(data["wait_time"])
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def authorization(browser):
    """
    Using for authorization on the site(standard option).
    How it works. Need to add: @pytest.mark.usefixtures("authorization")
    for the test class or method which need to use authorization.
    After that this decorator will replace the authentication steps
    in the test methods.

    ########## Short example ##########

    @pytest.mark.usefixtures("authorization")
    class TestSomePage:
        # Will be performed authorization on site,
          opened necessary page and 5 seconds be waited.

        def test_open_some_page(self, browser):
            some_page = CartPage(browser, Cart.LINK)
            some_page.open_page()
            time.sleep(5)
    """
    LoginPage(browser, Login.LINK).authorization(LOGIN_STANDARD, PASSWORD)

