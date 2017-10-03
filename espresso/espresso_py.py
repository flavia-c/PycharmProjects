import math

class Espresso:

    def __init__(self, coffee, sugar, water):
        self.coffee = coffee
        self.sugar = sugar
        self.water = water

    def prepare_coffee(self):
        self.quantity = self.coffee + self.sugar + self.water
        return self.quantity

    def prepare_time_coffee(self):
        self.time = self.quantity / math.pi
        return math.floor(self.time)

    def printing(self):
        print(f'Cantitatea totala de espresso: {self.quantity} grame')
        print(f'Timpul de preparare espresso: {math.floor(self.time)} secunde')

if __name__ == '__main__':

    e = Espresso(80, 10, 50)
    e.prepare_coffee()
    e.prepare_time_coffee()
    e.printing()