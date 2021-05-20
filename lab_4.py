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



t = True
i = 0

while t:
    print('Сейчас вы увидите случайную анаграмму, вам нужно угадать слово.\n')
    input('Нажмите Enter, чтобы начать')
    slova = (('экзистенциализм', 'имплементация', 'электрокофемолка', 'дизоксерибонуклеиновый', 'детерминированность'),
             ('аксель', 'помидор', 'евгеника', 'программа', 'алгоритм'),
             ('дом', 'лом', 'ком', 'лук', 'холм'))
    slovo_1 = random.choice(slova[i])
    anagramma = ''
    slovo_2 = slovo_1
    while slovo_2:
        dlina = len(slovo_2)
        bukva_index = random.randint(0, (dlina - 1))
        bukva = slovo_2[bukva_index]
        anagramma += bukva
        if bukva_index != 0:
            slovo_nachalo = slovo_2[:bukva_index]
        else:
            slovo_nachalo = ''
        slovo_konec = slovo_2[(bukva_index + 1):]
        slovo_2 = slovo_nachalo + slovo_konec
    print(anagramma)

    otvet = input('Напишите слово и нажмите Enter, чтобы проверить вашу версию\n')
    if otvet != slovo_1:
        if i < 2:
            i += 1
        else: i = 2
    else: t = False
print('Верно!')

input('Нажмите Enter, чтобы выйти')


