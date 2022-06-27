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

