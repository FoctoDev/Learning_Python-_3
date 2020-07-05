people = 50
cars = 40
trucks = 15
buses = 10


if cars > people:
    print("Поедем на машине.")
elif cars < people:
    print("Не поедем на машине.")
else:
    print("Мы не можем выбрать.")

if trucks > cars:
     print("Слишком много грузовиков.")
elif trucks < cars:
    print("Может, поехать на грузовике?")
else:
    print("Мы до сих пор не можем выбрать.")

if people > trucks:
    print("Хорошо, давайте поедем на грузовике.")
else:
    print("Прекрасно, давайте останемся дома.")


if cars > people or buses < people:
    print("Поедем на машине.")
elif cars < people:
    print("Не поедем на машине.")
else:
    print("Мы не можем выбрать.")


if cars > people and buses < people:
    print("Поедем на машине.")
elif cars < people:
    print("Не поедем на машине.")
else:
    print("Мы не можем выбрать.")
