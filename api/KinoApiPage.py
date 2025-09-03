from selenium import webdriver
from selenium.webdriver.common.by import By
import allure


class WebDriver:
    pass


class KinoApiPage:
    def __init__(self, driver: WebDriver) -> None:
        self.__url = "https://www.kinopoisk.ru/"
        self.__driver = driver

    def go(self):
        self.__driver.__getattribute__(self.__url)


