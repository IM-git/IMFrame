from elements import BaseElement


class Elements:

    @staticmethod
    def click(browser, locator, element):
        """Click the specified element."""
        return BaseElement().find_element(
            browser, locator, element).click()

    @staticmethod
    def get_to_attribute(browser, locator, element, attribute):
        """Get the specified attribute."""
        return BaseElement().find_element(
            browser, locator, element).click().get_attribute(attribute)

    @staticmethod
    def get_text(browser, locator, element):
        """Get the text from specified element."""
        return BaseElement().find_element(
            browser, locator, element).click().text

