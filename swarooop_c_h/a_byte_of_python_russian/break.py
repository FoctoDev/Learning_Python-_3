# применение break в цикле while
while True:
    s = input('Введите что-нибудь : ')
    if s == 'выход':
        break
    print('Длина строки:', len(s))
print('Завершение')

# применение break в цикле for
for i in range(1, 10):
    if i == 5:
        break
    print(i)
print('Завершение')
