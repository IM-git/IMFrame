from pages import BasePage

from elements import MouseActions
from elements import KeyboardActions

from src.locators.example_locators.main import Main

from tools import Logger
from tools import DataSettings

DATA = DataSettings.config_data()


class MainPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

        #   Displaying info about use of the singleton(yes/no)
        Logger().info(f'The use of singleton: {DATA["singleton"].lower()}.')

        self.mouse_actions = MouseActions(self.browser)
        self.keyboard_actions = KeyboardActions(self.browser)

    def click_link_english_version(self) -> None:
        self.click_element(*Main.LINK_ENGLISH_VERSION)

    def click_link_community_portal(self) -> None:
        self.click_element(*Main.LINK_COMMUNITY_PORTAL)
