# _*_ coding: utf-8 _*_
from appium import webdriver
import yaml

file = open("desired_caps.yaml", Loader=yaml.FullLoader)
data = yaml.load(file)

desired_caps = {}
desired_caps['platformName'] = data['Android']
desired_caps['deviceName'] = data['127.0.0.1:62001']