def maximum (x, y):
    if x > y:
        return x
    elif x == y:
        return 'Числа равны'
    else:
        return y

print(maximum(2, 3))

# max -- встроенная функция поиска максимума
print(max(3, 90, 18))
