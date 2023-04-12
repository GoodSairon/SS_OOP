class Parallelogram:

    def __init__(self, width=0, lenght=0):
        self.width = width
        self.lenght = lenght
        self.squad = None

    def calc_area(self):
        self.squad = int(self.width) * int(self.lenght)
        print(self.squad)

class Square(Parallelogram):

    def calc_area(self):
        self.squad = int(self.width) * int(self.width)
        print(self.squad)

a = Parallelogram(3, 5)
a.calc_area()

b = Square(4)
b.calc_area()
