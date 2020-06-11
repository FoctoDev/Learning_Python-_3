# Применение continue с циклом while
while True:
    s = input('Введите что-нибудь : ')
    if s == 'выход':
        break
    if len(s) < 3:
        print('Слишком мало')
        continue
    print('Введённая строка достаточной длины')
    # Разные другие действия здесь

# Применение continue с циклом for
for i in range(1, 20, 2):
    if i > 18:
        break
    if i < 10:
        print(i, '- before')
        continue
    print(i, '- after')
    # Разные другие действия здесь
