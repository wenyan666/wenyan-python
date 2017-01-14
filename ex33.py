i = 0
numbers = []

while i < 6:
    print ("At the top i is %d" %i)
    numbers.append(i)

    i += 1
    print ("Numbers now: ", numbers)
    print ("At the bottom i is %d" % i)

print ("The numbers:")

for num in numbers:
    print (num)
# 默写的时候把while写成了if，最后的结果为[0]，循环就执行了一次
