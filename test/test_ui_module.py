from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from pages.AuthPage import AuthPage
from time import sleep

def test_auth():
    browser = webdriver.Chrome()
    browser.implicitly_wait(4)
    browser.maximize_window()

    auth_page = AuthPage(browser)
    auth_page.go()

    sleep(5)


