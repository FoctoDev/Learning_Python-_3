# похоже на сценарий с argv, функция имеет короткое имя, характеризующее, что она делает "печать два", то есть печатает 2 агруемента
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# ок, здесь вместо *args мы делаем следующее
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# принимаем только один аргумент
def print_one(arg1):
    print(f"arg1: {arg1}")

# не принимаем агрументов
def print_none():
    print("А я ничего не получаю.")


print_two("Александр","Иванов")
print_two_again("Иванов","Александр")
print_one("Первый!")
print_none()
