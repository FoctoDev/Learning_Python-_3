# Запускать из консоли с 3-мя агрументами, например
# python ex13.py first 2nd 3rd
from sys import argv

first, second, third = argv
my_age = int(input("Мой возраст: "))

print("Моя первая переменная называется:", first)
print("Моя вторая переменная называется:", second)
print("Моя третья переменная называется:", third)
print("Моя возраст:", my_age)
