
print("Введите первый список:")
set_1 = set(input())
print("Введите второй список:")
set_2 = set(input())

print(*sorted((set_1 - set_2)))