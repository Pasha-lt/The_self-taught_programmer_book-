
# 4. Создайте классы Horse и Rider. Используйте композицию, чтобы смоделировать лошадь с всадником на ней.

class Hourse:
    def __init__(self, hourse_name, age, color, owner):
        self.hourse_name = hourse_name
        self.age = age
        self.color = color
        self.owner = owner


class Rider:
    def __init__(self, name):
        self.name = name

rider1 = Rider('Anton')
hourse1 = Hourse('bucefal', 5, 'black', rider1)
print(hourse1.owner.name)  # Anton


exit()

# 3. Создайте класс Shape. Определите в нем метод what_am_i, который при вызове выводит строку "Я — Фигура .".
# Измените ваши классы Rectangle и Square из предыдущих заданий для наследования от Square, создайте объек-
# ты Square и Rectangle и вызовите в них новый метод.

class Shape:
    def what_am_i(self):
        return f'Я фигура!'


class Rectangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calculate_perimeter(self):
        return self.a + self.b + self.c


class Square(Shape):
    def __init__(self, r):
        self.r = r

    def calculate_perimeter(self):
        return self.r * 4


sh = Shape()
print(sh.what_am_i())  # Я фигура!

sq = Square(10)
print(sq.calculate_perimeter())  # 40
print(sq.what_am_i())  # Я фигура!

rec = Rectangle(3, 4, 5)
print(rec.calculate_perimeter())  # 12
print(rec.what_am_i())  # Я фигура!
exit()


# 2) В классе Square определите метод change_size, позволяющий передавать ему число,
# которое увеличивает или уменьшает (если оно отрицательное) каждую сторону объекта Square на соответствующее значение.


class Square:
    def __init__(self, a):
        self.a = a

    def change_size(self, other):
        self.a = self.a + other


sq = Square(10)
sq.change_size(2)
print(sq.a)  # 12
sq.change_size(3)
print(sq.a)  # 15

exit()


# 1) Создайте классы Rectangle и Square с методом calculate_perimeter, вычисляющим периметр фигур,
# которые эти классы представляют. Создайте объекты Rectangle и Square вызовите в них этот метод.


class Rectangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calculate_perimeter(self):
        return self.a + self.b + self.c


class Square:
    def __init__(self, r):
        self.r = r

    def calculate_perimeter(self):
        return self.r * 4


sq = Square(10)
print(sq.calculate_perimeter())  # 40

rec = Rectangle(3, 4, 5)
print(rec.calculate_perimeter())  # 12
