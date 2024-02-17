#Задание №1:

# Ввод числа N
N = int(input("Введите количество чисел: "))

# Счетчик нулей
zero_count = 0

# Ввод и подсчет нулей
for _ in range(N):
    num = int(input("Введите число: "))
    if num == 0:
        zero_count += 1

# Вывод результата
print("Количество нулей:", zero_count)

#Задание №2:

# Ввод числа X
X = int(input("Введите натуральное число: "))

# Счетчик делителей
divisors_count = 0

# Подсчет делителей
for i in range(1, X + 1):
    if X % i == 0:
        divisors_count += 1

# Вывод результата
print("Количество делителей числа", X, ":", divisors_count)

#Задание №3:

# Ввод чисел A и B
A = int(input("Введите целое число A: "))
B = int(input("Введите целое число B: "))

# Вывод четных чисел на отрезке [A, B]
for num in range(A, B + 1):
    if num % 2 == 0:
        print(num, end=" ")
