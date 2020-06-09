class Parent(object):
    """Создается класс Родитель"""

    def override(self):
        print("РОДИТЕЛЬ override()")

    def implicit(self):
        print("РОДИТЕЛЬ implicit()")

    def altered(self):
        print("РОДИТЕЛЬ altered()")

class Child(Parent):
    """Создается класс Ребенок, наследующий Родитель"""

    def override(self):
        print("ПОТОМОК override()")

    def altered(self):
        print("ПОТОМОК, ДО ВЫЗОВА altered() В РОДИТЕЛЕ")
        super(Child, self).altered()
        print("ПОТОМОК, ПОСЛЕ ВЫЗОВА altered() В РОДИТЕЛЕ")

dad = Parent() # создается dad как экземпляр класса Parent
son = Child() # создается son как экземпляр класса Child

dad.implicit() # или Parent().implicit(), вывод -- РОДИТЕЛЬ implicit()
son.implicit() # или Child().implicit(), вывод -- РОДИТЕЛЬ implicit(), наследует Child implicit() от Parrent

dad.override() # или Parent().override(), вывод -- РОДИТЕЛЬ override()
son.override() # или Child().override(), вывод -- ПОТОМОК override(), Child переопределят override() у Parrent

dad.altered() # или Parent().altered(), вывод -- РОДИТЕЛЬ altered()
son.altered() # или Child().altered(), сначала Child переопределят altered(),
# затем вызывается Parent().altered(), затем снова вызывается Child().altered()
## вывод
# ПОТОМОК, ДО ВЫЗОВА altered() В РОДИТЕЛЕ
# РОДИТЕЛЬ altered()
# ПОТОМОК, ПОСЛЕ ВЫЗОВА altered() В РОДИТЕЛЕ
