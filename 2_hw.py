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
