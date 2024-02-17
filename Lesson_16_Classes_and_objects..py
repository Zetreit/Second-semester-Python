#Задание №1:

class CashRegister:
    def __init__(self):
        self.balance = 0
    
    def top_up(self, amount):
        self.balance += amount
    
    def count_1000(self):
        return self.balance // 1000
    
    def take_away(self, amount):
        if amount > self.balance:
            raise ValueError("Недостаточно денег в кассе")
        self.balance -= amount

# Создаем экземпляр класса CashRegister
cash_register = CashRegister()

while True:
    print("Выберите действие:")
    print("1. Пополнить кассу")
    print("2. Забрать из кассы")
    print("3. Отобразить баланс в целых тысячах")
    print("4. Выйти")
    
    choice = input("Введите номер действия: ")
    
    if choice == '1':
        try:
            amount = int(input("Введите сумму для пополнения кассы: "))
            cash_register.top_up(amount)
            print("Касса пополнена.")
        except ValueError:
            print("Ошибка! Введите целое число.")
    elif choice == '2':
        try:
            amount = int(input("Введите сумму для изъятия из кассы: "))
            cash_register.take_away(amount)
            print("Сумма успешно изъята из кассы.")
        except ValueError as e:
            print(e)
    elif choice == '3':
        print("Баланс в целых тысячах:", cash_register.count_1000())
    elif choice == '4':
        print("Программа завершена.")
        break
    else:
        print("Неверный ввод. Попробуйте снова.")


#Задание №2:

class Turtle:
    def __init__(self, x=0, y=0, s=1):
        self.x = x
        self.y = y
        self.s = s
    
    def go_up(self):
        self.y += self.s
    
    def go_down(self):
        self.y -= self.s
    
    def go_left(self):
        self.x -= self.s
    
    def go_right(self):
        self.x += self.s
    
    def evolve(self):
        self.s += 1
    
    def degrade(self):
        if self.s <= 1:
            raise ValueError("Невозможно уменьшить s дальше")
        else:
            self.s -= 1
    
    def count_moves(self, x2, y2):
        x_moves = abs(x2 - self.x) // self.s
        y_moves = abs(y2 - self.y) // self.s
        return x_moves + y_moves

# Создаем экземпляр класса Turtle
turtle = Turtle()

while True:
    print("Выберите действие:")
    print("1. Переместить черепашку вверх")
    print("2. Переместить черепашку вниз")
    print("3. Переместить черепашку влево")
    print("4. Переместить черепашку вправо")
    print("5. Увеличить количество клеточек на шаг перемещения")
    print("6. Уменьшить количество клеточек на шаг перемещения")
    print("7. Посчитать минимальное количество действий до позиции (x2, y2)")
    print("8. Выйти")
    
    choice = input("Введите номер действия: ")
    
    if choice == '1':
        turtle.go_up()
        print("Черепашка перемещена вверх.")
    elif choice == '2':
        turtle.go_down()
        print("Черепашка перемещена вниз.")
    elif choice == '3':
        turtle.go_left()
        print("Черепашка перемещена влево.")
    elif choice == '4':
        turtle.go_right()
        print("Черепашка перемещена вправо.")
    elif choice == '5':
        turtle.evolve()
        print("Количество клеточек на шаг перемещения увеличено.")
    elif choice == '6':
        try:
            turtle.degrade()
            print("Количество клеточек на шаг перемещения уменьшено.")
        except ValueError as e:
            print(e)
    elif choice == '7':
        try:
            x2 = int(input("Введите координату x2: "))
            y2 = int(input("Введите координату y2: "))
            print("Минимальное количество действий до позиции ({}, {}) равно:".format(x2, y2), turtle.count_moves(x2, y2))
        except ValueError:
            print("Ошибка! Введите целые числа.")
    elif choice == '8':
        print("Программа завершена.")
        break
    else:
        print("Неверный ввод. Попробуйте снова.")
