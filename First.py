import  math

'''x=int(input())
m=int(input())
y=int(input())
c=x//60
d=x%60
hour = m+c
minute = d+ y
if minute > 60:
    minute = minute % 60
    hour += 1

print(hour)
print(minute)

'''

'''x = 5
y = 10
res = y > x * x or y >= 2 * x and x < y
print(res)


y = 0
while y == 0:
    try:
        x = int(input("Введите число "))
        if x % 2 == 0:
            print("Четное")
        else:
            print("Нечетное")

        z = input("Хотите продолжить? ")
        if z.lower() == "нет":
            y = 1
            print("Ну и иди отсюдова")
        else:
            y = 0
    except ValueError:
        print('Алееее это не число.')'''

'''
a = int(input()) # мин
b = int(input()) # макс
h = int(input()) # реальное=
if a <= h <= b:
    print("Это нормально")
elif a >= h:
    print("Недосып")
elif h >= b:
    print("Пересып")'''

'''year = int(input())
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Високосный")
else:
    print("Обычный")'''

'''a = int(input())
b = int(input())
c = int(input())
p = (a + b + c) / 2
s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
print (s)

'''
'''
x = int(input())
if -15 < x <= 12 or 14 < x < 17 or 19 <= x:
    print(True)

else:
    print(False)'''

'''
a = float(input())
b = float(input())
typeV = input()
if typeV == "+":
    print(a + b)
elif typeV == "-":
    print(a - b)
elif typeV == "*":
    print(a * b)
elif typeV == "/":
    if (b==0):
        print("Деление на ноль!")
    else:
        print(a / b)
elif typeV == "mod":
    if (b==0):
        print("Деление на 0!")
    else:
        print(a % b)
elif typeV == "pow":
    print(a ** b)
elif typeV == "div":
    if (b==0):
        print("Деление на ноль!")
    else:
        print(a // b)'''
'''
tp = input()
summary = 0
pi = 3.14
if tp.lower() == "треугольник":
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a + b + c) / 2
    summary = (p * (p - a) * (p - b) * (p - c)) ** 0.5
elif tp.lower() == "прямоугольник":
    a = float(input())
    b = float(input())
    summary = a * b
elif tp.lower() == "круг":
    r = float(input())
    summary = pi * r ** 2
else:
    print("Вы ввели не ту фигуру")

print(summary)'''
'''
a = int(input())
b = int(input())
c = int(input())
if a >= b >= c:
    print(a)
    print(c)
    print(b)
elif a <= b <= c:
    print(c)
    print(a)
    print(b)
elif a <= c <= b:
    print(b)
    print(a)
    print(c)
elif b <= a <= c:
    print(c)
    print(b)
    print(c)
elif b <= c <= a:
    print(a)
    print(c)
    print(b)
elif c <= a <= b:
    print(b)
    print(c)
    print(a)'''

'''value = int(input())
message = "программист"
ov = "ов"
a = "а"
if value % 100 == 11 or value % 10 == 0 or value % 10 >= 5 or value % 100 == 12 or value % 100 == 13 or value % 100 == 14:
    print(f"{value} {message}" + ov)
elif value % 100 == 1 or value % 10 == 1:
    print(f"{value} {message}")
elif value % 100 == 2 or value % 10 < 5:
    print(f"{value} {message}" + a)'''

"""a,b,c,d,e,f = input()
#a,b,c,d,e,f = number // 100000, number % 100000 // 10000, number % 10000 // 1000, number % 1000 // 100, number % 100 // 10, number % 10 // 1
if a + b + c == d + e + f:
    print("Счастливый")
else:
    print("Обычный")"""


"""i = 0
while i < 5:
    print('*')
    if i % 2 == 0:
        print('**')
    if i > 2:
        print('***')
    i = i + 1




def firstVal(a):
    return a[0]

b = (2,4,6)
print(firstVal(b))


def square(radius, pi = 3.15):
    return pi * (radius ** 2)

print(square(5))
"""


def task_1():
    first: int = 23
    second: float = 3.5
    third: str = "Some Text"
    fourth: list = [1, 5, 8]
    fifth: bool = True

    print(type(first))
    print(type(second))
    print(type(third))
    print(type(fourth))
    print(type(fifth))


task_1()


def task_2() -> int:
    a = [1, 2, 3, 5, 8, 13, 21] # Золотое сечение Фибоначчи
    print(a[0], a[1], a[2])

task_2()

def task_3(a) -> int:
    return a ** 2
print(task_3(3))




