# _*_ coding: utf-8 _*_
from find_element.capability import driver

driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.tal.kaoyan:id/login_email_edittext")').send_keys("asd")