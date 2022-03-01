from base_element import BaseElement


class Elements:

    @staticmethod
    def click(browser, locator, element):
        return BaseElement().find_element(
            browser, locator, element).click()

    @staticmethod
    def get_to_attribute(browser, locator, element, attribute):
        return BaseElement().find_element(
            browser, locator, element).click().get_attribute(attribute)

    @staticmethod
    def get_text(browser, locator, element):
        return BaseElement().find_element(
            browser, locator, element).click().text

