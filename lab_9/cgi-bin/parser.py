#lab-4
#Вариант 10
import cgi, cgitb, re, sys, os, random
from os import environ as env
cgitb.enable()
sys.stdout.reconfigure(encoding='')
def funcSort(a):
	return abs(a)
form = cgi.FieldStorage()
a_list = []
for i in range(0, 12):
	a_list.append(random.randint(-4, 3))	
print("Hello, ", form.getfirst("name", "") )
print("<br><br>")
print(a_list)
print("<br><br>")
if (form.getfirst("func1", "") == "on"):
	tmp = 1
	flag = 1
	for i in a_list:
		if(flag):
			tmp *= i
			flag = 0
		if(not flag):
			flag = 1
	print("Произведение нечётных чисел " + str(tmp) + "<br><br>")
if (form.getfirst("func2", "") == "on"):
	tmp = abs(a_list[0])
	for i in a_list:
		if (tmp >= abs(i)):
			tmp = abs(i)
	print("Минимальное среди чисел, взятых по абсолютной величине: " + str(tmp) + "<br><br>")
if (form.getfirst("func3", "") == "on"):
	a_list.sort(key = funcSort)
	print("Массив, отсортированный по абсолютной величине: ")
	print(a_list)


	