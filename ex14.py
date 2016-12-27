# -*- coding:UTF-8 -*-
from sys import argv

script, user_name = argv
prompt = ">"

print "Hi,%s, I\'m %s script." %(user_name, script)
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
# 默写的，和原书中略有不同。但是可以正常运行起来。不错。下面是原书中的代码
print '''
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
''' % (likes, lives, computer)

# 1把%s写成了%S，混用两种调用参数变量，同时使用%s和逗号连接，结果%s被直接打印出来
# 有的打印出来有单引号，有的没有。直接用逗号引用的参数变量没有单引号
