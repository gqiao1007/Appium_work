# _*_ coding: utf-8 _*_
from appium import webdriver

desired_caps = {}

desired_caps["platformName"] = 'Android'

desired_caps['deviceName'] = '127.0.0.1:62001'

desired_caps['platformVersion'] = '7.1.2'

desired_caps['app'] = r'E:\workspace\Appium_work\matiars\2_2a3b6ae08f8768ccb2d820753cabb474.apk'
desired_caps['appPackage'] = 'com.tal.kaoyan'
desired_caps['appActivity'] = '.ui.activity.SplashActivity'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)



