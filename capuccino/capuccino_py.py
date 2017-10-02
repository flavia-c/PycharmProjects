import math
from espresso.espresso_py import Espresso

class Capuccino(Espresso):
    def __init__(self, c_coffee, c_sugar, c_water,  milk):
        super().__init__(coffee=c_coffee, sugar=c_sugar, water=c_water)
        self.milk = milk

    def prepare_coffee(self):
        add_milk = super().prepare_coffee() + self.milk
        print(f'Cantitatea totala cappuccino: {add_milk} grame')

    def prepare_time_coffee(self):
        new_time = super().prepare_time_coffee() + math.sqrt(self.milk)
        print(f'Timpul de preparare cappuccino: {math.floor(new_time)} secunde')

    def energy(self):
        en = self.milk * math.pow(self.coffee, 2)
        print(f'Energia totala: {math.floor(en)} calorii')

if __name__ == '__main__':

    c = Capuccino(80, 10, 50, 20)
    c.prepare_coffee()
    c.prepare_time_coffee()
    c.energy()

