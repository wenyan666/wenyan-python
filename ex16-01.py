# -*- coding:UTF-8 -*-
from sys import argv

script, filename = argv

txt = open(filename)

print "If you want to read %r?" % filename
print "If you don't want, hit CTRL-C(^C)."
print "If you want that, hit YES."
raw_input("?")

print "Here is your file %r:" % filename
print txt.read() 
# 由于不熟练，在括号里面加了filename。导致无法读取文件

print "Type your filename again:"
file_again = raw_input(">")

txt_again = open(filename)

print txt_again.read()
# 加分练习
print "And finally, we close it."
txt.close() # 是从ex16中复制过来的代码，target没有改成“txt”导致报错
