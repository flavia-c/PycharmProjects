from espresso.espresso_py import Espresso
from capuccino.capuccino_py import Capuccino

if __name__ == '__main__':
    e = Espresso(80, 10, 50)
    e.prepare_coffee()
    e.prepare_time_coffee()
    e.printing()

    c = Capuccino(80, 0, 50, 20)
    c.prepare_coffee()
    c.prepare_time_coffee()
    c.energy()