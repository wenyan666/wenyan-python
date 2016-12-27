# -*- coding:UTF-8 -*-
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll so a list:
\t* Cat food
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# 加分习题3：将转义序列和格式化字符串组合到一起，创建一种更复杂的格式。 
a = 6
b = 480
c = "yeah!"
print "How about \'%r\'/\'%r\'?" % (b, a),b/a
print "%s That\'s coll!" %c

# 附加练习
while True:
   for i in ["/","-","|","\\","|"]:
      print "%s\r" % i,
# 这个还挺神奇的，一直转个不停，也没有办法结束，这是啥？
