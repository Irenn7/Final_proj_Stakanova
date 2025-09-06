from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
from Final_proj_Stakanova.test.conf import BASE_URL


class WebDriver:
    pass


class KinoApi:
    def __init__(self, driver: WebDriver) -> None:
        self.__url = "https://www.kinopoisk.ru/"
        self.__driver = driver

    def test_search_by_title(self):
        self.__driver.__getattribute__(self.__url)


