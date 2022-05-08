import time
import allure
from pages.example_pages.main_page import MainPage
from src.locators.example_locators.main import Main
from tests.base_cases import BaseCases


class Test(BaseCases):

    @allure.feature("Main page.")
    @allure.link(url=Main.LINK, name='MAIN_LINK')
    def test_main(self, browser):
        """Checking main page. Open main page.
        Checking the text in the tab header.
        Checking the image display."""

        self.check_status_code(url=Main.LINK)
        main_page = MainPage(browser, Main.LINK)

        main_page.open_page()
        main_page.click_link_english_version()  # pre-main page
        main_page.click_link_community_portal()

        time.sleep(1)
