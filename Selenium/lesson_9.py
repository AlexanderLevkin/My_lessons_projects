import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome, Firefox, Remote

driver = Chrome(executable_path=ChromeDriverManager().install())

base_url = 'https://demoqa.com/checkbox'
driver.get(base_url)
driver.maximize_window()
time.sleep(2)

arrow_of_check_box = driver.find_element(By.XPATH, '//button[@aria-label="Toggle"]')
arrow_of_check_box.click()
check_box_desktop = driver.find_element(By.XPATH, '//label[@for="tree-node-desktop"]')
check_box_desktop.click()
check_box_documents = driver.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[2]/span/label/span[3]')
check_box_documents = check_box_documents.text
print(check_box_documents)
assert check_box_documents == "Documents"
print("Well done")
time.sleep(2)
