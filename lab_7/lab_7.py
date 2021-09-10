#Косинов 10 вариант
#Лабораторная №7

import math
import random

my_file = open("test.txt", 'w')

my_file.write("test string")

my_file.close()

my_file = open("test.txt", 'r')

message = my_file.read()

print(message, '\t', type(message))

# #1
# a_set = {i for i in "abcdefg"}
# print(a_set)
# #2
# it_ob = []
# for i in a_set:
#     if type(i) == int or type(i) == float or type(i) == complex or type(i) == bool or type(i) == str or type(i) == tuple or type(i) == frozenset or type(i) == bytes:
#         it_ob.append(i)
#     else:
#         it_ob.append(int(random.random * 100))
# print(it_ob)
# #3
# b_set = set()
# for i in it_ob:
#     b_set.add(i)
# print(b_set, "\n")

# set_test1 = a_set.intersection(b_set)
# set_test2 = a_set.difference(b_set)

# print(set_test1)
# print(set_test2)

# #4
# a_dict = {i: i**2 + 1 for i in range(5)}
# items = a_dict.items()
# a_dict.pop(1)
# a_dict.clear()
# print(a_dict)

