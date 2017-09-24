from math import *
from espresso.espresso_py import espresso

class capuccino(espresso):
    def __init__(self, c_coffee, c_sugar, c_water,  milk):
        super().__init__(coffee = c_coffee, sugar = c_sugar, water = c_water)
        self.milk = milk

    def prepare_coffee(self):
        super().prepare_coffee()
        self.add_milk = espresso.cantitate_totala_cafea + self.milk
        print(f'Cantitatea totala cappuccino: {self.add_milk} grame')

    def prepare_time_coffee(self):
        super().prepare_time_coffee()
        self.new_time = espresso.time + sqrt(self.milk)
        print(f'Timpul de preparare cappuccino: {floor(self.new_time)} secunde')

    def energy(self):
        self.en = self.milk * pow(self.coffee, 2)
        print(f'Energia totala: {floor(self.en)} Jouli')

if __name__ == '__main__':
    c = capuccino(80, 10, 50, 20)
    c.prepare_coffee()
    c.prepare_time_coffee()
    c.energy()

