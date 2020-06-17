# Множество
bri = set(['Бразилия', 'Россия', 'Индия'])

print('Индия' in bri)
print('США' in bri)

bric = bri.copy()
print(bric)

bric.add('Китай')
print(bric)

# проверяет, является ли bric надмножеством bri или нет.
bric.issuperset(bri)

bri.remove('Россия')
print(bri)

# пересечение множеств
bri & bric # OR bri.intersection(bri)
