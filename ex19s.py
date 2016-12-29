# -*- coding:UTF-8 -*-
def favorite(user_name, interest, be_fond_of):
    print "Hi, %r, nice to meet you. I'd like to talk about my favorite." % user_name
    print "I like %r, and I like %r." % (interest, be_fond_of)
    print "That's cool, doesn't it?\n"
	
#1.give the function directly
favorite("wenyan", "swiming", "runing")

#2.give the function variable by script
name = "xiaoming"
hobby = "typing"
fond_of = "coding"

favorite(name, hobby, fond_of)

#3.give the function by math
favorite(2+3, 7, 9)

#4.give the function by combine math and variable
favorite(24/12, 6, 8)

#5.give the function by raw_input
who = raw_input("who?")
like = raw_input("tell me what's you like:")
love = raw_input("now tell me your love:")

favorite(who, like, love)

#6.give the function by raw_input and math
x = raw_input(">")
y = raw_input(">")

favorite(x, y, "apple")

#7.give the function by*
favorite("yeah"*5, "singing", "dancing"*3)

#8.give the function by raw_input directly?
favorite(raw_input("test1:"), raw_input("test2:"), raw_input("test3:"))

'''
又忘记了def后面的冒号：。。。
直接给函数的时候，是字符串的时候需要加双引号
最后一句记得加\n分行，不然会很乱
字符串和数字不能直接加合，会报错，但是可以用*重复	n次
'''
