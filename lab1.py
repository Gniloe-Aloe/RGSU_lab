help("|")
first = int(input())
second = int(input())
tmp = first// second
if (type(tmp) == float):
    tmp = int(tmp)
print(bin(tmp))
print(first)
print(tmp)
print(first<<tmp)