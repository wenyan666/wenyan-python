# -*- coding:UTF-8 -*-
formatter = "%r %r %r %r"
print formatter % (1,2,3,4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
   "I had this thing.",
   "That you could type up right.",
   "But it didn't sing.",
   "So I said goodnight."
)
# 最后一行既有单引号，又有双引号，发现把don't中的‘去掉之后就显示单引号了。可能是这个原因。
print '''
I learn some new thing in ex9,so I back here to do some excise.
I wanna know what happed if I use three quotes.
Is it the same with three double-quetes?
I will see.
'''
