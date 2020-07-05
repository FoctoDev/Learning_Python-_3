print("Введите начало диапазона.")
x = int(input("> "))

print("Введите конец диапазона.")
y = int(input("> "))

def count_string_for(a, b):
    i = 0
    numbers = []

    for i in range(a, b):
        print(f"В начале значение i равно {i}")
        numbers.append(i)

        # i += b
        print("Текущие значения: ", numbers)
        print(f"В конце значение i равно {i}")


count_string_for(x, y)
