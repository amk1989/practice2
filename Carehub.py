import time
from appium import webdriver
# from appium.options.android import UiAutomator2Options
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='emulator-5554',
    appPackage='com.hhaexchange.aide',
    appActivity='com.hhaexchange.carehub.ui.activities.MainActivity',
    language='en',
    locale='US'

)
appium_server_url = 'http://127.0.0.1:4723'


driver = webdriver.Remote(appium_server_url, options=AppiumOptions().load_capabilities(capabilities))
time.sleep(4)

#el = driver.find_element(by=AppiumBy.XPATH, value='new UiSelector().text("Enter your Login")')
#el = driver.find_element(by=AppiumBy.XPATH, value='(//android.widget.TextView[@text="Login"])[1]').click()

#el = driver.find_element(by=AppiumBy.XPATH, value='(//android.widget.TextView[@text="Login"])[1]').send_keys("123")

#el.click()
#el.send_keys('amey.k@yahoo.com')
el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(0)').send_keys("amkulkarni@hhaexchange.com")
time.sleep(5)
el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(1)').send_keys("Winjit@123")
time.sleep(5)
el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(0)').click()
time.sleep(5)
el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(1)').click()
time.sleep(5)
#new UiSelector().className("android.widget.EditText").instance(0)
driver.quit()