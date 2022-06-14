#1
''' Дан список из строк.
а) Поменять местами самую длинную и самую короткую строки в списке
б) Отсортировать список, чтобы строки шли по алфавиту '''

strings = ["red", "eggs", "table", "b", "a", "ab", "ford", "ofcourse"]
short_word = strings.index(min(strings, key=len))
long_word = strings.index(max(strings, key=len))

strings[short_word], strings[long_word] = strings[long_word], strings[short_word]
print("a: ", strings)


def bubble_sort(string):
    for i in range(0, len(string)-1):
        for j in range(len(string)-1):
            if(string[j] > string[j+1]):
                temp = string[j]
                string[j] = string[j+1]
                string[j+1] = temp
    return string


print("b: ", bubble_sort(strings))

#2
''' Найдите первую и последнюю буквы А в данной символьной строке. 
Сформируйте новую строку, в которой сначала идет группа символов, 
стоящая после последней буквы А, затем группа символов, стоящая перед первой буквой А, и, наконец, все остальные символы. '''

string = "fdfdgassssssssssssssssaeeeeeeeeeerrrrrrrrrrrrraxxxxxx!"
print("Индекс первой буквы 'a':", string.find("a"))
print("Поиск 'a' методом rfind:", string.rfind("a"))

print(string[string.rfind("a") + 1:] + string[:string.find("a")] + string[string.find("a") + 1:string.rfind("a")])

#3
''' Дано предложение. Первое слово предложения, имеющее данную длину k, замените последним словом этого предложения. '''

string = "We don’t need no education, we don’t need no thought control."

k = int(input("Enter K: "))#2
result = string.split()

for i, value in enumerate(result):
    if len(value) == k:
        result[i], result[len(result)-1] = result[len(result)-1], result[i]
        break

print(result)

#5
''' Распечатайте заданный текст треугольниками. '''

string = "cosinus"


for i in range(len(string)):
    print(string[0:len(string)-i])


for i in range(len(string)):
    print(" "*i, string[i:])


for i in range(len(string)+1):
    print(string[:i])


for i in range(len(string)+1):
    print(" "*(len(string)-i), string[len(string)-i:])
