# -*- coding:UTF-8 -*-

# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1:%r, arg2: %r." % (arg1, arg2)
	
# OK, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1:%r, arg2:%r" % (arg1, arg2)
	
# or just type one argument
def print_one(arg1):
    print "arg1:%r" % arg1
	
# this is none argument
def print_none():
   print "I got nothin'."
   
print_two("zed", "shaw")
print_two_again("zed", "shaw")
print_one("first")
print_none()


'''
加分习题
def one(who, why, where):
    print "I love %r,becouse he is %r, I meet him in %r." % (who, why, where)
	
def two(what, how):
    print "I'd like learning %r, by %r." % (what, how)
	
one("Manger", "smart", "book")
two("Python", "following the big bug.")
已运行成功。
'''
