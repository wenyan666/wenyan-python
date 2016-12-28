# -*- coding:UTF-8 -*-
from sys import argv
# 改变txt = open（filename）的位置（在read之前）会影响结果吗？不会
script, filename = argv
# the txt = open(filename)'s original position

print "Here's your file %r:" % filename
txt = open(filename)   # the new position of txt = open(filename), nothing happened
print txt.read(10)
# 加分题8。刚开始在前面加了print，结果打印出来的是none的提示
txt.close()

print "Please type your filename again:"
txt_again = raw_input(">")
# 自己写这里写成了open（filename）而不是open（txt_again）,可能是对open原理有点模糊
txt_again = open(txt_again)
print txt_again.read()

#加分习题7  定义、open、read缺一不可，否则读取不出来
file_more = raw_input("type the filename once again:")
txt_more = open(file_more)
print txt_more.readlines()

file_test = raw_input("type the filename once again:")
txt_test = open(file_more)
print txt_test.readline()

# 加分题8
txt_again.close()

'''
3.函数（function）和方法（method）基本上是一样的，都是事先实现功能的一段代码，少量的区别：
  *函数主要是内部使用，方法主要是暴露给外部使用。
  *函数偏面向过程，方法偏面上对象。
  
5.不分好坏，看场合和具体需求？感觉raw_input与用户的互动性更强。

7.read() 读取全部字节（文件内容），也可以在括号里面添加需要读取的字节数量；
  readline（）读取第一行的字节，也可以在括号里输入数字限定读取的长度；
  readlines（）全部读取，且用\n连接成一行。也可以输入数字限定读取长度。
  
8.善始善终，养成好的程序思维。
'''
