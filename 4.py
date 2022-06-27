# Модуль 4. Основы ООП. Классы.

#1
'''
Создать класс Person, который содержит: 
переменные fullName, age;
методы move() и talk(), в которых просто вывести на консоль сообщение -"Такой-то  Person говорит". 
Добавьте два конструктора  - Person() и Person(fullName, age).
Создайте два объекта этого класса. Один объект инициализируется конструктором Person(), другой - Person(fullName, age).
'''

class Person:
    def __init__(self, fullname = 'noname', age = 18):
        self.fullName = fullname
        self.age = age

    def move(self):
        print("Такой-то", self.fullName, "говорит, мне", self.age, "лет")

    def talk(self):
        print("Такой-то", self.fullName, "говорит")


noname = Person()
noname.talk()

Max = Person('Max', 22)
Max.move()

#2
'''
Создать класс Student() который содержит переменные name(str), points(list). 
В списке points - три числа - оценки студента за три экзамена. 
Создать 10 экземпляров класса, занести их в список. 
Отсортировать студентов по имени и по среднему баллу. 
Вывести отсортированные списки студентов на печать. 
'''

class Student:
    def __init__(self, fname, lpoints):
        self.name = fname
        self.points = lpoints

    def print_info(self):
        print(self.name, self.points)


def bubble_sort_name(string):
    for i in range(0, len(string)-1):
        for j in range(len(string)-1):
            if(string[j].name > string[j+1].name):
                temp = string[j]
                string[j] = string[j+1]
                string[j+1] = temp
    return string


def bubble_sort_point(list_st):
    for i in range(0, len(list_st)-1):
        for j in range(len(list_st)-1):
            if(list_st[j].points > list_st[j+1].points):
                temp = list_st[j]
                list_st[j] = list_st[j+1]
                list_st[j+1] = temp
    return list_st


list_students = [Student("Валера", [5, 5, 4]),
                 Student("Каркуша", [5, 4, 4]),
                 Student("Нюша", [1, 5, 2]),
                 Student("Лосяш", [1, 2, 1]),
                 Student("Крош", [3, 5, 1]),
                 Student("Бараш", [4, 5, 1]),
                 Student("Потат", [3, 2, 1]),
                 Student("Пин", [3, 4, 4]),
                 Student("Совунья", [2, 1, 2]),
                 Student("Потапыч", [4, 1, 1])]

print("Студенты:")
for i in range(len(list_students)):
    list_students[i].print_info()

bubble_sort_name(list_students)

print("Студенты отсортированные по имени:")
for i in range(len(list_students)):
    list_students[i].print_info()

bubble_sort_point(list_students)

print("Студенты отсортированные по баллу:")
for i in range(len(list_students)):
    list_students[i].print_info()
