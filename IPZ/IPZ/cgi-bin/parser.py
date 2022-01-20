print ( "Access-Control-Allow-Origin: *" )
print ()

import cgi, cgitb, random, pickle, sys
cgitb.enable()
sys.stdout.reconfigure(encoding='utf-8')

def raisePoint():
	f=open ("right.txt", 'r' )
	w = f.read()
	f.close()
	s = int(w)
	s += 1
	w = str(s)
	f=open ("right.txt", 'w' )
	f.write(w)
	f.close()

form = cgi.parse(keep_blank_values = "True")

questions = {1: ("Большинство утверждений истинные? (1 - да, 0 - нет)<br><br>1) Кортеж итерабелен<br>2) Кортеж изменяемый<br>3) Класс кортежа именуется Tupe", "1"), 
2: ("Большинство утверждений истинные? (1 - да, 0 - нет)<br><br>1) Список итерабелен<br>2) Список изменяем<br>3) Класс списка именуется List", "1"), 
3: ("Большинство утверждений истинные? (1 - да, 0 - нет)<br><br>1) (1, 2, 3) - это список<br>2) [1, 2, 3] - это кортеж<br>3) ([1, 2], [3, 4]) - это кортеж списков", "0"), 
4: ("Большинство утверждений истинные? (1 - да, 0 - нет)<br><br>1) (1, 2, 3) - это кортеж<br>2) {1, 2, 3} - это список<br>3) ([1, 2], [3, 4]) - это список кортежей", "0")}

name = form["name"][0]
answer = form["answer"][0]

if (name != ""):
	w = "0"
	f=open ("right.txt", 'w' )
	f.write(w)
	f.close()
	f=open ("cash.txt", 'w' )
	f.write(w)
	f.close()
	f=open ("name.txt", 'w' )
	f.write(name)
	f.close()
	f=open ("variant.txt", 'w' )
	f.write("0")
	f.close()
	answer = "1"
	f=open ("done.txt", 'w' )
	f.write("")
	f.close()

if (answer != ""):
	f=open ("cash.txt", 'r' )
	w = f.read()
	f.close()
	s = int(w)
	s += 1
	w = str(s)
	f=open ("cash.txt", 'w' )
	f.write(w)
	f.close()
	f=open ("variant.txt", 'r' )
	variant = int(f.read())
	f.close()
	
	
	
	if (variant != 0):
		if (questions[variant][1] == answer):
			raisePoint()
	
	if (s == 4):
		f=open ("name.txt", 'r' ) 
		name = f.read()
		f.close()
		f=open ("right.txt", 'r' ) 
		points = f.read()
		f.close()
		answers = {"name": name, "tests": 3, "points": points}
		print("Уважаемый " + answers["name"] + "<br><br>Вы выволнили " + str(answers["tests"]) + " теста<br><br>Вы набрали " + answers["points"] + " очка")
	else:
		t = True
		f=open ("done.txt", 'r' ) 
		done = f.read()
		f.close()
		while(t):
			variant = random.randint(1, 3)
			t = str(variant) in done
		done += str(variant)
		f=open ("done.txt", 'w' ) 
		f.write(done)
		f.close()
		f=open ("variant.txt", 'w' ) 
		f.write(str(variant))
		f.close()
		print(questions[variant][0])


