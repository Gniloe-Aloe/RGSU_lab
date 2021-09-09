#Косинов 10 вариант
#Лабораторная №5

import math
import random

def func1(array):
    tmp_array = []
    for i in array:
        tmp_array.append(math.sqrt(i))

    return tmp_array


def func2(my_dict: dict, value: str):
    list_of_key = []
    for key in my_dict:
        if my_dict[key] == value:
            list_of_key.append(key)

    return list_of_key


def func3(my_list):
    tmp_list = []
    for i in my_list:
        tmp_list.append(int(i))
    
    return tmp_list


my_array = [25, 144, 156.25]
print(func1(my_array))

a_dict = {0: "к", 1 : "m", 2: "l", 3 : "r", 4: "s", 5 : "o", 6 : "o", 7 : "o"}
print(func2(a_dict, "o"))

a_list = [True, False, 10, 12]
print(func3(a_list))

new_list = func3(a_list)
new_list.sort()
print(new_list)





# kortesh = tuple("hello world")
# kortesh2 = tuple("Test")

# mass = []
# for i in range(10):
#     mass.append(i)
 
# def my_sum(a: int, b: int):
#     return a + b

# value = int(random.random() * 100)
# print("value == ", value)
# print("sqr of value == ", math.sqrt(value))

# for i in "Hello world!":
#     if i == "o":
#         continue
#     print(i * 2, end="")
# print()

# for i in "hello world":
#     if i == "l":
#         break
#     else:
#         print("Нашли букву!")
# else:
#     print("Буквы в сторке нет")

