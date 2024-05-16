#!/usr/bin/python
# -*- coding: UTF-8 -*-
import allure
from utils.urls import Urls
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=10):
        wait = WebDriverWait(self.driver, time)
        return wait.until(EC.presence_of_element_located(locator), message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        wait = WebDriverWait(self.driver, time)
        return wait.until(EC.presence_of_all_elements_located(locator), message=f"Can't find elements by locator {locator}")

    @allure.step('Перейти по адресу')
    def go_to_site(self, url=Urls.MAIN_PAGE):
        self.driver.get(url)

    @allure.step('Получить текущий URL')
    def current_url(self):
        return self.driver.current_url

    # Переключиться на определенное окно
    def switchwindow(self, windownumber: int = 1):
        # Пример использования методов из базового класса
        self.switchwindow(windownumber)