# _*_ coding: utf-8 _*_
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

desired_caps = {}

desired_caps["platformName"] = 'Android'

desired_caps['deviceName'] = '127.0.0.1:62001'

desired_caps['platformVersion'] = '7.1.2'

desired_caps['app'] = r'E:\workspace\Appium_work\matiars\2_2a3b6ae08f8768ccb2d820753cabb474.apk'
desired_caps['appPackage'] = 'com.tal.kaoyan'
desired_caps['appActivity'] = '.ui.activity.SplashActivity'
desired_caps['noReset'] = 'False'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)




def check_agreeBtn():
    print('check agreeBtn')

    try:
        agreeBtn = driver.find_element_by_id("com.tal.kaoyan:id/tip_commit")
    except NoSuchElementException:
        print('no agreeBtn')
    else:
        agreeBtn.click()

def check_okBtn():
    print('check okBtn')

    try:
        okBtn = driver.find_element_by_id("com.tal.kaoyan:id/tv_ok")
    except NoSuchElementException:
        print('no okBtn')
    else:
        okBtn.click()

check_agreeBtn()
check_okBtn()



