#Задание №1:
# Ввод числа
number = int(input("Введите целое число: "))

# Проверка на четность и знак числа
if number == 0:
    print("Нулевое число")
elif number % 2 == 0:
    if number > 0:
        print("Положительное четное число")
    else:
        print("Отрицательное четное число")
else:
    if number > 0:
        print("Положительное нечетное число")
    else:
        print("Отрицательное нечетное число")


#Задание №2:

# Ввод слова
word = input("Введите слово из маленьких латинских букв: ")

# Счетчики гласных и согласных букв
vowels = 0
consonants = 0

# Проверка каждой буквы в слове
for char in word:
    if char in ['a', 'e', 'i', 'o', 'u']:
        vowels += 1
    elif char.isalpha():
        consonants += 1

# Вывод результатов
print("Количество гласных букв:", vowels)
print("Количество согласных букв:", consonants)

#Задание №3:

# Ввод данных
X = int(input("Минимальная сумма инвестиций: "))
A = int(input("Майкл вложил: "))
B = int(input("Иван вложил: "))

# Проверка условий
if A >= X and B >= X:
    print(2)
elif A >= X:
    print("Mike")
elif B >= X:
    print("Ivan")
elif A + B >= X:
    print(1)
else:
    print(0)
