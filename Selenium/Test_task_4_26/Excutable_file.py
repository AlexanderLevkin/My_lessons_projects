import time
from ActionOnSite import Login, SelectItem, DataFromCart, driver, login, password
from Selenium.Test_task_4_26.Selectors import *

# Authorization on site

auth = Login(driver=driver)
auth.enter_to_the_site(login_name=login, password_name=password)

"""ITEM 1"""
#ITEM 1 (Paths of items on main page, cart page, order page)
def purchase_1():

    pick_a_item = SelectItem(driver=driver)
    pick_a_item.selecting_item(pick_item = item_1)
    pick_a_item.selecting_name_item(name_item = item_name_1)
    pick_a_item.selecting_cost_item(cost_item = item_cost_comm)
    pick_a_item.click_on_cart_button(cart_but = cart_button_comm)

    # Select data from site to compare
    data_capture = DataFromCart(driver=driver)
    data_capture.cart_check_name(cart_name=cart_name_comm)
    data_capture.cart_check_cost(cart_cost=cart_cost_comm)

    # ASSERTS
    assert pick_a_item.selecting_name_item(name_item = item_name_1) == data_capture.cart_check_name(cart_name=cart_name_comm)
    print("Name of item match with cart")
    time.sleep(1)

    data_capture.click_on_the_checkout_button()
    data_capture.fill_in_the_information_about_customer()
    data_capture.item_sum_from_cart(item_sum=item_sum_comm)
    data_capture.total_sum_from_cart(total_sum=total_sum_comm)

    assert data_capture.item_sum_from_cart(item_sum=item_sum_comm) == data_capture.total_sum_from_cart(total_sum=total_sum_comm)
    print('The sum from cart corresponds total sum !!!')
    return ()

"""ITEM 2"""
#ITEM 2 (Paths of items on main page, cart page, order page)
def purchase_2():
    pick_a_item = SelectItem(driver=driver)
    pick_a_item.selecting_item(pick_item = item_2)
    pick_a_item.selecting_name_item(name_item = item_name_2)
    pick_a_item.selecting_cost_item(cost_item = item_cost_comm)
    pick_a_item.click_on_cart_button(cart_but = cart_button_comm)

    # Select data from site to compare
    data_capture = DataFromCart(driver=driver)
    data_capture.cart_check_name(cart_name=cart_name_comm)
    data_capture.cart_check_cost(cart_cost=cart_cost_comm)

    # ASSERTS
    assert pick_a_item.selecting_name_item(name_item = item_name_2) == data_capture.cart_check_name(cart_name=cart_name_comm)
    print("Name of item match with cart")
    time.sleep(1)

    data_capture.click_on_the_checkout_button()
    data_capture.fill_in_the_information_about_customer()
    data_capture.item_sum_from_cart(item_sum=item_sum_comm)
    data_capture.total_sum_from_cart(total_sum=total_sum_comm)

    assert data_capture.item_sum_from_cart(item_sum=item_sum_comm) == data_capture.total_sum_from_cart(total_sum=total_sum_comm)
    print('The sum from cart corresponds total sum !!!')
    return ()

"""ITEM 3"""
#ITEM 3 (Paths of items on main page, cart page, order page)
def purchase_3():
    pick_a_item = SelectItem(driver=driver)
    pick_a_item.selecting_item(pick_item = item_3)
    pick_a_item.selecting_name_item(name_item = item_name_3)
    pick_a_item.selecting_cost_item(cost_item = item_cost_comm)
    pick_a_item.click_on_cart_button(cart_but = cart_button_comm)

    # Select data from site to compare
    data_capture = DataFromCart(driver=driver)
    data_capture.cart_check_name(cart_name=cart_name_comm)
    data_capture.cart_check_cost(cart_cost=cart_cost_comm)

    # ASSERTS
    assert pick_a_item.selecting_name_item(name_item = item_name_3) == data_capture.cart_check_name(cart_name=cart_name_comm)
    print("Name of item match with cart")
    time.sleep(1)

    data_capture.click_on_the_checkout_button()
    data_capture.fill_in_the_information_about_customer()
    data_capture.item_sum_from_cart(item_sum=item_sum_comm)
    data_capture.total_sum_from_cart(total_sum=total_sum_comm)

    assert data_capture.item_sum_from_cart(item_sum=item_sum_comm) == data_capture.total_sum_from_cart(total_sum=total_sum_comm)
    print('The sum from cart corresponds total sum !!!')
    return ()

"""ITEM 4"""
#ITEM 4 (Paths of items on main page, cart page, order page)
def purchase_4():
    pick_a_item = SelectItem(driver=driver)
    pick_a_item.selecting_item(pick_item = item_4)
    pick_a_item.selecting_name_item(name_item = item_name_4)
    pick_a_item.selecting_cost_item(cost_item = item_cost_comm)
    pick_a_item.click_on_cart_button(cart_but = cart_button_comm)

    # Select data from site to compare
    data_capture = DataFromCart(driver=driver)
    data_capture.cart_check_name(cart_name=cart_name_comm)
    data_capture.cart_check_cost(cart_cost=cart_cost_comm)

    # ASSERTS
    assert pick_a_item.selecting_name_item(name_item = item_name_4) == data_capture.cart_check_name(cart_name=cart_name_comm)
    print("Name of item match with cart")
    time.sleep(1)

    data_capture.click_on_the_checkout_button()
    data_capture.fill_in_the_information_about_customer()
    data_capture.item_sum_from_cart(item_sum=item_sum_comm)
    data_capture.total_sum_from_cart(total_sum=total_sum_comm)

    assert data_capture.item_sum_from_cart(item_sum=item_sum_comm) == data_capture.total_sum_from_cart(total_sum=total_sum_comm)
    print('The sum from cart corresponds total sum !!!')
    return ()

"""ITEM 5"""
#ITEM 5 (Paths of items on main page, cart page, order page)
def purchase_5():
    pick_a_item = SelectItem(driver=driver)
    pick_a_item.selecting_item(pick_item = item_5)
    pick_a_item.selecting_name_item(name_item = item_name_5)
    pick_a_item.selecting_cost_item(cost_item = item_cost_comm)
    pick_a_item.click_on_cart_button(cart_but = cart_button_comm)

    # Select data from site to compare
    data_capture = DataFromCart(driver=driver)
    data_capture.cart_check_name(cart_name=cart_name_comm)
    data_capture.cart_check_cost(cart_cost=cart_cost_comm)

    # ASSERTS
    assert pick_a_item.selecting_name_item(name_item = item_name_5) == data_capture.cart_check_name(cart_name=cart_name_comm)
    print("Name of item match with cart")
    time.sleep(1)

    data_capture.click_on_the_checkout_button()
    data_capture.fill_in_the_information_about_customer()
    data_capture.item_sum_from_cart(item_sum=item_sum_comm)
    data_capture.total_sum_from_cart(total_sum=total_sum_comm)

    assert data_capture.item_sum_from_cart(item_sum=item_sum_comm) == data_capture.total_sum_from_cart(total_sum=total_sum_comm)
    print('The sum from cart corresponds total sum !!!')
    return ()

"""ITEM 6"""
#ITEM 6 (Paths of items on main page, cart page, order page)
def purchase_6():
    pick_a_item = SelectItem(driver=driver)
    pick_a_item.selecting_item(pick_item = item_6)
    pick_a_item.selecting_name_item(name_item = item_name_6)
    pick_a_item.selecting_cost_item(cost_item = item_cost_comm)
    pick_a_item.click_on_cart_button(cart_but = cart_button_comm)

    # Select data from site to compare
    data_capture = DataFromCart(driver=driver)
    data_capture.cart_check_name(cart_name=cart_name_comm)
    data_capture.cart_check_cost(cart_cost=cart_cost_comm)

    # ASSERTS
    assert pick_a_item.selecting_name_item(name_item = item_name_6) == data_capture.cart_check_name(cart_name=cart_name_comm)
    print("Name of item match with cart")
    time.sleep(1)

    data_capture.click_on_the_checkout_button()
    data_capture.fill_in_the_information_about_customer()
    data_capture.item_sum_from_cart(item_sum=item_sum_comm)
    data_capture.total_sum_from_cart(total_sum=total_sum_comm)

    assert data_capture.item_sum_from_cart(item_sum=item_sum_comm) == data_capture.total_sum_from_cart(total_sum=total_sum_comm)
    print('The sum from cart corresponds total sum !!!')
    return ()
