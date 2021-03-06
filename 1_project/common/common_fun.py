from baseViews.baseView import BaseView
from common.desired_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException
import logging
from selenium.webdriver.common.by import By
import time,os
import csv

class Common(BaseView):
    cancelBtn=(By.ID,'android:id/button2')
    skipBtn=(By.ID,'com.tal.kaoyan:id/tv_skip')
    wemedia_cacel=(By.ID,'com.tal.kaoyan:id/ivAdViewClose')
    agreeBtn = (By.ID, "com.tal.kaoyan:id/tip_commit")

    def check_agreeBtn(self):
        logging.info('===============check agreeBtn==========================')

        try:
            agreeBtn = self.driver.find_element_by_id("com.tal.kaoyan:id/tip_commit")
        except NoSuchElementException:
            logging.info('no agreeBtn')
        else:
            agreeBtn.click()

    def check_okBtn(self):
        logging.info('===============check okBtn=====================')

        try:
            okBtn = self.driver.find_element_by_id("com.tal.kaoyan:id/tv_ok")
        except NoSuchElementException:
            logging.info('no okBtn')
        else:
            okBtn.click()

    def check_tiyanBtn(self):
        logging.info('======================check tiyanBtn========================')

        try:
            tiyanBtn = self.driver.find_element_by_id("com.tal.kaoyan:id/activity_splash_guidfinish")
        except NoSuchElementException:
            logging.info('no tiyanBtn')
        else:
            tiyanBtn.click()

    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    def swipeLeft(self):
        logging.info('swipeLeft')
        l = self.get_size()
        x1 = int(l[0] * 0.9)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.1)
        self.swipe(x1, y1, x2, y1, 1000)

    def getTime(self):
        self.now=time.strftime("%Y-%m-%d %H_%M_%S")
        return self.now

    def getScreenShot(self,module):
        time=self.getTime()
        image_file=os.path.dirname(os.path.dirname(__file__))+'/screenshots/%s_%s.png' %(module,time)

        logging.info('get %s screenshot' %module)
        self.driver.get_screenshot_as_file(image_file)

    def check_market_ad(self):
        logging.info('====check_market_ad====')
        try:
            element = self.driver.find_element(*self.wemedia_cacel)
        except NoSuchElementException:
            pass
        else:
            logging.info('close market ad')
            element.click()

    def get_csv_data(self,csv_file,line):
        logging.info('=====get_csv_data======')
        with open(csv_file,'r',encoding='utf-8-sig') as file:
            reader=csv.reader(file)
            for index,row in enumerate(reader,1):
                if index==line:
                    return row

if __name__ == '__main__':
    driver=appium_desired()
    com=Common(driver)
    # com.check_cancelBtn()
    # com.check_skipBtn()
    com.swipeLeft()
    com.getScreenShot('startApp')

    list = ["???", "???", "??????", "??????", "??????"]
    # for i in range(len(list)):
        # print(i, list[i])

    list1 = ["???", "???", "??????", "??????", "??????"]
    # for index, item in enumerate(list1):
    #     print(index, item)






