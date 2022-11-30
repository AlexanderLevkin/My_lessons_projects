import time

from selenium.webdriver.common.by import By


class Main():
    def __init__(self, driver):
        self.driver = driver

    def login(self, login, password):
        username_field = self.driver.find_element(By.XPATH, '//input[@id="user-name"]')
        username_field.send_keys(login)
        password_field = self.driver.find_element(By.XPATH, '//input[@id="password"]')
        password_field.send_keys(password)
        time.sleep(1)
        login_button = self.driver.find_element(By.XPATH, '//input[@id="login-button"]')
        login_button.click()
        time.sleep(1)
        print("Login into site\n")


"""Собираем переменные по вещам в магазине (Добавляем в корзину)"""
# #Souce labs backpack
#         sauce_labs_backpack = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]')
# #Sauce_Labs_Bike_light
#         sauce_labs_bike_light = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-bike-light"]')
# # sauce_labs_bolt_t_shirt
#         sauce_labs_bolt_t_shirt = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
# # sauce_labs_fleece_jacket
#         sauce_labs_fleece_jacket = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-fleece-jacket"]')
# #sauce_labs_onesie
#         sauce_labs_onesie = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-onesie"]')
#t_shirt_red
