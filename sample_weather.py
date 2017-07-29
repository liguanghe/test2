#!/usr/bin/python
# -*- coding: utf-8 -*-
# (C) 2014 Yunlong Zhou <reaper888@yeah.net>      
# Under licence  GPLv2
# File :   getweather.py 
# Introduction:      
#       This script is using for query weather of a city  
# Last Modify:
#       2014-7-5
# Useage :
#       See README

import urllib2
import sys
import os
import shlex, subprocess

chinese_flag = 1

def add_sys_argv():
	leng = len(sys.argv)
	arg_list = []
	for i in range(1, leng):
		arg_list.append(sys.argv[i])
	return arg_list

def check_arument_in(argu, arg_list):
    for i in range(0, len(arg_list)):
        if arg_list[i].find(argu) != -1 :
			return i
    return -1


def print_usage():
	global chinese_flag
	if chinese_flag:
		print """名称:
    getweather -- 获取中国城市的天气情况 \n
用法: 
    [python] getweather.py [结果选项] 城市名\n
结果选项:
    -h,      打印这个帮助文档（独自工作，不能和其他选项/城市名混合使用）
    -zh,     以中文打印城市天气信息
    -en,     以英文打印城市天气信息
注意:
    最多只能使用一个结果选项，如果不使用选项，默认输出结果为中文\n
作者:
    Zhou Yunlong <reaper888@yeah.net>
"""
	else:
		print """NAME:
    get weather of a city(in China) \n
SYNOPSIS: 
    [python] getweather.py [OPTION] cityname \n
DESCRIPTION:
    -h,      Print this help (work alone, won't work while be mixed with other argu)
	-zh,     Print the weather result in Chinese
    -en,     Print the weather result in English
NOTE:
    Support atmost one OPTION, if without OPTION(only cityname), the result will default in Chinese\n
AUTHOR:
    Zhou Yunlong <reaper888@yeah.net>
"""
	sys.exit()


def get_content(string):
	return string.split('":"')[1].strip("\"")

def use_urllib2(url):  
	try:  
		f = urllib2.urlopen(url, timeout=5).read()  
	except urllib2.URLError, e:  
		print e.reason  
		return -1
	else:
		return f

def get_city_code(test_city, citycode_f = "citycode"):
	global chinese_flag
	if os.path.exists(citycode_f):
		if "市" in test_city:
			test_city = test_city.split("市")[0]
	
		ret = os.system("grep %s %s >/dev/null" % (test_city,citycode_f))
		if ret == 0:
			grep_content = os.popen("grep %s %s" % (test_city,citycode_f)).read()
			city_code = grep_content.split("=")[0]
#			print "Now get city: \"%s\" code is %s " % (test_city, city_code)
	 		return city_code
		else:
			if chinese_flag:
				print "\t搜索\"%s\"失败，请重新搜索（市级城市）" % test_city
			else:
				print "\tSearch city \"%s\" fail, please check the city and retry(at lease city size)" % test_city
			sys.exit(-1)
	else:
		if chinese_flag:
			print "当前目录没有\"%s\"文件，无法搜索" % citycode_f
		else:
			print "There is no \"%s\" file in current directory" % citycode_f
		sys.exit(-1)


def get_argu_return_citycode():
	global chinese_flag
	sys_arg_list = add_sys_argv()
	list_len = len(sys_arg_list)
	help_find = check_arument_in('-h', sys_arg_list)
	zh_find = check_arument_in('-zh', sys_arg_list)
	en_find = check_arument_in('-en', sys_arg_list)
	if list_len == 1:
		if help_find != -1:
			print_usage()
		else:
			if chinese_flag:
				print "你只使用一个参数\"%s\"（且不是\"-h\"），将其作为城市名搜索" % sys_arg_list[0]
			else:
				print "You use one flag \"%s\", and it's not \"-h\", we will search it as city name" % sys_arg_list[0]
			city_code = get_city_code(sys_arg_list[0])
	elif list_len == 2:
		if zh_find != -1 and en_find == -1 and help_find == -1:
			chinese_flag = 1
			city_name = sys_arg_list[list_len - zh_find -1]
			city_code = get_city_code(city_name)
		elif en_find != -1 and zh_find == -1 and help_find == -1:
			chinese_flag = 0
			city_name = sys_arg_list[list_len - en_find -1]
			city_code = get_city_code(city_name)
		else:
			if chinese_flag:
				print "你选择了错误的结果选项，请重新输入或者使用'-h'查看如何使用"
			else:
				print "You use wrong arguments, please input again or learn howto with '-h' argument"
			sys.exit(-1)
	else:
		if chinese_flag:
			print "你使用了多于2个结果选项，请重新输入或者使用'-h'查看如何使用"
		else:
			print "You use more than two arguments, please input again or learn howto with '-h' argument"
		sys.exit(-1)
	return city_code			


def get_city_weather(city_code):
	global chinese_flag
	weather_url = "http://www.weather.com.cn/data/sk/%s.html" % city_code
	wea_str = use_urllib2(weather_url)
	if wea_str == -1:
		if chinese_flag:
			print "对不起，暂时搜寻不到此城市信息，请检查或稍后再试"
		else:
			print "Sorry that I can't find the weather info of this city now, please check or retry"
		sys.exit(-1)
	else:
		wea_list = wea_str.split(",")
		for item in wea_list:
			if "city" in item and "cityid" not in item:
				city_name = get_content(item)
			if "temp" in item:
				city_temp = get_content(item)
			if "time" in item:
				update_time = get_content(item)
	info_url = "http://www.weather.com.cn/data/cityinfo/%s.html" % city_code
	info_str = use_urllib2(info_url)
	if info_str == -1:
		if chinese_flag:
			print "对不起，暂时搜寻不到此城市信息，请检查或稍后再试" 
		else:
			print "Sorry that I can't find the weather info of this city now, please check or retry"
		sys.exit(-1)
	else:
		info_list = info_str.split(",")
		for item in info_list:
			if "temp1" in item:
				low_temp = get_content(item)
			if "temp2" in item:
				high_temp = get_content(item)
			if "weather" in item:
				today_weather = get_content(item)
	return city_name, city_temp, update_time, low_temp, high_temp, today_weather

def print_weather_to_user(city_name, city_temp, update_time, low_temp, high_temp, today_weather, city_code):
	global chinese_flag
	if low_temp > high_temp:
		t = low_temp
		low_temp = high_temp
		high_temp = t
	if chinese_flag:
		print """\t今天"%s市"天气是:
\t========================
\t今日天气 : %s
\t实时温度 : %s℃ 
\t今日的温度区间 : %s ~ %s
\t更新时间: %s
\t========================
\t更多请参见：http://www.weather.com.cn/weather/%s.shtml""" % (city_name, today_weather, city_temp, low_temp, high_temp, update_time, city_code)

	else:
		print """\tThe weather info of "%s":
\t========================
\tThe weather today is : %s
\tCurrenttly the temperature is : %s℃ 
\tThe weather section today is : %s ~ %s
\tUpdate time: %s
\t========================
\tSee more: http://en.weather.com.cn/weather/%s.shtml""" % (city_name, today_weather, city_temp, low_temp, high_temp, update_time, city_code)



############# Real start here
city_code = get_argu_return_citycode()
city_weather = get_city_weather(city_code)
print_weather_to_user(city_weather[0], city_weather[1], city_weather[2], city_weather[3],city_weather[4], city_weather[5], city_code)


