class BaseElement:

    @staticmethod
    def find_element(browser, locator, element):
        return browser.find_element(locator, element)

