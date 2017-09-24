from math import pi, floor

class espresso:
    cantitate_totala_cafea = 0
    time = 0

    def __init__(self, coffee, sugar, water):
        self.coffee = coffee
        self.sugar = sugar
        self.water = water

    def prepare_coffee(self):
        espresso.cantitate_totala_cafea = self.coffee + self.sugar + self.water
        return espresso.cantitate_totala_cafea

    def prepare_time_coffee(self):
        espresso.time = espresso.cantitate_totala_cafea / pi
        return floor(espresso.time)

    @staticmethod
    def afisare():
        print(f'Cantitatea totala de espresso: {espresso.cantitate_totala_cafea} grame')
        print(f'Timpul de preparare espresso: {floor(espresso.time)} secunde')

if __name__ == '__main__':
    e = espresso(80, 10, 50)
    e.prepare_coffee()
    e.prepare_time_coffee()
    e.afisare()