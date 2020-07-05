print("Введите целое чисто от 1 до 20.")
x = int(input("> "))

print("Введите второе целое чисто от 1 до 20.")
y = int(input("> "))

def count_string(a, b):
    i = 0
    numbers = []

    while i < a:
        print(f"В начале значение i равно {i}")
        numbers.append(i)

        i += b
        print("Текущие значения: ", numbers)
        print(f"В конце значение i равно {i}")


count_string(x, y)
