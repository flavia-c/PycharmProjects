class Fruit:
    """
    This is a fruit class
    """
    var = 5 #variabila globala

    def __init__(self, name, color, done='10%'): #detaliile obiectului
        self.name = name
        self.color = color

    def _gigi(self): #metoda de a defini functii private - cu underscore
        print('it is private')

    def show(self): #self is always the first parameter within a function from a class
        print(f'This fruit is {self.color} and its name is {self.name}')
        self._gigi()

    @staticmethod
    def apb(a, b):
        return a+b

if __name__ == "__main__":
    plum = Fruit('plum', 'purple')
    apple = Fruit('apple', 'red')

    plum.show()
    apple.show()

    print(Fruit.apb(3, 5))
    print(plum.apb(3, 5))

    print(plum.__dict__)
