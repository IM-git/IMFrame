import requests
import allure
from selenium.webdriver.common.by import By
import time

from pages import *
from src import *
from tools import Logger
from tools.allure_screenshot import taking_screenshot
from tools import AllureScreenshot
from pages.main_page import MainPage


class BaseTest:
    pass
