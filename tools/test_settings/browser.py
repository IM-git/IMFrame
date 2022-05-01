from patterns import Factory
from patterns import WebDriver
from tools.exceptions import InvalidCondition


class Browser:

    @staticmethod
    def browser(data):
        """Two options, create webdriver with singleton
        or without one.
        Condition pointed in the SINGLETON variable."""

        if data["singleton"].lower() == "no":
            driver = Factory().get_browser(data)  # without singleton
        elif data["singleton"].lower() == "yes":
            driver = WebDriver(data).driver     # singleton
        else:
            raise InvalidCondition(data["singleton"])
        return driver
