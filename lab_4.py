import random


a = float(10.2)
b = True
c = [a, b]
d = (a, b)
a_tuple = a, b, c, d

for pa in a_tuple:
    print(str(pa))

a_list = list(a_tuple)
a_list[0] = 14.8
a_tuple = tuple(a_list)

for pa in a_tuple:
    print(str(pa))

a_range = range(11)
b_tuple = tuple(a_range)
for pb in b_tuple:
    print(str(pb))



