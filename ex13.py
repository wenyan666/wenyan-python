# -*- coding:UTF-8 -*-
from sys import argv

script, first, second, third = argv


print "Your script is called:" , script
print "Your first variable is: " , first
print "Your second variable is:" , second
print "Your third variable is:" , third

# 这里的参数变量都用逗号连接，改成用%s还有效么？已测。可以！
# 这里第一行输入的为什么显示的文件名？原理是什么？  日后再解决

script, one, two, three = argv

print "test:%s" % script
print "test:%s" % one
print "test:%s" % two
print "test:%s" %three
