# -*- coding: utf-8 -*-
# 提醒

# 设置一个变量a = 命令open （）里是打开的内容
def open_read_txt(a):
	a = open(weather_info.txt)
# 读a，也就是打开的文件。a.read() 是指read a
	print (a.read())



	

open_read_txt


# 格式化字符串 



# 设置变量city = 命令input（） 输入提醒 
city = input("请输入你查询的城市")
print ("%s" % city)
elements = []

for city in open_read_txt(city):
	print ("%s" % city)
	elements.append(city)

for i in elements:
	print ("%s" % i)

# 要加一个循环，能不断出现 city = input("请输入你查询的城市")