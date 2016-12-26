# -*- coding:UTF-8 -*-

my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # 1bs
my_eyss = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "let's talk about %s. " % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyss,my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# 加分题4 1英寸=2.54厘米 1磅=0.4536千克

my_height_centimeter = my_height*2.54
my_weight_kelomrtre = my_weight*0.4536

print "Let's talk about you."
your_name = raw_input("type your name:")
print "Hi,%r!" % your_name
print "You know what? I'm %.2f centermeters tall. And I'm %.2f kilometres heavy." % (my_height_centimeter, my_weight_kelomrtre)


# this line is tricky,try to get it exactly tight
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)
