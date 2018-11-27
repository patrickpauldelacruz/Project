from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest

@pytest.fixture()
def env_setup():
    global driver
    path = "D:\\Python\\Selenium\\chromedriver.exe"
    driver = webdriver.Chrome(path)
    driver.implicitly_wait(10)
    driver.get("http://www.amaysim.com.au")
    driver.maximize_window()

    # Click Log in from Main Page
    link_login = driver.find_element_by_link_text("Login")
    link_login.click()

    # Enter Username
    text_username = driver.find_element_by_css_selector("#username")
    text_username.send_keys("0468340754")

    # Enter Password
    text_password = driver.find_element_by_css_selector("#password")
    text_password.send_keys("theHoff34")

    # Click Log In button
    btn_login = driver.find_element_by_css_selector("#new_session > button")
    btn_login.click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(@data-automation-id, 'mobile-card')]")))

    link_goto_plan = driver.find_element_by_xpath(
        "//*[contains(@data-automation-id, 'mobile-card')]//*[contains(text(), '0468 340 754')]")

    # Click to a specific plan
    link_goto_plan.click()

    # Go To Settings
    link_settings = driver.find_element_by_link_text("Settings")
    link_settings.click()

    yield
    driver.quit()

def test_ChangeSimName(env_setup):
    # Editing Sim Nick Name
    element_edit_sim_nickname = driver.find_element_by_xpath("//*[contains(@id, 'edit_settings_phone_label')]")
    element_edit_sim_nickname.click()

    lbl_sim_nickname = driver.find_element_by_xpath("//div[@id='settings_sim_nickname']/div/div/div/div[2]")
    init_sim_nickname_value = lbl_sim_nickname.text

    txt_sim_nickname = driver.find_element_by_xpath("//input[@id='my_amaysim2_setting_phone_label']")
    txt_sim_nickname.clear()

    if init_sim_nickname_value == 'testing':
        txt_sim_nickname.send_keys("autotest_rspec")
        validator = "autotest_rspec"
    else:
        txt_sim_nickname.send_keys("testing")
        validator = "testing"

    btn_save = driver.find_element_by_xpath("//input[@value='Save']")
    btn_save.click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@id='settings_sim_nickname']/div/div/div/div[2]")))

    lbl_sim_nickname = driver.find_element_by_xpath("//div[@id='settings_sim_nickname']/div/div/div/div[2]")
    assert lbl_sim_nickname.text == validator

def test_Cancel_ChangeSimName(env_setup):
    # Editing Sim Name
    element_edit_sim_nickname = driver.find_element_by_xpath("//*[contains(@id, 'edit_settings_phone_label')]")
    element_edit_sim_nickname.click()

    lbl_sim_nickname = driver.find_element_by_xpath("//div[@id='settings_sim_nickname']/div/div/div/div[2]")
    init_sim_nickname_value = lbl_sim_nickname.text

    txt_sim_nickname = driver.find_element_by_xpath("//input[@id='my_amaysim2_setting_phone_label']")
    txt_sim_nickname.clear()

    if init_sim_nickname_value == 'testing':
        txt_sim_nickname.send_keys("autotest_rspec")
    else:
        txt_sim_nickname.send_keys("testing")

    # Cancel Changes
    link_cancel = driver.find_element_by_xpath("//*[@id='show_settings_sim_nickname']")
    link_cancel.click()

    lbl_sim_nickname = driver.find_element_by_xpath("//div[@id='settings_sim_nickname']/div/div/div/div[2]")
    assert lbl_sim_nickname.text == init_sim_nickname_value

def test_EditRechargePin(env_setup):
    # Editing Recharge Pin//input[@id='my_amaysim2_setting_topup_pw'
    lbl_recharge_pin = driver.find_element_by_xpath("//div[@id='settings_recharge_pin']/div/div/div/div/div[2]")
    init_recharge_pin_value = lbl_recharge_pin.text

    element_edit_recharge_pin = driver.find_element_by_xpath("//*[contains(@id, 'edit_settings_recharge_pin')]")
    element_edit_recharge_pin.click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@value='Save']")))

    txt_recharge_pin = driver.find_element_by_xpath("//input[@id='my_amaysim2_setting_topup_pw']")
    txt_recharge_pin.clear()

    if init_recharge_pin_value == '1234':
        validator = "4321"
        txt_recharge_pin.send_keys(validator)

    else:
        validator = "1234"
        txt_recharge_pin.send_keys(validator)

    btn_save = driver.find_element_by_xpath("//input[@value='Save']")
    btn_save.click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@id='settings_recharge_pin']/div/div/div/div/div[2]")))

    lbl_recharge_pin = driver.find_element_by_xpath("//div[@id='settings_recharge_pin']/div/div/div/div/div[2]")
    assert lbl_recharge_pin.text == validator

def test_Cancel_EditRechargePin(env_setup):
    # Editing Recharge Pin//input[@id='my_amaysim2_setting_topup_pw'
    lbl_recharge_pin = driver.find_element_by_xpath("//div[@id='settings_recharge_pin']/div/div/div/div/div[2]")
    init_recharge_pin_value = lbl_recharge_pin.text

    element_edit_recharge_pin = driver.find_element_by_xpath("//*[contains(@id, 'edit_settings_recharge_pin')]")
    element_edit_recharge_pin.click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@value='Save']")))

    txt_recharge_pin = driver.find_element_by_xpath("//input[@id='my_amaysim2_setting_topup_pw']")
    txt_recharge_pin.clear()

    if init_recharge_pin_value == '1234':
        txt_recharge_pin.send_keys("4321")

    else:
        txt_recharge_pin.send_keys("1234")

    link_cancel = driver.find_element_by_xpath("//*[@id='edit_settings_topup_password']/div[3]/div/div/a")
    link_cancel.click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@id='settings_recharge_pin']/div/div/div/div/div[2]")))

    lbl_recharge_pin = driver.find_element_by_xpath("//div[@id='settings_recharge_pin']/div/div/div/div/div[2]")
    assert lbl_recharge_pin.text == init_recharge_pin_value