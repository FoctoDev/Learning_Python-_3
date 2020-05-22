## Animal наследует object
class Animal(object):
    pass

## Dog наследует Animal
class Dog(Animal):

    def __init__(self, name):
        ## переменная name экземпляра класса Dog
        self.name = name

## Cat наследует Animal
class Cat(Animal):

    def __init__(self, name):
        ## переменная name экземпляра класса Cat
        self.name = name

## Person населдует object
class Person(object):

    def __init__(self, name):
        ## переменная name экземпляра класса Person
        self.name = name

        ## Person - композиция животного некоторого вида
        self.pet = None

##
class Employee(Person):

    def __init__(self, name, salary):
        ## вызывает метод инициализации из родительского класса, чтобы дополнить его
        super(Employee, self).__init__(name)
        ## переменная name экземпляра класса Employee
        self.salary = salary
