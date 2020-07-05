print("Число")
a = int(input("> "))

if 0 < a < 10:
    print("10")
elif 10 < a < 100:
    print("100")
elif 100 < a < 1000:
    print("1000")
elif 1000 < a < 10000:
    print("10000")
else:
    print("> 100000")
