class Point:
    """Определяет координаты точки в двумерном простарнстве"""
    x = 1
    y = 1

print(dir(Point))

print(Point.__class__) ## <class 'type'>
print(Point.__delattr__) ## <slot wrapper '__delattr__' of 'object' objects>
print(Point.__dict__) ## {'__module__': '__main__', '__doc__': 'Определяет координаты точки в двумерном простарнстве', 'x': 1, 'y': 1, '__dict__': <attribute '__dict__' of 'Point' objects>, '__weakref__': <attribute '__weakref__' of 'Point' objects>}
print(Point.__dir__) ## <method '__dir__' of 'object' objects>
print(Point.__doc__) ## Определяет координаты точки в двумерном простарнстве
print(Point.__eq__) ## <slot wrapper '__eq__' of 'object' objects>
print(Point.__format__) ## <method '__format__' of 'object' objects>
print(Point.__ge__) ## <slot wrapper '__ge__' of 'object' objects>
print(Point.__getattribute__) ## <slot wrapper '__getattribute__' of 'object' objects>
print(Point.__gt__) ## <slot wrapper '__gt__' of 'object' objects>
print(Point.__hash__) ## <slot wrapper '__hash__' of 'object' objects>
print(Point.__init__) ## <slot wrapper '__init__' of 'object' objects>
print(Point.__init_subclass__) ## <built-in method __init_subclass__ of type object at 0x0317C200>
print(Point.__le__) ## <slot wrapper '__le__' of 'object' objects>
print(Point.__lt__) ## <slot wrapper '__lt__' of 'object' objects>
print(Point.__module__) ## __main__
print(Point.__ne__) ## <slot wrapper '__ne__' of 'object' objects>
print(Point.__new__) ## <built-in method __new__ of type object at 0x5E5D8B78>
print(Point.__reduce__) ## <method '__reduce__' of 'object' objects>
print(Point.__reduce_ex__) ## <method '__reduce_ex__' of 'object' objects>
print(Point.__repr__) ## <slot wrapper '__repr__' of 'object' objects>
print(Point.__setattr__) ## <slot wrapper '__setattr__' of 'object' objects>
print(Point.__sizeof__) ## <method '__sizeof__' of 'object' objects>
print(Point.__str__) ## <slot wrapper '__str__' of 'object' objects>
print(Point.__subclasshook__) ## <built-in method __subclasshook__ of type object at 0x0317C200>
print(Point.__weakref__) ## <attribute '__weakref__' of 'Point' objects>

print(Point.x) ##
print(Point.y) ##

class SomeClass():
    """Описание класса"""

    def __init__(self, x, y, z):
        """Описание метода класса"""
        self.x = x # Координата по оси X
        self.y = y # Координата по оси Y
        self.z = z # Координата по оси Z

coord = SomeClass(10, 5, 6)

print(SomeClass.__init__) ## <function SomeClass.__init__ at 0x0163D340>
print(coord.__init__) ## <bound method SomeClass.__init__ of <__main__.SomeClass object at 0x01639148>>
