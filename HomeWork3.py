a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = [x for x in range(a, b) if x % 5 == 0]

print(c)


