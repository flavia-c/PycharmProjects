"""f = open('fisier.txt', 'r+')
#f = open('nume_fisier', 'mod deschidere') r = read only
content = f.read()
content1 = f.read()
f.seek(0)
print(content1)
f.close()"""

with open('fisier.txt', 'r+') as f:
    lines = f.readlines()

v=[]
for line in lines:
    c = line.capitalize()
    v.append(c)

rand = input('Dati randul: ')
val = input('Dati valoarea: ')

if int(rand) <= len(lines):
    v.insert(int(rand), '{v}\n'.format(v = val))
else:
    print('Fisierul are doar {} linii'.format(len(lines)))

with open('new.txt', 'w+') as f2:
    f2.writelines(v)

"""alias:
f.open()
content=f.read()
f.close

f2 = open('fisier.txt', 'r+')
content = 'test test test'
f2.write(content)
f2.close()
print('f2 inchis: ', f2.closed)""" #verific ca fisierul e inchis