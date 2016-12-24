# -*- coding:UTF-8 -*-
# 从系统文件中导入参数变量
from sys import argv
# 给参数变量赋值
script, filename = argv
# txt变量赋值为open参数变量filename
txt = open(filename)
# 打印需要显示的部分，并执行变量命令
print "Here is your file %r:" % filename
print txt.read()
# 邀请用户再次输入参数变量filename，给新的命令赋值为open
print "Type the filename again:"
file_again = raw_input(">")
# 给新的变量赋值
txt_again = open(file_again)
# 执行新的变量
print txt_again.read()
