import time
from appium import webdriver
# from appium.options.android import UiAutomator2Options
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='emulator-5554',
    appPackage='com.hhaexchange.uma',
    appActivity='crc6496ce20f433df0767.MainActivity',
    language='en',
    locale='US'
)
appium_server_url = 'http://127.0.0.1:4723'
driver = webdriver.Remote(appium_server_url, options=AppiumOptions().load_capabilities(capabilities))
time.sleep(4)
#el = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text("HHAeXchange+").instance(0)')
#el.click()
