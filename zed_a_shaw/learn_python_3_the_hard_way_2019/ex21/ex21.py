def add(a, b):
    print(f"СЛОЖЕНИЕ {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"ВЫЧИТАНИЕ {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"УМНОЖЕНИЕ {a} * {b}")
    return a * b

def divide(a, b):
    print(f"ДЕЛЕНИЕ {a} / {b}")
    return a / b


print("Давайте выполним ннесколько вычислений с помощью функций!")

age = add(30, 5)
height = subtract(190, 4)
weight = multiply(35, 2)
iq = divide(250, 2)

print(f"Возраст: {age}, Рост: {height}, Вес: {weight}, IQ: {iq}")


# Головоломка в качетсве дополнительного задания, введитекод в любом случае.
print("Это головоломка.")
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
what_q = age + height - weight * iq / 2
# what2 = add(iq + 200, subtract(weight, multiply(age // 10, divide(height, 2))))

print("Получается: ", what, "Вы можете это вичислить вручную?")
print(f"Вручную получается уравнение: {age} + {height} - {weight} * {iq} / 2 = ", what_q)
# Более подробнее о головоломке
# print(divide(iq, 2))
# print(multiply(weight, divide(iq, 2)))
# print(subtract(height, multiply(weight, divide(iq, 2))))
# print(add(age, subtract(height, multiply(weight, divide(iq, 2)))))
