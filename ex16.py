# -*- coding:UTF-8 -*-
from sys import argv

script, filename = argv

print "Now I'm going to eraser you file %r." % filename
print "If you don't want that, hit CTRL-C(^C)."
print "If you want that, hit RETERN."
# 这地方为嘛不用在前面加一个变量来定义？而是直接用raw_input?  想多了，是可以直接用的。
raw_input("Tell me you answer?")
# 以write模式打开文件
print "Openging the file..."
target = open(filename, 'w')

print "Truncate the file, goodbye." 
print "Now I ask you to type three new lines for it:"
# 让用户输入三个句子
line1 = raw_input("line1:")
line2 = raw_input("line2:")
line3 = raw_input("line3:")

print "I'm going to write there to the file."
# 为啥line1-3不用双引号，而\n要用双引号呢？是因为line1-3提前定义过了？
# 错把错号写成了等号，导致‘file’object attribute ‘write’ is read-only
# 向文件内写入上面三行
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# 在一行中输入
# 刚开始把%(line1, line2, line3)放在了write括号外面，程序报错
target.write("%s\n%s\n%s\n" % (line1, line2, line3)) 
print "And finally, we close it."

target.close()

'''
加分题
2.  from sys import argv
    script, filename = argv
	txt = open(filename)
	print txt.read()
	
3.target.write("%s\n%s\n%s\n" % (line1, line2, line3)) 
  这个是在网上查找的。第一次自己尝试写得不对，报错。值得多看几遍把这个记住。
  write括号内是一个整体，提取文件也需要在内部完成这样理解对吗？
  
4.因为open默认打开方式是只打开，不可以写入。
  不需要在target.truncate，因为’w'模式打开文件的时候会自动truncate文件。  
'''
