import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Wiz_Game_Feature_File.Utensils.object_repo import objectdict

driver = webdriver.Chrome('C:\Mohesh\Drivers\chromedriver.exe')
driver.maximize_window()
driver.get('https://www.saucedemo.com/')
driver.find_element(By.ID,'user-name').send_keys('standard_user')
driver.find_element(By.ID,'password').send_keys('secret_sauce')
driver.find_element(By.ID,'login-button').click()
time.sleep(3)
element = driver.find_element(By.XPATH, objectdict['filter_locator'])
drop = Select(element)
drop.select_by_visible_text('Price (low to high)')
driver.execute_script("window.scrollBy(0,1000)","")
time.sleep(3)
driver.save_screenshot("C:\Mohesh\Wizard_Game_BDD\Screenshot\home.png")