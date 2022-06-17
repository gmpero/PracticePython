#1 Задача создать двумерный массив n на m строк и заполнить его нулями


def write_2d(n, m):
    mas = []

    for i in range(n):
        empti = []

        for j in range(m):
            empti.append(0)

        mas.append(empti)

    return mas


def print_matrix(mas):
    for i in range(len(mas)):
        for j in range(len(mas[i])):
            print(mas[i][j], end=' ')
        print()


matrix = write_2d(5, 10)
'''
print_matrix(matrix)
'''

#2 Задача отобразить двухмерный массив зеркально данному

mas = [[1, 2, 3, 4],
       [4, 5, 6],
       [7, 8, 9]]


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    # arr[i], arr[j] = arr[j], arr[i]


def reverse_mas(mas):
    for st in mas:
        for i in range(len(st) // 2):
            swap(st, i, len(st) - 1 - i)


reverse_mas(mas)
print_matrix(mas)
