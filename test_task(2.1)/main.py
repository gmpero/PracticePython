# Дан список из строк.
# а) Поменять местами самую длинную и самую короткую строки в списке
# б) Отсортировать список, чтобы строки шли по алфавиту

strings = ["red", "eggs", "table", "b", "a", "ab", "ford", "ofcorse"]


def bubble_sort(string):
    for i in range(0, len(string)-1):
        for j in range(len(string)-1):
            if(string[j] > string[j+1]):
                temp = string[j]
                string[j] = string[j+1]
                string[j+1] = temp
    return string


print(min(strings, key=len))
print("The sorted list is: ", bubble_sort(strings))

