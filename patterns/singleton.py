from patterns import Factory

"""
Singleton is a creative design pattern
that lets you ensure that a class has only one instance,
while providing a global access point to this instance.
"""


class WebDriver:
    """This is singleton for webdriver."""
    class __WebDriver:

        def __init__(self, data):
            self.driver = Factory().get_browser(data)

    driver = None

    def __init__(self, data):
        if not self.driver:
            WebDriver.driver = WebDriver.__WebDriver(data).driver


class Singleton(type):
    """This is singleton for read file."""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
