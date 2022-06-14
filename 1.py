#1
'''
(переменные и операторы) Дано число n<1440. С начала суток прошло n минут. 
Определите, сколько часов и минут будут показывать электронные часы в этот момент. 
Программа должна вывести два числа: количество часов (от 0 до 23) и количество минут (от 0 до 59). 
'''

n = int(input("Введите количество минут с начала суток: "))
if n>=1440 or n<0:
    print("Error")
else:
    quantity_of_hours = int(n/60)
    quantity_of_minutes = n%60
    print("с начала суток прошло " + str(quantity_of_hours)+" часа(ов) и " + str(quantity_of_minutes)+" минут")
#print("с начала суток прошло " + str(int(n/60)) + " часа(ов) и " + str(int(n%60)) + " минут")

#2
'''
(условия) Дано текущее время (часы, минуты, секунды). Определить, сколько время будет через 10 секунд
'''

timeH, timeM, timeS = map(int, input("Введите время (часы, минуты и секунды через пробел): ").split())

if timeH >= 24 or timeM >= 60 or timeS >=60:
    print("EROR")
else:
    timeAllS = timeH*3600+timeM*60+timeS

    timeAllS += 10

    timeH = int(timeAllS / 3600)
    timeM = int(timeAllS % 3600 / 60)
    timeS = int(timeAllS % 3600 % 60)

    if timeH >= 24:
        timeH = 0

    print("h:" +str(timeH) + "\t" + "m:" + str(timeM) + "\t" + "s:" + str(timeS))
    
#3
'''
(циклы) Даны два целых числа A и В. 
Выведите все числа от A до B включительно, в порядке возрастания, если A < B, или в порядке убывания в противном случае.
'''
    
a = int(input("a: "))
b = int(input("b: "))

#if b < a:
    #a, b = b, a
print("result:")
while a <= b:
    print(a)
    a += 1
while a >= b:
    print(a)
    a -= 1

#4
'''
(списки, алгоритмы списков) Дан список из 10 элементов. 
Найти максимальный и минимальный элемент. 
Поменять местами максимальный и минимальный элемент. Не использовать функции max и min
'''

list = [1, 2, 3, 4, 5, 6, 7, 8, 10]
a = 0
b = 0
minX = list[0]
maxX = list[0]
for x in list:
    if x > maxX:
        maxX=x
        a = list.index(x)
for x in list:
    if x < minX:
        minX=x
        b = list.index(x)


list[a], list[b] = list[b], list[a]
print("меняем местами элементы max и min ")
for x in list:
    print(x)
print("max: " + str(maxX))
print("min: " + str(minX))

#5
'''
(списки, методы списков) Даны два списка с числами. 
Создать третий список, в котором будут элементы, которые есть и в первом и во втором списке
'''

firstList = [1,2,4,2,5,7,1,9,100]
secondList = [1,2,3,2,5,7,9,1,4,100]
res_list = []
#result=list(set(firstList) & set(secondList))
#print(result)

for i, value in enumerate(firstList):
    for j, value in enumerate(secondList):
        if firstList[i] == secondList[j]:
            res_list.append(firstList[i])
            secondList[j] = "false"

print(res_list)

#6
'''
(функции) Даны две стороны прямоугольника. 
Написать три функции, которые возвращают, площадь, периметр и диагональ этого прямоугольника
'''

import math

a = int(input("Введите число: "))
b = int(input("Введите число: "))


def area(a,b):
    return a*b
  
  
def perimeter(a,b):
    return 2*(a+b)
  

def diagonal(a,b):
    return math.sqrt(a**2+b**2)
  

#c = area(a,b)
#d = perimeter(a,b)
#e = diagonal(a,b)

print ("Площадь: " + str(area(a,b)))
print ("Периметр: " + str(perimeter(a,b)))
print ("Диагональ: " + str(diagonal(a,b)))

#7
'''
(двумерные списки) В двумерном списке 4х4 найти элемент, значение которого наиболее приближено к среднему арифметическому всех элементов массива
'''

mas = [[1, 3, 1, 3], 
       [3, 4, 6, 5],
       [0, 1, 2.5, 0],
       [0, 1, 4, 2]]
s = 0

for row in mas:
    s+=sum(row)
size = (len(mas)*len(mas[0]))
sr = s / size
srn = abs(sr - mas[0][0])

for i in mas:
    for value in i:
        if srn > abs(sr-value):
            srn = abs(sr-value)
            output = value

print("answer:" + str(output))
