class Rectangle:
    def __init__(self, height: int, width: int):
        self.height = height
        self.width = width

    def square(self):
        square = self.width * self.height
        print(f'Площадь равна {square}')

    def perimeter(self):
        perimetr = (self.height + self.width) * 2
        print(f'Периметр равен {perimetr}')


first = Rectangle(2,3)
second = Rectangle(5, 7)
third = Rectangle(8, 10)
first.square()
first.perimeter()
second.square()
second.perimeter()
third.square()

class Math:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def addition(self):
        sum = self.a + self.b
        print(f'Сумма равна {sum}')

    def multiplication(self):
        summ = self.a * self.b
        print(f'Умножение равно {summ}')

    def division(self):
        if self.b != 0:
            div = self.a / self.b
            print(f'Деление равно {div}')
        else:
            print("Деление невозможно на 0")

    def subtraction(self):
        sub = self.a - self.b
        print(f'Вычитание равно {sub}')

first_try = Math(15, 10)
first_try.addition()
first_try.division()
first_try.subtraction()
first_try.multiplication()

# По данному заданию не понял, что именно нужно выводить. Нужно ли просто возвращать текст в методе или с принтом
class Button:
    def __init__(self, text: str, type: str = "button", locator: str = ""):
        self.text = text
        self.var = type
        self.locator = locator

    def click_button(self):
        print(f"Клик по кнопке {self.text}")

text_box = Button("Text Box")
text_box.click_button()
check_box = Button("Check box")
check_box.click_button()
radio_button = Button("Radio button")
radio_button.click_button()
web_tables = Button("Web tables")
web_tables.click_button()
buttons = Button("Buttons")
buttons.click_button()
links = Button("Links")
links.click_button()
broken_links = Button("Broken links")
broken_links.click_button()
upload_download = Button("Upload and download")
upload_download.click_button()
dynamic_prop = Button("Dynamic Properties")
dynamic_prop.click_button()
