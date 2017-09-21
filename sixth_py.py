with open('fisier.txt', 'r+') as f:
    lines = f.readlines()

v=[]
for line in lines:
    if len(line) >= 3:
        c = line[0:2] + line[2:].capitalize()
        v.append(c)
    else:
        v.append(line)

#rand = input('Dati randul: ')
#val = input('Dati valoarea: ')
#v.insert(int(rand), '{val}\n'.format(val = val))

with open('new.txt', 'w+') as f2:
    f2.writelines(v)