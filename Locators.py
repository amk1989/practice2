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
    appPackage='com.hhaexchange.uma',
    appActivity='crc6496ce20f433df0767.MainActivity',
    language='en',
    locale='US'
)
appium_server_url = 'http://127.0.0.1:4723'


driver = webdriver.Remote(appium_server_url, options=AppiumOptions().load_capabilities(capabilities))
time.sleep(4)
#el= driver.find_element(by.id("com.hhaexchange.uma:id/en-US")).click();
el = driver.find_element(by=AppiumBy.XPATH, value='//androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.widget.ImageView').click()

#el = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="com.hhaexchange.uma:id/SignUpButton"]').click()
el = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="com.hhaexchange.uma:id/Login_LanguagePicker_Button1"]').click()
