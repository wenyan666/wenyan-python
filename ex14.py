# -*- coding:UTF-8 -*-
from sys import argv
# 加分练习3，给脚本多加了一个变量funny
script, user_name, funny = argv
# 加分练习2，修改prompt的内容运行
prompt = "type here >"

print "Hi,%s, I\'m %s script.I\'m %s to meet you." %(user_name, script, funny)
print "I will ask you few questions."
print "Do you like me?" , user_name
likes = raw_input(prompt)

print "Where are you live?"
lives = raw_input(prompt)

print " Could you tell me which computer you using?"
computer = raw_input(prompt)

print "OK,%s,you said %s about like me." % (user_name, likes)
print "You live %s, sure don't know where is here." % lives
print "you said you have %s computer.that's coll!" % computer
# 默写的，和原书中的内容和方法不同。但是可以正常运行起来。
print '''
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
''' % (likes, lives, computer)

# 1把%s写成了%S，混用两种调用参数变量，同时使用%s和逗号连接，结果%s被直接打印出来
# 有的打印出来有单引号，有的没有。直接用逗号引用的参数变量没有单引号
