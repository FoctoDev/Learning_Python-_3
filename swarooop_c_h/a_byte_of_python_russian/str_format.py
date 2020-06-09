age = 26
name = 'Swaroop'

print('Возраст {0} -- {1} лет.'.format(name, age))
print('Почему {0} забавляется с этим Python?'.format(name))

# ещё можно так
print('Возраст {} -- {} лет.'.format(name, age))
print('Почему {} забавляется с этим Python?'.format(name))

# или так
print(f"{name}, тебе {age} лет?")

# десятичное число (.) с точностью в 3 знака для поавающих:
print('{0:.3}'.format(1/3))

# заполнить подчёркиваниями (_) с центровкой текста (^) по ширине 11:
print('{0:_^11}'.format('hello'))

#  по ключевым словам:
print('{name} написал {book}'.format(name='Swaroop', book='a Byte of Python'))
