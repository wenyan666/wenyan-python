the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes therough a list
for number in the_count:
    print ("This is count %d" % number)

# same as above
for fruit in fruits:
    print ("A fruit of type: %s" % fruit)

# also we can go through mixed list too
# notice we have to use %r since we don't know what's in it
for x in change:
    print ("I got %r" % x)

# we can also build lists, first start with empty ones
elemengts = []
# then use the range function to do 0 to 5 counts
for y in range(0, 6):
    print ("Adding %d to the list." % y)
    # append is a function that lists Understand
    elemengts.append(y)

for i in elemengts:
    print ("Elemengt was: %d" % i)

why = []
why.append(y)
for i in why:
    print("Why just give me one number: %d?" %i)

another = range(0, 3)
for i in another:
    print ("Skip the range and get: %d" % i)
