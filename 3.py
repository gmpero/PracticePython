#1
'''
(Словари) В словарь заносятся пары синонимов, например hello - hi, bye - goodbye, list - arrray(можно дополнить своими). 
Написать программу, которая ищет значение(синоним), по его ключу
'''

words = {"hi": "hello", "bye": "goodbye", "list": "array"}
print(words[input()])

#2
'''
(Словари) Дан текст. Составить словарь, в котором подсчитывается сколько раз встречается каждое слово в тексте. 
Ключем будет само слово, а значением - количество повторений
'''

text = "Advertisers study how people learn so that they can 'teach' them to respond to their advertising. " \
       "They want us to be interested, to try something, and then to do it again. " \
       "These are the elements of learning: interest, experience and repetition. " \
       "If an advert can achieve this, it is successful. " \
       "If an advert works well, the same technique can be used to advertise different things. " \
       "So, for example, in winter if the weather is cold and you see a family having a warming cup of tea and feeling cosy, " \
       "you may be interested and note the name of the tea ... " \
       "Here the same technique is being used as with the cool, refreshing drink."

dictionary = {}

for el in text.split():
    if el in dictionary:
        dictionary[el] = dictionary[el] + 1
    else:
        dictionary[el] = 1

# for word in text.split():
#    dictionary[word] = dictionary.get(word, 0) + 1 // проверяем есть ли данный ключ в словаре, если нет то присваем туда 0 + 1 иначе + 1

print(dictionary)

#3a
'''
а) (Словари) Есть два списка одинаковой длины. 
В первом содержатся ключи, а во втором значения. Напишите функцию CreateDict(), которая создаёт из этих ключей и значений словарь.
'''

key = "hello", "array", "goodbye"
value = "hi", "arr", "bye"


def CreateDict(list_1, list_2):
    dictionary = {}
    for k, v_key in enumerate(key):
        for v, v_value in enumerate(value):
            if k == v:
                dictionary[v_key] = [v_value]
    return dictionary


print(CreateDict(key, value))

#3b
'''
б) Есть два списка разной длины. В первом содержатся ключи, а во втором значения. Напишите функцию, которая создаёт из этих ключей и значений словарь. 
Если ключу не хватило значения, в словаре должно быть значение None. Значения, которым не хватило ключей, нужно игнорировать.
'''

key = "hello", "array", "goodbye", "one"
value = "hi", "arr", "bye"


def CreateDict(key, value):
    dictionary = {}
    for k, v_key in enumerate(key):
        for v, v_value in enumerate(value):
            if k == v:
                dictionary[v_key] = [v_value]
            if k > v:
                dictionary[v_key] = None
    return dictionary


print(CreateDict(key, value))

#4
'''
(Множества) Даны два списка чисел. Найдите все числа, которые входят как в первый, так и во второй список и выведите их в порядке возрастания.
'''

num_1 = {1, 6, 9, 1, 2, 3, 4, 5, 6}
num_2 = {9, 8, 7, 6, 5, 4, 3}

my_set = set(num_1)
list_result = []
for el in my_set:
    if el in num_2:
        list_result.append(el)

print(list_result)

#5
'''
(Множества) Дано множество Colors, сдержащее набор цветов. 
Напишите функцию in_rainbow(), проверяющую, все ли цвета из этого набора входят в палитру цветов радуги
'''

colors = {"red", "blue", "ggg"}


def in_rainbow(colors):
    rainbow = {"Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"}
    if rainbow <= colors:
        return "Yes"
    return "No"


print(in_rainbow(colors))

#6
'''
(Множества) Дан текст: в первой строке записано число строк, далее идут сами строки. Определите, сколько различных слов содержится в этом тексте. 
Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов или символами конца строки.
'''

