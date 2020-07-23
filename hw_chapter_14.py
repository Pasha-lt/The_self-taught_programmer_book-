# 3. Напишите функцию, которая принимает два объекта в качестве параметров и возвращает True,
# если они являются одним и тем же объектом, и False в противном случае.

class Equalizer:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        if self.a is self.b:  # 'is' в отличии от '==' даст возможность сравнить по типу.
            return 'True'
        return 'False'

print(Equalizer(5, 5.0))  # False
print(Equalizer(5, 5))  # True
print(Equalizer(5, 4))  # False

exit()

# 2. Измените класс Square так, чтобы когда вы выводите объект Square, выводилось сообщение с длинами
# всех четырех сторон фигуры. Например, если вы создадите квадрат при помощи Square(29) и осуществите вывод, Python
# должен вывести строку 29 на 29 на 29 на 29



class Square:
    square_list = []
    def __init__(self, a):
        self.a = a
        self.square_list.append(a)

    def __repr__(self):
        return f'Стороны квадрата - {self.a} на {self.a} на {self.a} на {self.a}!'


sq = Square(15)
print(sq)  # [15, 10, 11]


exit()

# 1. Добавьте переменную square_list в класс Square так, чтобы всякий раз, когда вы создаете новый объект Square,
# он добавлялся в список.

class Square:
    square_list = []
    def __init__(self, a):
        self.a = a
        self.square_list.append(a)

sq = Square(15)
s2 = Square(10)
print(Square.square_list)  # [15, 10]
s3 = Square(11)
print(Square.square_list)  # [15, 10, 11]
