class Strings:

    def __init__(self, nr):
        self.nr = nr
        self.propozitie = ''

    def getString(self): #to get a string from console input
        for i in range(self.nr):
            self.cuv = input('Dati cuvantul: ')
            self.propozitie = self.propozitie + self.cuv + ' '

    def printString(self):
        a = self.propozitie.upper()
        b = a[:-1] + '.'
        print('Propozitia este: {}'.format(b))

if __name__ == '__main__':
    q = Strings(3)

    q.getString()
    q.printString()