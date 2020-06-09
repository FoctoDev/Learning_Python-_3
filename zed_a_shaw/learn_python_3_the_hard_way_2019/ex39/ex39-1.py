#  словарь регионов
regions = {
    'Челябинская область': 'CL',
    'Курганская область': 'KGN',
    'Свердловская область': 'SVE',
    'Республика Башкортостан': 'BS',
    'Республика Татарстан': 'TA'
}

# словарь столиц регионов
capital_сities = {
    'CL': 'Челябинск',
    'KGN': 'Курган',
    'BS': 'Уфа',
    'TA': 'Казань',
    'SVE': 'Екатеринбург'
}

print('-' * 10)
print(regions)

print('-' * 10)
print(capital_сities)

# вывод абревиатуры региона
# возвращает значение по указанному ключу
region_45 = regions.get('Курганская область')
region_77 = regions.get('Московская область')
print('-' * 10)
print(f"Курганская область имеет аббревиатуру: {region_45}")
print(f"Московская область имеет аббревиатуру: {region_77}")

# добавление региона и столицы
regions['Тюменская область'] = 'TYU'
capital_сities['TYU'] = 'Тюмень'

# вывод аббревиатур всех регионов
print('-' * 10)
for region, abbrev in list(regions.items()):
    print(f"{region} имеет аббревиатуру {abbrev}")

# вывод всех столиц регионов
print('-' * 10)
for abbrev, capital in list(capital_сities.items()):
    print(f"В регионе {abbrev} столица {capital}")

# вывод всех регионов, возвращаем коллекцию ключей в словаре
print('-' * 10)
for k in regions.keys():
    print(k)

# вывод всех столиц, возвращаем коллекцию значений в словаре
print('-' * 10)
for v in capital_сities.values():
    print(v)

# подсчет количества регионов в словаре
print('-' * 10)
print(f"В словаре {len(regions)} регионов.")

#
region_74 = regions.pop('Челябинская область')
print('-' * 10)
print(f"Код Челябинской область: {region_74}")

# копирование словаря
dict = regions.copy()
print('-' * 10)
print(f"Копия словаря:\n{dict}")

# очистим словарь
dict = dict.clear()
print('-' * 10)
print(dict)

# создание словаря с 3 ключами и одинаковым значением
dict = {} # пустой словарь, не None
dict = dict.fromkeys(['Москва', 'Рязань', 'Саратов'], 'RU')
print('-' * 10)
print(dict)

# или так
cities = ('Санкт-Петербург', 'Самара', 'Кострома', 'Елабуга', 'Севастополь')
country = 'RU'
dict = dict.fromkeys(cities, country)
print('-' * 10)
print(dict)

# получение значения элемента с конкретным ключом
# если ключ не найден, он будет вставлен в словарь вместе с указанным значением.
x = dict.setdefault('Киев', 'UA')
print('-' * 10)
print(x)
x = dict.setdefault('Севастополь', 'UA')
print(x)

# возвращает произвольную пару (ключ, значение) и удалят её из словаря
y = capital_сities.popitem()
print('-' * 10)
print(y)

# и наконец удалим словари
# del regions
# del capital_сities
# print(regions)
# print(capital_сities)
