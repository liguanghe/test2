# 从sys模块中提取（import）参数变量（argv），就是整个命令
from sys import argv

# 解包参数变量，命令名，文件
script, filename = argv

# 打印，%r是文件名
print ("We're going to erase %r." % filename)
print ("If you don't want that, hit CTRL-C (^C).")
print ("If you do want that, hit RETURN.")

# input用？提示
input("?")

print ("Opening the file...")
# target 是目标的意思，赋值 open命令 文件名，'w'是可写的意思。 目标是打开文件
target = open(filename, 'w')

print ("Truncating the file. Goodbye!")
# target是目标，紧跟truncate的命令，不带参数和变量的命令用. 否则用=赋值
target.truncate()

print ("Now I'm going to ask you for three line.")

# 赋值，line1 是input的内容，用“line1”提醒
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print ("I'm going to write these to the file.")

# 目标命令write （）里面是写什么什么
target.write (line1)
target.write("\n")
target.write (line2)
target.write("\n")
target.write (line3)
target.write("\n")


print ("And finally, we close it.")
# 目标命令close 所以target很有必要。
target.close()

txt = open(filename)

print ("Here's your file %r" % filename)
# 用. 后面是命令，无需任何参数
print (txt.read())

print ("Type the filename again:")
# 赋值，文件是输入的文件名
file_again = input("> ")

# 赋值，打开命令，file_again 就是input的内容，文件名
txt_again = open(file_again)

# 用. 后面是命令read read也是一个命令，
print (txt_again.read())
