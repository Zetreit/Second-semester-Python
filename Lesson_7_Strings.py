#Задание №1:

# Ввод строки
s = input("Введите строку без пробелов: ")

# Проверка на палиндром
if s == s[::-1]:
    print("yes")
else:
    print("no")

#Задание №2:

# Ввод строки
s = input("Введите строку: ")

# Преобразование идущих подряд пробелов в один
s = ' '.join(s.split())

# Вывод измененной строки
print(s)

