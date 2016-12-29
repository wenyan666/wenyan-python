# -*- coding:UTF-8 -*-
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "I will copy %r to %r." % (from_file, to_file)

in_file = open(from_file)
indata = in_file.read()

print "There are %d bytes in this file." % len(indata)

print "Does the outfile exists? %r?" % exists(to_file)
print "Hit RETERN to continue, hit CTRL-C(^C) to abor."
raw_input("?")

out_file = open(to_file,'w')
out_file.write(indata)

print "Alright, all done."

in_file.close()
out_file.close()


'''
加分习题
1.import用来引入各种模块、包，从而使用其中包含的方法，定义的数据等。

3.把print的部分全部去掉，然后通过如数学思维的等量代换？
  open(to_file,'w').write(open(from_file).rend()) 
  
5.cat这个命令是将两个文件“连接（com*cat*enate)"到一起，不过实际上它最大的用途是打印文件内容到屏幕上。
  我的Windows里面居然有cat这个命令，而且正常运行了。

6. close()是为了释放资源。如果不close()，那就要等到垃圾回收时，自动释放资源。垃圾回收的时机是不确定的，也无法控制的。
'''
