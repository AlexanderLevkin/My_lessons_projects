import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome, Firefox, Remote
from EnterSite import Login, SelectItem
from Selenium.Test_task_4_26.DataCapture import DataFromCart
from Selenium.Test_task_4_26.Credentials import item_1, item_name_1, item_cost_1, cart_name_1, cart_cost_1, item_sum_1, \
    total_sum_1

driver = Chrome(executable_path=ChromeDriverManager().install())
base_url = 'https://www.saucedemo.com'
driver.get(base_url)
driver.maximize_window()
password = "secret_sauce"
login = "standard_user"

# Authorization on site
auth = Login(driver=driver)
auth.enter_to_the_site(login_name=login, password_name=password)

#look for items
def purchase_1():
    pick_a_item = SelectItem(driver=driver)
    pick_a_item.selecting_item(pick_item = item_1)
    pick_a_item.selecting_name_item(name_item = item_name_1)
    pick_a_item.selecting_cost_item(cost_item = item_cost_1)
    pick_a_item.click_on_cart_button()

    # Select data from site to compare
    data_capture = DataFromCart(driver=driver)
    data_capture.cart_check_name(cart_name=cart_name_1)
    data_capture.cart_check_cost(cart_cost=cart_cost_1)

    # Asserts
    assert pick_a_item.selecting_name_item(name_item = item_name_1) == data_capture.cart_check_name(cart_name=cart_name_1)
    print("Name of item match with cart")
    time.sleep(1)
    # assert pick_a_item.selecting_cost_item(cost_item = item_cost_1) == data_capture.cart_check_cost(cart_cost=cart_cost_1)
    # print("Cost of item match with cart")
    data_capture.click_on_the_checkout_button()
    data_capture.fill_in_the_information_about_customer()
    data_capture.item_sum_from_cart(item_sum=item_sum_1)
    data_capture.total_sum_from_cart(total_sum=total_sum_1)

    assert data_capture.item_sum_from_cart(item_sum=item_sum_1) == data_capture.total_sum_from_cart(total_sum=total_sum_1)
    print('The sum from cart corresponds total sum !!!')
    return ()
def purchase_2():
    pick_a_item = SelectItem(driver=driver)
    pick_a_item.selecting_item(pick_item = item_1)
    pick_a_item.selecting_name_item(name_item = item_name_1)
    pick_a_item.selecting_cost_item(cost_item = item_cost_1)
    pick_a_item.click_on_cart_button()

    # Select data from site to compare
    data_capture = DataFromCart(driver=driver)
    data_capture.cart_check_name(cart_name=cart_name_1)
    data_capture.cart_check_cost(cart_cost=cart_cost_1)

    # Asserts
    assert pick_a_item.selecting_name_item(name_item = item_name_1) == data_capture.cart_check_name(cart_name=cart_name_1)
    print("Name of item match with cart")
    time.sleep(1)
    # assert pick_a_item.selecting_cost_item(cost_item = item_cost_1) == data_capture.cart_check_cost(cart_cost=cart_cost_1)
    # print("Cost of item match with cart")
    data_capture.click_on_the_checkout_button()
    data_capture.fill_in_the_information_about_customer()
    data_capture.item_sum_from_cart(item_sum=item_sum_1)
    data_capture.total_sum_from_cart(total_sum=total_sum_1)

    assert data_capture.item_sum_from_cart(item_sum=item_sum_1) == data_capture.total_sum_from_cart(total_sum=total_sum_1)
    print('The sum from cart corresponds total sum !!!')
    return ()