"""print('Hello Testers!')

a=7
b=9

print(f'test sum {a+b} dif {a-b}')"""

l=[]
for i in range(2000, 3201):
    if i%7 ==0:
        if i%5 !=0:
            l.append(i)

print('Lista nr divizibile cu 7 care nu sunt multiple de 5: ', l)

text = input('Dati un text cu litere si cifre: ')

litera = 0
nr = 0

for j in text:
    if j.isalpha():
        litera += 1
    elif j.isdigit():
        nr += 1

print('nr de litere: ', litera, ' si nr de cifre: ', nr)


#print('lista este: ', list(range(5, 10)))