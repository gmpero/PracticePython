#Найдите первую и последнюю буквы А в данной символьной строке. Сформируйте новую строку, в которой сначала идет группа символов, стоящая после последней буквы А, затем группа символов, стоящая перед первой буквой А, и, наконец, все остальные символы.
string = "fdfdgassssssssssssssssaeeeeeeeeeerrrrrrrrrrrrraxxxxxx!"
print("Индекс первой буквы 'a':", string.find("a"))
print("Поиск 'a' методом rfind:", string.rfind("a"))

print(string[string.rfind("a") + 1:] + string[:string.find("a")] + string[string.find("a") + 1:string.rfind("a")])

