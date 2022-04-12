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

class child_Cartoon_character(Cartoon_character):
    def __init__(self, name, cartoon_name, age, rank, animal_type):
        super().__init__(name, cartoon_name, age, rank)
        self.animal_type = animal_type

    def print_info(self):
        print("Персонаж " + self.name + " из " + self.cartoon_name + ". Его возраст - " + str(self.age) + ". Вид - " + str(self.animal_type) + "\n")

    def special_speak(self):
        print(self.name + " говорит: оньк-оньк-оньк\n")

class second_class(object):
    def second_class_metod(self):
        print("Вызвался метод из second_class\n")

class third_class(child_Cartoon_character, second_class):
    def third_class_metod(self):
        print("Вызвался метод из third_class\n")

class foot_to_meter(float):
    def __new__(foot):
        return foot * 0.3048

class subsequence_lab(object):
    def __init__(self, self_string:str):
        self.__self_string = self_string

    @property
    def __getitem__(self):
        return self.__self_string

    @property
    def first(self):
        if(self.__self_string.__len__() > 0):
            return self.__self_string[0]

    @property
    def last(self):
        if(self.__self_string.__len__() > 0):
            return self.__self_string[self.__self_string.__len__() - 1]
    
    @property
    def __str__(self):
        return self.__getitem__

    @property
    def pop(self, index = 1):
        if(index < self.__self_string.__len__()):
            tmp_string = ""
            while index < self.__self_string.__len__():
                tmp_string += self.__self_string[index]
                index+=1
            self.__self_string = tmp_string        
        else:
            print("недопустимый индекс")
    
          
 

pers1 = child_Cartoon_character("Porko", "Porko Rosso", 45, 5, "pig")
pers1.print_info()

tmp = foot_to_meter
meter_counter = tmp.__new__(100)
print(meter_counter)

dkosinov = subsequence_lab("some_string")
print(dkosinov.__getitem__)
print(dkosinov.first)
print(dkosinov.last)
print(dkosinov.__str__)
dkosinov.pop
print(dkosinov.__getitem__)