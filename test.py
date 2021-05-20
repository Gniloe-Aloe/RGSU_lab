import random
words = (('гипербола', 'эллипс', 'парабола', 'ассимптота', 'производная'), ('ложка', 'вилка', 'тарелка', 'посуда', 'кружка'), ('кот', 'стол', 'стул', 'лук', 'луг'))

i = 0

t = True

while (t):
    word = random.choice(words[i])
    correct = word
    ana = ''

    while word:
        pos = random.randrange(len(word))
        ana += word[pos]
        word = word[:pos]+word[pos + 1:]

print(str(ana))

ans = "неверный ответ"

t1 = True

while t1:
    ans = input("Введите ваш ответ: ")

    if ans == '':
        t1 = False
        t = False
        break

if ans == correct:
    print("Верно!")

    t = False
    t1 = False

else:

    print("Неправильно!")
    if (i < 2):

        ans = input("Хотите более лёгкую анаграмму?" + "\n" +"1 -да"+ "\n" +"0 -нет")

        if (ans == "1"):

            i = i + 1
            t1 = False