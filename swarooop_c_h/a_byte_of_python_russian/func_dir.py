import sys

print(dir(sys)) # получим список атрибутов модуля 'sys'

print(dir()) # получим список атрибутов текущего модуля

a = 5 # создадим новую переменную 'a'
print(dir())

del a # удалим имя 'a'
print(dir())

print(dir('print')) # артибуты функции print
