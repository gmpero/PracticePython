l = ["f", 1, 2, 3, "s", 1.2]

dictionary = {}
string = None

for el in l:
    if type(el) == str:
        dictionary[el] = []
        string = el
    else:
        dictionary[string].append(el)

print(dictionary)