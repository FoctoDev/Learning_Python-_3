def my_func(arg1, arg2, arg3):
    print(f"Первый аргумент: {arg1}\nВторой аргумент: {arg2}\nИ третий аргумен {arg3}.")
    print(f"Сумма всех аргументов равна: {arg1} + {arg2} + {arg3} =", arg1 + arg2 + arg3)
    print(f"Я перемножил все аргументы: {arg1} * {arg2} * {arg3} =", arg1 * arg2 *arg3)

print("Первый вызов функции:")
my_func(1, 5, 10)

print("\nВтрой вызов функции:")
my_func(1 + 2, 5 - 2, 10 + 2)

print("\nТретий вызов функции:")
my_func(1 * 2, 5 // 2, 10 - 7)

new_arg1 = 7
new_arg2 = 3
new_arg3 = 24

print("\nЧетвертый вызов функции:")
my_func(new_arg1, new_arg2, new_arg3)

print("\nПятый вызов функции:")
my_func(new_arg1 // 2, new_arg2 * 2, new_arg3 - 8)

print("\nШестой вызов функции:")
my_func(new_arg1 - 2, new_arg2 + 2, new_arg3 // 3)

print("\nСедьмой вызов функции:")
my_func(new_arg1, new_arg1, new_arg1)

print("\nВосьмой вызов функции:")
my_func(new_arg1 - 2, new_arg2 + new_arg1, new_arg3 - new_arg2)

print("\nДевятый вызов функции:")
my_func(new_arg1 * 2 - new_arg2 // 3, (new_arg2 + new_arg1) * 2 // 5, new_arg3 - new_arg2 * 2)

print("\nДесятый вызов функции:")
my_func((new_arg1 - new_arg2) * 36 / 100, (new_arg2 + new_arg1) * 2 + (new_arg3 - new_arg2) / 2, new_arg3 + new_arg2 - new_arg3)

print("\nА теперь введем свои аргументы")

num1 = int(input("Первое число: "))
num2 = int(input("Второе число: "))
num3 = int(input("Третье чмсло: "))

print("\nОдиннадцатый вызов функции:")
my_func(num1 * 3, num2 // 2, num3 + 16)
