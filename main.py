


import random

n = input("Enter a number of dice to throw: ")
i = 1
y=0
x=0.1
while (i<=n):
     y=random.randint(1,6)
     if i==1:
      print ("\nDie %d: %d" % (i, y))
      i = i + 1
      x = x + y
      y = 0
     else:
      print ("Die %d: %d" % (i, y))
      i=i+1
      x = x + y
      y=0
print ("\nAverage: %1.1f" % (x/n))


