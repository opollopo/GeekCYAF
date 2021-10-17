# import cong
#
# cong.t1()
# import p1.sun as s1
# s1.st1()
from cong import *
from p1.sun import *
from p1 import *

# t1()
# t2()
# st1()
# sun.st1()
a = set()
a.add(1)
a.add(3)
a.add(2)
a.remove(1)
print(a)
b = {3, 4, 5}
print(b)
c = a | b
print(a - b)
print(a ^ b)
t = [1, 2, 3, 4, 5, 68, 5, 2, 47, 1]
s = set(t)
print(list(s))
