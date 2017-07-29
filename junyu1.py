# Function definition

def dict_maker():
	file = open('weather_info.txt')
	d = {}
	for line in file:
		x = line.split(',')
		a = x[0]
		b = x[1]
		c = len(b) - 1
		b = b[0:c]
		d[a] = b
	return d

def welcome():
    print('''
        ----------
        你好，这里是天气查询中心，请用中文输入您希望了解天气的城市名称进行查询；
        获得更多帮助，请输入 h 或者 help 了解更多；
        退出程序，请输入 exit 或 quit。
        ----------
        ''')

def hint():
    print('请输入指令或您要查询的城市名：')

def help_output():
    print('''
- 中文输入城市名，查询该城市的天气；
- 输入 h 或者 help，获取帮助文档；
- 输入 history，获取查询历史；
- 输入 exit 或 quit，退出天气查询系统。
        ''')

def exit_function():
    history()
    exit()

def history():
    print("It is history")

#简单的判断函数
#def input_check():
#    while True:
#        try:
#            a = input('Plean enter city name:')
#                d[a]
#                break
#        except KeyError:
#            print("Sorry,I don't understand what you mean,please try agian.")
#    return d[a]

def input_check():
    a = input('>>>')
    if a == 'h' or a == 'help':
        help_output()
    elif a == 'exit' or a == 'quit':
        exit_function()
    else:
        while True:
            try:
                    d[a]
                    print('%s 的天气状况为: %s' % (a, d[a]))
                    break
            except KeyError:
                print(" 您的输入有误，请重新输入。")
                break

# Main

d = dict_maker()
welcome()

while True:
    hint()
    input_check()
