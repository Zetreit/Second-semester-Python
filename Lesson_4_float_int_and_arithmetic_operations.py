#Задание №1:

# Запрос ввода сторон прямоугольника
side1 = float(input("Введите длину первой стороны прямоугольника: "))
side2 = float(input("Введите длину второй стороны прямоугольника: "))

# Вычисление площади и периметра
area = side1 * side2
perimeter = 2 * (side1 + side2)

# Вывод результатов
print("Площадь прямоугольника:", area)
print("Периметр прямоугольника:", perimeter)

#Задание №2:

# Ввод пятизначного целого числа
number = int(input("Введите пятизначное целое число: "))

# Разбиваем число на отдельные цифры
units = number % 10
tens = (number % 100) // 10
hundreds = (number % 1000) // 100
thousands = (number % 10000) // 1000
ten_thousands = number // 10000

# Вычисляем результат
result = (tens ** units) * (hundreds * 100) / (ten_thousands - thousands)

# Выводим результат
print("Результат:", result)
