l = []

print(type(l))

print(len(l))

l.append('abc')
l.append([1, 2])
l.append(6)

l.extend([1, 4, 5, 6])

print('sirul este: ', l)
print('me de elemente: ', len(l))
print('element 2: ', l[1])
print('de la el 4 pana la sf: ', l[3:])
print('ultimul element: ', l[-1])
print('penultimul element: ', l[-2])
print('ultimele elemente: ', l[-2:])

cuvant = 'ana are mere'

print(cuvant[-4:])
print(cuvant.split(' '))

print(l.index(1))

for item in l:
    print(item)

for item in l:
    tipul = type(item)
    print(f'{tipul.__name__}')

if 'a' in l:
    print('a')
else:
    if 5 not in l:
        print('5')
    else:
        print('go home')

m=[]
print('lista initiala: ', l)

for item in l:
    tip = type(item)
    if tip == int:
        m.append(item)
print(m)
m.reverse() #lista inversata
print(m)

while 5 in l:
    print('a')  # atata timp cat exista 5 in lista, print 'a'. la primul el gasit, va iesi din functie
    break

while 5 in l:
    l.pop()  #elimina ultimul element din lista
    print('noua lista este: ', l)

"""while 5 in l:
    c = l.pop(5)  #elimina elementul de pe pozitia indicata
    print('Elementul eliminat din lista: ', c)"""

new_list = []
for i in l:
    if type(i) == int:
        new_list.append(i)

int_list = [i for i in l if type(i) == int]

print(int_list)
print(new_list)