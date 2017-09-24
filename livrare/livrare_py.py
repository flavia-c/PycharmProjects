from espresso.espresso_py import espresso
from capuccino.capuccino_py import capuccino

if __name__ == '__main__':
    e = espresso(80, 10, 50)
    e.prepare_coffee()
    e.prepare_time_coffee()
    e.afisare()

    c = capuccino(80, 0, 50, 20)
    c.prepare_coffee()
    c.prepare_time_coffee()
    c.energy()