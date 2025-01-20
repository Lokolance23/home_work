def equal(a, b):

    if a > b:
        x = f"Большое число {a}"
    elif a < b:
        x = f"Большое число {b}"
    else:
        x = "Значения равны"
    print(x)

a = int(input("Введите первое число "))
b = int(input("Введите второе число "))
equal(a, b)

def equal135(a, b):

    if a - b == 135 or b - a == 135:
        x = f"YES"
    else:
        x = "NO"
    print(x)

a = int(input("Введите первое число "))
b = int(input("Введите второе число "))
equal135(a, b)

def seasons(a):
    if 0 < a < 3 or 10 < a < 13:
        y = "Зима"
    elif 2 < a < 6:
        y = "Весна"
    elif 5 < a < 9:
        y = "Лето"
    elif 8 < a < 12:
        y = "Осень"
    else:
        y = "Ввели неправильное значение"
    print(y)

a = int(input("Введите номер месяца "))

seasons(a)

def more10(a, b, c):

    if a > 10 and b > 10 and c > 10:
        x = f"YES"
    else:
        x = "NO"
    print(x)

a = int(input("Введите первое число "))
b = int(input("Введите второе число "))
c = int(input("Введите второе число "))

more10(a, b, c)


def positiveNum(a, b, c, d, e) -> int:

    x = [a, b, c, d, e]
    i = 0

    for y in x:
        if y > 0:
            i += 1

    print(f"Положительных чисел {i}")
1
a = int(input("Введите первое число "))
b = int(input("Введите второе число "))
c = int(input("Введите второе число "))
d = int(input("Введите второе число "))
e = int(input("Введите второе число "))

positiveNum(a, b, c, d, e)

def timeToDays(years, months):
    days = years * 365 + months * 29
    print(f"В итоге получается {days} дней")

years = int(input("Введите количество лет "))
months = int(input("Введите количество месяцев "))
timeToDays(years, months)
