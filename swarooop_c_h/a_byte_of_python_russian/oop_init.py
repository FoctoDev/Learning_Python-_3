class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Привет! Меня зовут', self.name)

p = Person('Swaroop')
p.say_hi()

# Предыдущие 2 строки можно
# Person('Swaroop').say_hi()

# Здесь при вызове класса в круглых скобках передаётся значения 'Swaroop',
# которое будет присвоено параметрам метода __init__().
# Первый его параметр – self – ссылка на сам только что созданный объект.
# Второй - name.

# В данном примере конструктор класса __init__()
# не позволит создать объект без обязательного поля name.
# p = Person() вызывет исключение и объект не будет создан
# TypeError: __init__() missing 1 required positional argument: 'name'
