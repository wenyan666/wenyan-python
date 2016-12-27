# -*- coding:UTF-8 -*-
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So,you're %r old, %r tall and %r heavy." %(age,height,weight)

# raw_input：读取一行输入的字符串
# 其他用法
job = raw_input("What\'s your work for?")
# 在输入6'25"的时候为嘛后面的"不用转义字符呢？
