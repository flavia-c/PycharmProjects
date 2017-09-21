"""def nume(param):
    #actiuni
    return #optional

def suma(a, b=9):
    s = a + b
    return s

s = suma(a=1, b=8)

print(s)"""

"""1 func: citim de la tastatura si returnam int: 

2 func: le comparam
daca nr1 >= nr2 => true daca nu false

cu output (true sau false),

3 func: 
daca e true atunci cerem de la tastatura altul (nr1)

4 func:
daca e false, sa printam primul nr impar mai mic ca el"""

def citire():
    nr = input('Dati un nr: ')
    return int(nr)

def compar(a, b):
    if a >= b:
        return True
    else:
        return False

"""def new_nr():
    new = citire()
    return new"""

def impar(b):
    if b%2 == 1:
        return b-2
    else:
        return b-1

a = citire()
b = citire()
c = compar(a, b)
print(c)

if c:
    a = citire()
else:
    a = impar(a)

print('a={}, b={}'.format(a, b))



