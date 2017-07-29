# 从 系统 import 参数变量（就是命令行后面要加一个词，这个词在命令行中会被使用）
# 要在命令行输入 python ex14.py(script name) 后 空格输入。 
from sys import argv

# 第一个必须是script ，隔开空格， 自定义一个变量名。 这两个总共是argv的意思。
# 解包

script, user_name = argv


# 提醒input的词，也可以直接替代下面input（）里的prompt
prompt = '> '

# 格式化字符
print ("Hi %s, I'm the %s script." % (user_name, script))
print ("I'd like to ask you a few questions.")
print ("Do you like me %s?" % user_name)
likes = input(prompt)

print ("Where do you live %s?" % user_name)
lives = input(prompt)

print ("What kind of computer do you have?")
computer = input(prompt)

print ("""
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer))

# 目前看在weather项目中没什么用，
# 联想到def功能，可能可以从其他脚本中import其中的某个def定义功能？

