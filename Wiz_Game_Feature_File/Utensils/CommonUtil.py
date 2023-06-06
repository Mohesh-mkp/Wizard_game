import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from Wiz_Game_Feature_File.Utensils.object_repo import objectdict
from selenium.webdriver.support.select import Select


def open_browser(context):
    context.driver = webdriver.Chrome(objectdict['driver_loc'])
    context.driver.maximize_window()


def input_text(context, location ,username):
    context.driver.find_element(By.ID, location).send_keys(username)


def click_element(context, element):
    context.driver.find_element(By.ID, element).click()
    time.sleep(2)


def click_element_by_xpath(context, element):
    context.driver.find_element(By.XPATH, element).click()
    time.sleep(2)

def Dashboard_page(context):
    context.driver.implicitly_wait(5)
    context.driver.find_element(By.ID, objectdict['Three_bar_locator']).click()
    context.driver.save_screenshot("C:\Mohesh\Wizard_Game_BDD\Screenshot\Threebar_click.png")
    context.driver.find_element(By.ID, objectdict['About_locator']).click()
    context.driver.save_screenshot("C:\Mohesh\Wizard_Game_BDD\Screenshot\About.png")

def Verify_displayed(context, element):
    bool_val = context.driver.find_element(By.XPATH, element).is_displayed()
    if bool_val is True:
        print('Logo Exist in main page')
    else:
        print('Logo does not Exist in current page')


def verify_text(context, element, actual_res):
    text_val = context.driver.find_element(By.XPATH, actual_res).text
    if text_val == element:
        print('Actual meets with expected outcome')
    else:
        print('Actual does not meet expected outcome')


def dropdown_filter(context, value):
    element = context.driver.find_element(By.XPATH, objectdict['filter_locator'])
    drop = Select(element)
    drop.select_by_visible_text(value)


def verify_content(context, amount):
    context.driver.execute_script("window.scrollBy(0,1000)", "")
    time.sleep(3)
    lc = context.driver.find_element(By.XPATH, objectdict['checkout_total']).text


