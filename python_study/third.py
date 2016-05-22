__author__ = 'fly'

import first1

li = range(1,5)
li1 = []
for val in li:
    li1.append(val)
li1.extend(li)
print(li1)
li1.remove(4)
print(li1)
li1.remove(4)
print(li1)

dict = {'A':65,'B':66,'C':67}
dict1 = dict
length = len(dict)
print("length is %d" %(length))
print(dict)

del dict['A']
print(dict)
print(dict1)

first1.hello()
first1.logo()