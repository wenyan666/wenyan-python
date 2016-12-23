# -*- coding:UTF-8 -*-
# 给变量赋值
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." %(binary,do_not)
# 直接输出变量x和y的值
print x
print y
# 在字符串里面显示变量值（格式化的字符串）
print "I said: %r." % x 
print "I slso said: '%s'." % y
# 给新的变量赋值
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
# 直接输出新的变量值
print joke_evaluation % hilarious
# 还是给变量赋值
w = "This is the left side of..."
e = "a string with a right side."
# 组合字符串？
print w + e
