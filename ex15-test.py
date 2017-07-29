# 用 argv参数变量， 获取文件名。 解包为命令名和文件名
from sys import argv

script, filename = argv

# open是一个命令，跟脚本、input等命令类似，接受一个参数，返回一个值，讲这个值赋予一个变量。
# 在txt上调用了open这个函数  用等号，并且文件名也有txt


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