#lab-4
#Вариант 10
import cgi, cgitb, re, sys, os
from os import environ as env
cgitb.enable()

sys.stdout.reconfigure(encoding='utf-8')

form = cgi.FieldStorage()
first_field = form.getfirst("first_field", "")
second_field = form.getfirst("second_field", "")
third_field = form.getfirst("third_field", "")
p = re.compile("(Ст. )(\d курса)( факультет )(\D+)")
m = re.match(p, first_field)

if (m):
	print("Your course and faculty: " + m.group(2) + " " + m.group(4) + "<br><br>")
else:
	print("Data1 is incorrect" + "<br><br>")
	
p = re.compile("(Фамилия Инициалы )([А-Яа-я]+)(\s)([А-Яа-я]+)")
m = re.search(p, second_field)
if (m):
	print("Surname, initials" + m.group(2) + " " + m.group(4) + "<br><br>")
else:
	print("second_field is incorrect" + "<br><br>")

p = re.compile("(ЗК: )(\d+)")
m = p.match(third_field)
if (m):
	print("Your ZK number: " + m.group(2) + "<br><br>")
else:
	print("third_field is incorrect" + "<br><br>")
	
literal = form.getfirst("literal", "")
p = re.compile("(\{\(\d,\s*\d,\s*\d,\s*\d\s*\),\s*\"[\s\S]+\"\})")
m = p.search(literal)
if (m):
	print("Your literal is: " + m.group(1) + "<br><br>")
else:
	print("Literal is incorrect" + "<br><br>")