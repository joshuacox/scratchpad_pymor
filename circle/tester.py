#!/usr/bin/env python

from circle import Circle

c = Circle(4)
c.printAll()
d = Circle(3)
d.printAll()
e = Circle(2)
e.printAll()

print (str(e))
print (Circle(2))

if str(e) == str(Circle(2)):
    print('equal')
else:
    print('not equal')

if str(e) == Circle(2):
    print('equal')
else:
    print('not equal')
