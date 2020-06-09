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

        ## Person - композиция животного некоторого вида, т.е класс Person содержит объект pet другого класса (животные)
        self.pet = None

## Employee населдует Person
class Employee(Person):

    def __init__(self, name, salary):
        ## вызывает метод инициализации из родительского класса, чтобы дополнить его
        super(Employee, self).__init__(name)
        ## переменная salary экземпляра класса Employee
        self.salary = salary

## Fish населдует object
class Fish(object):
    pass

## Salmon населдует Fish
class Salmon(Fish):
    pass

## Halibut населдует Fish
class Halibut(Fish):
    pass


## barbos населдует Dog
barbos = Dog("Барбос")

## barsik населдует Cat
barsik = Cat("Барсик")

## mary населдует Person
mary = Person("Машка")

## mary.pet населдует barsik, который наследует Cat
mary.pet = barsik

## filka населдует Employee
filka = Employee("Филька", 120000)

## filka.pet населдует barbos, который наследует Dog
filka.pet = barbos

## flipper населдует Fish
flipper = Fish()

## crouse населдует Salmon
crouse = Salmon()

## harry населдует Halibut
harry = Halibut()
