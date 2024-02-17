#Задание №1:

import math

def factorial(n):
    return math.factorial(n)

def factorial_list(n):
    return [factorial(i) for i in range(factorial(n), 0, -1)]

number = int(input("Введите натуральное число: "))
print(factorial(number))
print(factorial_list(number))

#Задание №2:

import collections

# Создание словаря pets
pets = {
    1: {
        "Мухтар": {
            "Вид питомца": "Собака",
            "Возраст питомца": 9,
            "Имя владельца": "Павел"
        }
    },
    2: {
        "Каа": {
            "Вид питомца": "желторотый питон",
            "Возраст питомца": 19,
            "Имя владельца": "Саша"
        }
    }
}

def create():
    last = collections.deque(pets, maxlen=1)[0]
    new_id = last + 1
    pet_name = input("Введите имя питомца: ")
    pet_type = input("Введите вид питомца: ")
    pet_age = int(input("Введите возраст питомца: "))
    owner_name = input("Введите имя владельца: ")
    pets[new_id] = {
        pet_name: {
            "Вид питомца": pet_type,
            "Возраст питомца": pet_age,
            "Имя владельца": owner_name
        }
    }

def read(ID):
    if ID in pets:
        pet_info = pets[ID]
        for name, attributes in pet_info.items():
            age_suffix = "год" if attributes["Возраст питомца"] == 1 else "года" if 1 < attributes["Возраст питомца"] < 5 else "лет"
            print(f'Это {attributes["Вид питомца"]} по кличке "{name}". Возраст питомца: {attributes["Возраст питомца"]} {age_suffix}. Имя владельца: {attributes["Имя владельца"]}')
    else:
        print("Питомец с указанным ID не найден.")

def update(ID):
    if ID in pets:
        pet_info = pets[ID]
        for name, attributes in pet_info.items():
            pet_type = input("Введите новый вид питомца: ")
            pet_age = int(input("Введите новый возраст питомца: "))
            owner_name = input("Введите новое имя владельца: ")
            attributes["Вид питомца"] = pet_type
            attributes["Возраст питомца"] = pet_age
            attributes["Имя владельца"] = owner_name
        print("Информация о питомце обновлена.")
    else:
        print("Питомец с указанным ID не найден.")

def delete(ID):
    if ID in pets:
        del pets[ID]
        print("Информация о питомце удалена.")
    else:
        print("Питомец с указанным ID не найден.")

def pets_list():
    for ID, pet_info in pets.items():
        for name, attributes in pet_info.items():
            age_suffix = "год" if attributes["Возраст питомца"] == 1 else "года" if 1 < attributes["Возраст питомца"] < 5 else "лет"
            print(f'ID: {ID}. Это {attributes["Вид питомца"]} по кличке "{name}". Возраст питомца: {attributes["Возраст питомца"]} {age_suffix}. Имя владельца: {attributes["Имя владельца"]}')

command = ""
while command != "stop":
    command = input("Введите команду (create/read/update/delete/pets_list/stop): ")
    if command == "create":
        create()
    elif command == "read":
        pet_id = int(input("Введите ID питомца: "))
        read(pet_id)
    elif command == "update":
        pet_id = int(input("Введите ID питомца: "))
        update(pet_id)
    elif command == "delete":
        pet_id = int(input("Введите ID питомца: "))
        delete(pet_id)
    elif command == "pets_list":
        pets_list()
    elif command == "stop":
        print("Программа завершена.")
    else:
        print("Неверная команда.")
