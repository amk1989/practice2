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
    locale='US',
    )
appium_server_url = 'http://127.0.0.1:4723'


driver = webdriver.Remote(appium_server_url, options=AppiumOptions().load_capabilities(capabilities))
time.sleep(4)
el = driver.find_element(by=AppiumBy.XPATH, value= "//*[@text='Allow']").click()
el = driver.find_element(by=AppiumBy.XPATH, value='//androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.widget.ImageView').click()
el = driver.find_element(AppiumBy.ID,"com.hhaexchange.uma:id/logo_login").click()
el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("EmailField")').send_keys("amkulkarni@hhaexchange.com")
el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("PasswordField")').send_keys("Winjit@123")
el = driver.find_element(AppiumBy.ID,"com.hhaexchange.uma:id/ValidationEntry_Eyeicon_Button").click()
el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.hhaexchange.uma:id/Login_Login_Button")').click()
el= driver.find_element(by=AppiumBy.XPATH,value= "//*[contains(@index, '7')]").click()
el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.FrameLayout").instance(8)').click()
#el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("")').click()
#el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("AWS ENT Agency_II(Mobile Team TX Office)")').click()