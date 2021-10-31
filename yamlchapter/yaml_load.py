# _*_ coding: utf-8 _*_
import yaml

file=open("familyinfo.yaml")
data = yaml.load(file, Loader=yaml.FullLoader)

print(data)