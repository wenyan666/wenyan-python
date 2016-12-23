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

# 附加练习
while True:
   for i in ["/","-","|","\\","|"]:
      print "%s\r" % i,
   
