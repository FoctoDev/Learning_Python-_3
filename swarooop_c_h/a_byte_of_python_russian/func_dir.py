import sys

print(dir(sys)) # получим список атрибутов модуля 'sys'
print('\n', dir()) # получим список атрибутов текущего модуля

a = 5 # создадим новую переменную 'a'
print('\n', dir())

del a # удалим имя 'a'
print('\n', dir())

print('\n', dir('print')) # артибуты функции print
print('\n', dir(str)) # атрибуты класса str
