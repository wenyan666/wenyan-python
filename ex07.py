# -*- coding:UTF-8 -*-
print "Mary had a little lamb."
print "Its fleece was white as %s." % 'snow'
print "And everywhere that Mary went."
print "." * 10 # what'd that do? 这个把.直接乘以10，也就是重复了10次

# 为什么是end1-12？我可以改为别的吗？比如start1-12甚至其他？多个字母是否也会直接连接？
# 这些都完全没有问题，常见问答中已经解决了全部问题
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"
start1 = "!"

# watch that comma at the end. try removity it to see what happens
# 去掉之后，变成了两行。逗号的作用就是把两行连接成一行。
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12 + start1 
