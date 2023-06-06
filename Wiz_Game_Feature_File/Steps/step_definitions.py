import time
from behave import *
from Wiz_Game_Feature_File.Utensils.CommonUtil import *
from Wiz_Game_Feature_File.Utensils.object_repo import objectdict


@given('I am on the Demo Login Page')
def launch_browser(context):
    open_browser(context)
    context.driver.get(objectdict['given_url'])
    context.driver.save_screenshot("C:\Mohesh\Wizard_Game_BDD\Screenshot\Demo_Login.png")

@when('I fill the account information for account StandardUser into the Username field and the Password field')
def valid_input_field(context):
    input_text(context, objectdict['username_locator'] ,objectdict['User_name1'])
    input_text(context, objectdict['pwd_locator'] ,objectdict['pwd1'])
    context.driver.save_screenshot("C:\Mohesh\Wizard_Game_BDD\Screenshot\Credentials.png")

@when('I click the Login Button')
def login(context):
    click_element(context, objectdict['login_button_locator'])
    context.driver.save_screenshot("C:\Mohesh\Wizard_Game_BDD\Screenshot\Login_click.png")

@then('I am redirected to the Demo Main Page')
def Redirecting_to_dashboard(context):
    Dashboard_page(context)
    context.driver.save_screenshot("C:\Mohesh\Wizard_Game_BDD\Screenshot\Inventory_Page.png")

@then('I verify the App Logo exists')
def logo_verification(context):
    Verify_displayed(context, objectdict['logo_locator'])
    context.driver.save_screenshot("C:\Mohesh\Wizard_Game_BDD\Screenshot\Logo.png")
    time.sleep(5)
    context.driver.close()


@when('I fill the account information for account LockedOutUser into the Username field and the Password field')
def invalid_input_field(context):
    input_text(context, objectdict['username_locator'], objectdict['User_name2'])
    input_text(context, objectdict['pwd_locator'], objectdict['pwd2'])
    context.driver.save_screenshot("C:\Mohesh\Wizard_Game_BDD\Screenshot\Invalid_credentials.png")


@then('I verify the Error Message contains the text "Sorry, this user has been banned. "')
def text_verification(context):
    expected_res = 'Sorry, this user has been banned.'
    verify_text(context, expected_res, objectdict['invalid_user_error'])
    context.driver.save_screenshot("C:\Mohesh\Wizard_Game_BDD\Screenshot\Error_message.png")


@given('I am on the inventory page')
def redirect_to_inventory_page(context):
    launch_browser(context)
    context.driver.save_screenshot("C:\Mohesh\Wizard_Game_BDD\Screenshot\Demo_Login.png")
    valid_input_field(context)
    context.driver.save_screenshot("C:\Mohesh\Wizard_Game_BDD\Screenshot\Valid_cred.png")
    login(context)
    context.driver.save_screenshot("C:\Mohesh\Wizard_Game_BDD\Screenshot\Inventory.png")


@when('user sorts products from low price to high price')
def low_to_high_filter(context):
    value = 'Price (low to high)'
    dropdown_filter(context, value)
    context.driver.save_screenshot("C:\Mohesh\Wizard_Game_BDD\Screenshot\Filter_value.png")


@when('user adds lowest priced product')
def add_lower_price_product(context):
    time.sleep(3)
    click_element_by_xpath(context, objectdict['low_price_product'])
    context.driver.save_screenshot("C:\Mohesh\Wizard_Game_BDD\Screenshot\low_price_prod.png")
    click_element(context, objectdict['add_to_cart_locator'])
    context.driver.save_screenshot("C:\Mohesh\Wizard_Game_BDD\Screenshot\Addtocart.png")


@when('user clicks on cart')
def cart_click(context):
    click_element(context, objectdict['cart_logo_locator'])
    context.driver.save_screenshot("C:\Mohesh\Wizard_Game_BDD\Screenshot\cart.png")

@when('user clicks on checkout')
def checkout_click(context):
    click_element(context, objectdict['checkout_button_lcator'])
    context.driver.save_screenshot("C:\Mohesh\Wizard_Game_BDD\Screenshot\checkout_page.png")


@when('user enters first name John')
def first_name_input(context):
    input_text(context, objectdict['checkout_first_name_locator'], 'John')


@when('user enters last name Doe')
def last_name_input(context):
    input_text(context, objectdict['checkout_last_name_locator'], 'Doe')


@when('user enters zip code 123')
def zip_input(context):
    input_text(context, objectdict['checkout_zip_locator'], '123')
    context.driver.save_screenshot("C:\Mohesh\Wizard_Game_BDD\Screenshot\checkout_name.png")

@when('user clicks Continue button')
def continue_click(context):
    click_element(context,objectdict['continue_button_locator'])
    context.driver.save_screenshot("C:\Mohesh\Wizard_Game_BDD\Screenshot\continue.png")

@then('I verify in Checkout overview page if the total amount for the added item is $8.63')
def checkout_overview_verification(context):
    amount = '8.63'
    print(verify_content(context, amount))
    context.driver.save_screenshot("C:\Mohesh\Wizard_Game_BDD\Screenshot\Total amount.png")


@when('user clicks Finish button')
def finish_click(context):
    click_element(context, objectdict['finish_button_locator'])
    context.driver.save_screenshot("C:\Mohesh\Wizard_Game_BDD\Screenshot\Finishpart.png")

@then('Thank You header is shown in Checkout Complete page')
def checkout_complete_verification(context):
    val = context.driver.find_element(By.XPATH, objectdict['checckout_complete_page_text']).is_displayed()
    if val == True:
        print('Ordr placed successfully')
    else:
        print('Failed to place order')
    context.driver.save_screenshot("C:\Mohesh\Wizard_Game_BDD\Screenshot\Thank_you_page.png")
    context.driver.close()