from selenium.webdriver.common.by import By

class AuthPage:

    def __init__(self, browser):
        self._driver = browser
        self._driver.get("ttps://www.kinopoisk.ru/")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

#найти поле ввода логина и пароля
    def search_input_field(self):
        self._driver.find_element(By.CLASS, "CurrentAccount-login").send_keys("AuthAccountListItem-login")
        self._driver.find_element(By.ID, "passp-field-passwd").send_keys("KiVi8021KiN")
        self._driver.find_element(By.CLASS, "Button2 Button2_size_xxl Button2_view_contrast-action Button2_width_max Button2_type_submit").click()