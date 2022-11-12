from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(executable_path='/Users/alexanderlevkin/Desktop/My_projects/'
                                           'My_lessons_projects/Selenium/geckodriver')
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
email_field.send_keys("TEST_TEST@mail.ru")

message_field = driver.find_element(By.NAME, 'textarea-919')
message_field.send_keys("This is the test message, don't answer on it")

click_on_the_sent_button = driver.find_element(By.CSS_SELECTOR, 'div.popap-submit:nth-child(7) > button:nth-child(1)')
click_on_the_sent_button.click()