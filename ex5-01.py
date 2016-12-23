# -*- coding:UTF-8 -*-

name = 'Zed A. Shaw'
age = 35 # not a lie
height = 180 # cm
weight = 80 # 1kg
eyss = 'Blue'
teeth = 'White'
hair = 'Brown'

print "let's talk about %r. " % name
print "He's %rcm tall." % height
print "He's %rkg heavy." % weight
print "Actually that's not too heavy."
print "He's got %r eyes and %r hair." % (eyss,hair)
print "His teeth are usually %r depending on the coffee." % teeth

# this line is tricky,try to get it exactly tight
print "If I add %r, %r, and %r I get %r." % (age, height, weight, age + height + weight)
