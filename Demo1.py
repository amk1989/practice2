from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

cap:Dict[str, Any]={
"appium:appPackage": "com.hhaexchange.uma",
  "appium:appActivity": "crc6496ce20f433df0767.MainActivity",
  "appium:udid": "emulator-5554",
  "platformName": "Android",
  "appium:platformVersion": "15",
  "appium:automationName": "UiAutomator2",
  "appium:app": "C:\\Users\\amey.kulkarni\\Downloads\\0702241800.apk",
  ##"appium:autoGrantPermissions": true,
  ##"appium:appWaitDuration": 30000

}
url = 'http://localhost:4724'
driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
driver.quit()