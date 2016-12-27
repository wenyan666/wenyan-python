# -*- coding:UTF-8 -*-
# %d 是格式化整数，看样子可以直接在后面输入数值？
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
# %s是格式化字符串
y = "Those who know %s and those who %s." %(binary,do_not)
print x
print y
# %r是把x等号后面的打印出来，不管什么；%s 为嘛要加上单引号才能显示和%r一样的效果。
print "I said: %r." % x 
print "I slso said: '%s'." % y
# 这里为嘛灭有给False加双引号？是因为false是python自动识别的关键字？
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

# 还是给变量赋值
w = "This is the left side of..."
e = "a string with a right side."
# 组合字符串？
print w + e
# +就是执行了正常的加法吧，只不过不是数字就直接连接在一起了，若是数字肯定就直接加合了
