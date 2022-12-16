from ActionOnSite import Item
from Selenium.Test_task_4_26.Selectors import *

"""ITEM 1"""


def purchase_1():
    auth = Item(login_name=login, password_name=password, pick_item=item_1, name_item=item_name_1)
    auth.enter_to_the_site()


"""ITEM 2"""


def purchase_2():
    auth = Item(login_name=login, password_name=password, pick_item=item_2, name_item=item_name_2)
    auth.enter_to_the_site()


"""ITEM 3"""


def purchase_3():
    auth = Item(login_name=login, password_name=password, pick_item=item_3, name_item=item_name_3)
    auth.enter_to_the_site()


"""ITEM 4"""


def purchase_4():
    auth = Item(login_name=login, password_name=password, pick_item=item_4, name_item=item_name_4)
    auth.enter_to_the_site()


"""ITEM 5"""


def purchase_5():
    auth = Item(login_name=login, password_name=password, pick_item=item_5, name_item=item_name_5)
    auth.enter_to_the_site()


"""ITEM 6"""


def purchase_6():
    auth = Item(login_name=login, password_name=password, pick_item=item_6, name_item=item_name_6)
    auth.enter_to_the_site()
