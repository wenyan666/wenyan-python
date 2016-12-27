# -*- coding:UTF-8 -*-
# 加分练习3：将raw_input和argv一起使用，让你的脚本从用户手上得到更多的输入
from sys import argv

script, first, second, third = argv

print "Your script is called:" , script
print "Your first variable is: " , first
print "Your second variable is:" , second
print "Your third variable is:" , third

fell = raw_input("What\'s the felling of having you first script?")
print "How about to type more code as you like?",
type_more = raw_input()


# 调用的参数和参数名称必须一致，输入的参数数量也必须刚刚好，不然都会报错
