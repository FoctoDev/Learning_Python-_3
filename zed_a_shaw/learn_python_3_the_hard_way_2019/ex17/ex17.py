from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Копирование данных из файла {from_file} в файл {to_file}")

# Можете следующие две строки кода разместить в одну?
# in_file = open(from_file, encoding = 'utf-8')
# indata = in_file.read()
indata = open(from_file, encoding = 'utf-8').read()

print(f"Исходный файл имеет размер {len(indata)} байт")

print(f"Целевой файл существует? {exists(to_file)}")
print("Готов, нажмите клавишу Enter для продолжения или CTRL+С для отмены.")
input()

out_file = open(to_file, 'w', encoding = 'utf-8')
print("Вы точно хотите скопировать данные? Для продолжения нажмите Enter, для отмены CTRL+C.")
input()
out_file.write(indata)

print("Отлично, всё сделано.")

out_file.close()
# in_file.close()
