import cgi, cgitb, random, pickle, sys
cgitb.enable()
sys.stdout.reconfigure(encoding='UTF-8')
form = cgi.parse(keep_blank_values = "True")

questions = {1: ("Может ли множество содержать повторяющиеся эллементы?\n\n1) да\n2) нет\n3) иногда", "2"), 
2: ("Как определяется неизменяемое множество?\n\n1) frozenset\n2) constset\n3) ewerset", "1"), 
3: ("Что делает этот метод set.union?\n\n1) Вычитает множество, переданное в качестве аргумента\n2) Объединяет несколько множеств\n3) Проверяет множество на равенство, возвращая bool", "2"), 
4: ("Какой оператор эквивалентен вызову этого метода set.issubset(other)?\n\n1) ==\n2) <=\n3) >=", "2"),
4: ("Какой оператор эквивалентен вызову этого метода set.issuperset(other)?\n\n1) ==\n2) <=\n3) >=", "3"),
}

name = form["name"][0]
answer = form["answer"][0]

if (name == ""):
	raise SystemExit
	print("Не введено имя!")

w = "0"
r_file=open ("faithful.txt", 'w' )
r_file.write(w)
r_file.close()
r_file=open ("cash.txt", 'w' )
r_file.write(w)
r_file.close()
r_file=open ("name.txt", 'w' )
r_file.write(name)
r_file.close()
r_file=open ("variant.txt", 'w' )
r_file.write("0")
r_file.close()
answer = "-1"
r_file=open ("end.txt", 'w' )
r_file.write("")
r_file.close()
r_file=open ("answers.txt", 'w' )
r_file.write("")
r_file.close()
r_file=open ("cash.txt", 'r' )
w = r_file.read()
r_file.close()

if ((answer != "") and (w != "5")):
	s = int(w)
	s += 1
	w = str(s)
	r_file=open ("cash.txt", 'w' )
	r_file.write(w)
	r_file.close()
	r_file=open ("variant.txt", 'r' )
	variant = int(f.read())
	r_file.close()
	if (answer != "-1"):
		r_file=open ("answers.txt", 'r' )
		ans = r_file.read()
		r_file.close()
		ans = ans + answer + "\n"
		r_file=open ("answers.txt", 'w' )
		r_file.write(ans)
		r_file.close()
	
	if (variant != 0):
		if (questions[variant][1] == answer):
			r_file = open ("faithful.txt", 'r' )
			w = r_file.read()
			r_file.close()
			s = int(w)
			s += 1
			w = str(s)
			r_filef = open ("faithful.txt", 'w' )
			r_file.write(w)
			r_file.close()
	
	if (s == 5):
		r_file=open ("name.txt", 'r' ) 
		name = r_file.read()
		r_file.close()
		r_file=open ("faithful.txt", 'r' ) 
		points = r_file.read()
		r_file.close()
		r_file=open ("answers.txt", 'r' )
		ans = r_file.read()
		r_file.close()
		answers = {"name": name, "tests": 3, "points": points}
		print(answers["name"] + ",\n\n ответили\n" + ans + "\n\nнабрали " + answers["points"] + " балла")
	else:
		t = True
		r_file=open ("end.txt", 'r' ) 
		end = r_file.read()
		r_file.close()
		while(t):
			variant = random.randint(1, 3)
			t = str(variant) in end
		end += str(variant)
		r_file=open ("end.txt", 'w' ) 
		r_file.write(end)
		r_file.close()
		r_file=open ("variant.txt", 'w' ) 
		r_file.write(str(variant))
		r_file.close()
		print(questions[variant][0])


