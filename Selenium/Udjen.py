import time
import datetime
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome, Firefox, Remote, ActionChains, Keys

driver = Chrome(executable_path=ChromeDriverManager().install())
base_url = "https://yudzhen.by/"
driver.get(base_url)
driver.maximize_window()

send_feedback = driver.find_element(By.XPATH, '//a[@class="btn-green-border letter-director"]')
send_feedback.click()

name_field = driver.find_element(By.CSS_SELECTOR, '#wpcf7-f121-o3 > form:nth-child(2) > div:nth-child(3) > '
                                                  'span:nth-child(2) > input:nth-child(1)')
name_field.send_keys("TEST_TEST")

phone_field = driver.find_element(By.CSS_SELECTOR, '#wpcf7-f121-o3 > form:nth-child(2) > div:nth-child(4) > '
                                                   'span:nth-child(2) > input:nth-child(1)')
phone_field.send_keys("TEST_TEST")

email_field = driver.find_element(By.CSS_SELECTOR, '#wpcf7-f121-o3 > form:nth-child(2) > div:nth-child(5) > '
                                                   'span:nth-child(2) > input:nth-child(1)')
email_field.send_keys("TEST_TEST@mail")

message_field = driver.find_element(By.NAME, 'textarea-919')
message_field.send_keys("This is the test message, don't answer on it")

click_on_the_sent_button = driver.find_element(By.CSS_SELECTOR, 'div.popap-submit:nth-child(7) > button:nth-child(1)')
click_on_the_sent_button.click()

warning_test = driver.find_element(By.CSS_SELECTOR, 'div.wpcf7-response-output:nth-child(8)')
value_warning_test = warning_test.text
try:
    warning_message_phone = driver.find_element(By.XPATH, '//span[@class="wpcf7-not-valid-tip"]')
    warning_message_phone = warning_message_phone.text
    print(warning_message_phone)
except NoSuchElementException as exception:
    time.sleep(3)
    warning_message_phone = driver.find_element(By.XPATH, '//span[@class="wpcf7-not-valid-tip"]')
    warning_message_phone = warning_message_phone.text
    assert warning_message_phone == "Введён некорректный телефонный номер."
    print("PHONE - TEST PASS")
    time.sleep(1)
try:
    warning_message_email = driver.find_element(By.XPATH, '//span[@class="wpcf7-not-valid-tip"]')
    warning_message_email = warning_message_email.text
    assert warning_message_email == "Неверно введён элекронный адрес."
    print("EMAIL - TEST PASS")
except AssertionError as exception:
    warning_message_email = driver.find_element(By.CSS_SELECTOR, '#wpcf7-f121-o3 > form > div:nth-child(5) '
                                                                 '> span > span')
    warning_message_email = warning_message_email.text
    assert warning_message_email == "Неверно введён электронный адрес."
    print("EMAIL - TEST PASS")
    time.sleep(1)