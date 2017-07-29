# -*- coding: utf-8 -*-
# import os

data = {}
s_history = []


def init():
    # 初始化天气数据库
     with open('weather_info.txt', 'rt') as f:
        for line in f:
            str = line.split(',', 1)  # 字符串以逗号分隔
            data[str[0]] = str[1]
    return data


def option():
    keyword = input(" 请输入要查询天气的城市名称：")
    search(keyword)


def search(keyword):
    if keyword == "history":
        history(keyword)
    elif keyword == "help" or keyword == "h":
        help()
    elif keyword == "q" or keyword == "quit":
        quit()
    elif keyword in data:
        print(keyword + " 的天气是: " + data[keyword])
        record(keyword)
    else:
        print(" 抱歉, 没有收录该城市."+'\n')
        option()


def record(keyword):
    if keyword in data:
        search_tmp = keyword + ',' + data[keyword]
        s_history.append(search_tmp.rstrip())
    # if not os.path.exists('log.txt'):
        # with open('log.txt', 'wt') as f:
        #     f.write(search_tmp)
    option()


def history(keyword):
    if s_history == []:
        print(" 暂无查询历史 " + '\n')
    else:
        for item in s_history:
            print(item)
        # f = open('log.txt', 'rt')
        # f.read()
    option()


def help():
    print(''.rjust(50, '-'))
    print("history".rjust(20), " 获取查询历史 ".rjust(20))
    print("quit".rjust(20), " 退出天气查询 ".rjust(20))
    print(''.rjust(50, '-'))
    option()


def quit():
    print(" 感谢使用！")
    return


init()
option()