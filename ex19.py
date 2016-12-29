# -*- coding:UTF-8 -*-
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d crackers!" % boxes_of_crackers
    print "Man that's enough for a paity!"
    print "Get a blanket.\n"
	
print "We can just give the functions member directly:"
cheese_and_crackers(20,30)
 
print "Or, we can use variable from our script:"
accout_of_cheese = 10
accout_of_crackers = 50

cheese_and_crackers(accout_of_cheese, accout_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10+20, 5+6)

print "And we can combine the two, variable and math:"
cheese_and_crackers(accout_of_cheese+100, accout_of_crackers+1000)


'''
遇到了unexpected indent的问题，一只运行不起来。查了之后发现是tab和空格的问题。体会到了python的严格！
函数后面记得加：
加分题见ex.19s.py
'''
