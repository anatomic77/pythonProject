class Square:
    def __init__(self, a=10):
        self.a = a

    def calculate_area(self):
        return f'площадь квадрата равна {self.a ** 2}'

    def draw(self):
        for row in range(self.a):
            for column in range(self.a):
                print('*', end='  ')
            print()


class Pr(Square):
    def __init__(self, a=10, b=10):
        super().__init__(a)
        self.b=b

    def calculate_area(self):
        return f'площадь прямоугольника равна {self.a * self.b}'


    def draw(self):
        for row in range(self.a):
            for column in range(self.b):
                print('*', end='  ')
            print()


p1 = Pr(5)
p2 = Pr(10, 15)

print(p1.calculate_area())
print(p2.calculate_area())

p2.draw()

# class Elevator:
#     def __init__(self, floors=5, stop=3, move=int(input())):
#         self.floors = floors
#         self.stop = stop
#         self.move = move
#
#     def elevator_up(self):
#         if self.stop <= self.floors:
#             print(f'Лифт двигается вверх на {self.stop} этож')
#             self.stop += 1
#         else:
#             print(f'Лифт не может подняться выше')
#
#     def elevator_down(self):
#         if self.stop > 1:
#             self.stop -= 1
#             print(f'Лифт двигается вниз на {self.stop} этаж')
#         else:
#             print(f'Лифт не может опуститься')
#
#     def el_move(self):
#         if self.floors <= self.move:
#             self.stop = self.move
#             print(f'Лифт двигается  на {self.move} этаж')
#         else:
#             print(f'Лифт не может опуститься')
#
#
# el = Elevator(10, 5)
# print('----')
#
# el.el_move()