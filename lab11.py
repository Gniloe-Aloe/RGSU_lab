#Вариант10
class Cartoon_character(object):
    class_atribute = "Dkosinov"

    def __init__(self, name, cartoon_name, age, rank):
        self.name = name
        self.cartoon_name = cartoon_name
        self.age = age
        self.__rank = rank
        self.__close_tmp = "dkosinov"
        self.__private_method()

    def __str__(self):
        return "Персонаж " + self.name + " из " + self.cartoon_name + ". Его возраст - " + str(self.age) + "\n"

    def __del__(self):
        print("Персонаж удалён\n")

    def print_info(self):
        print("Персонаж " + self.name + " из " + self.cartoon_name + ". Его возраст - " + str(self.age) + "\n")

    @property
    def rank(self):
        return self.__rank

    @rank.setter
    def rank(self, rank):
        if(rank >= 0 and rank <= 5):
            self.__rank = rank
        else:
            print("Ошибочный ввод rank >= 0 and rank <= 5\n")

    def __private_method(self):
        print("Объект создан")

    @property
    def close_tmp(self):
        return self.__close_tmp
    
 

pers1 = Cartoon_character("Porko", "Porko Rosso", 45, 5)
print(pers1.rank)
pers1.rank = 4
print(pers1.rank)
print(pers1.close_tmp)
pers1.print_info()
print(pers1)
pers1.rank = 6
print(pers1.rank)
pers2 = Cartoon_character("Ziro", "The wind has risen", 25, 2)
print(pers2)
