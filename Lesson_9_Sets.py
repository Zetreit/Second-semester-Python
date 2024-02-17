#Задание №1

# Ввод числа N
N = int(input())

# Создание пустого списка для чисел
numbers = []

# Ввод N чисел и добавление их в список
for _ in range(N):
    num = int(input())
    numbers.append(num)

# Переворачиваем список чисел и выводим его
reversed_numbers = numbers[::-1]
for num in reversed_numbers:
    print(num)

#Задание №2

# Ввод числа N
N = int(input())

# Ввод N чисел через пробел и разделение их на список
numbers = list(map(int, input().split()))

# Изменение порядка элементов в списке
reversed_numbers = numbers[::-1]

# Вывод измененного списка
for num in reversed_numbers:
    print(num, end=' ')

#Задание №3

# Ввод максимальной массы лодки и количества рыбаков
m = int(input())
n = int(input())

# Ввод веса каждого рыбака и сохранение в список
fishermen_weights = [int(input()) for _ in range(n)]

# Сортировка списка весов рыбаков по возрастанию
fishermen_weights.sort()

# Инициализация переменной для подсчета лодок
boats_count = 0

# Пока есть рыбаки в списке
while fishermen_weights:
    # Если в списке остался только один рыбак
    if len(fishermen_weights) == 1:
        # Увеличиваем количество лодок и выходим из цикла
        boats_count += 1
        break
    # Если сумма весов двух самых легких рыбаков не превышает максимальную массу лодки
    elif fishermen_weights[0] + fishermen_weights[-1] <= m:
        # Удаляем из списка двух рыбаков и увеличиваем количество лодок
        fishermen_weights.pop(0)
        fishermen_weights.pop()
        boats_count += 1
    else:
        # Если сумма весов двух самых легких рыбаков превышает максимальную массу лодки
        # Удаляем из списка только самого тяжелого рыбака и увеличиваем количество лодок
        fishermen_weights.pop()
        boats_count += 1

# Вывод количества лодок
print(boats_count)
