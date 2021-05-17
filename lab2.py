class Ask(object):
    question = str
    ansver = str
    def __init__(self, question, ansver):
        self.question = question
        self.ansver = ansver
        pass


def get_ask(value:Ask):
    print(value.question)
    user_ansver = input()
    if user_ansver == value.ansver:
        print("Верно!")
        return 1
    else:
        print("Неправильно!")
        return 0
        

fio = "Косинов Денис Сергеевич"
print(fio)
print(fio[3::2])
print(fio.rindex(fio))

a1 = Ask("Должны ли абстрактные классы описывать реализацию методов?\n 1 - да\n 0 - нет", "0")
a2 = Ask("Поддерживают ли целые числа в python длинную арифметику?\n 1 - да\n 0 - нет", "1")
a3 = Ask("Строка в python задаётся с помощью фигурных скобок\n 1 - да\n 0 - нет", "0")
a4 = Ask("Можно ли указывать отрицательные индексы в срезах?\n 1 - да\n 0 - нет", "1")
a5 = Ask("Существует ли у строк в python метод push_back?\n 1 - да\n 0 - нет", "0")
point = 0
point += get_ask(a1)
point += get_ask(a2)
point += get_ask(a3)
point += get_ask(a4)
point += get_ask(a5)

print(fio + ", ваша оценка: " + str(point))

