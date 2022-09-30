# IMFrame
___
My draft-framework, use for performing webpages tests.
___
Introduction about singleton+webdriver.\
Here 2 ways for using webdriver:
1. **Without singleton.**\
Enter webdriver(browser) in class page from test file.
```
.\tests\test_main.py


from pages.main_page import MainPage

def test_main(self, browser):
           main_page = MainPage(browser)
```
_If not add browser in MainPage: MainPage(), webdriver will still be initialized._

2. **Use singleton.**\
Creates one time the object with webdriver in conftest.py\
Object have global access. Uses the webdriver exactly from page.
```
.\tests\example_tests\test_main.py

from pages.example_pages.main_page import MainPage


def test_main(self):
           main_page = MainPage()
```

```
.\pages\base_page.py

from tools import DataSettings

DATA = DataSettings.config_data()


class MainPage(BasePage):

    def __init__(self):
        browser = None
        super().__init__(browser)
        if browser is None:
            self.browser = WebDriver(DATA).driver
        else:
            self.browser = browser
```
In the base_page file: if browser isn't shipping from test file( is None), takes webdriver from DataSetting,
else browser conducts from test file.\
In this situation, it is compared here that the file is initialized using singleton or not.
___
Structure folders:

```
├───elements
├───pages
├───patterns
├───selenoid
├───src
│   ├───enums
│   ├───locators
│   └───sql_requests
├───tests
│   └───sql_tests
└───tools
    ├───exceptions
    ├───logs
    ├───mongodb
    ├───test_settings
    └───sql
```
