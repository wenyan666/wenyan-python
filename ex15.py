# -*- coding:UTF-8 -*-
from sys import argv
# 改变txt = open（filename）的位置（在read之前）会影响结果吗？不会
script, filename = argv
# the txt = open(filename)'s original position

print "Here's your file %r:" % filename
txt = open(filename)   # the new position of txt = open(filename), nothing happened
print txt.read()

print "Please type your filename again:"
txt_again = raw_input(">")
# 自己写这里写成了open（filename）而不是open（txt_again）,可能是对open原理有点模糊
txt_again = open(txt_again)
print txt_again.read()
