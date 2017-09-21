"""d = {
    'key': 'value',
    'key2': 'value2',
    'a': 2
}

d['key3'] = 'val'
print(d)

d.keys() #lista cu cheile din dictionar
d.items() #tupla de chei si valori

for k, v in d.items():
    print('{} > {}'.format(k, v))"""

d1 = {
    'a': 100,
    'b': 200,
    'c': 300
}

d2 = {
    'a': 50,
    'b': 35,
    'm': 36,
    'n': 555
}

"""VARIANTA 1

d3 = {}

d3.update(d1)
d3.update(d2)
print('d3 =', d3)

for k in d1.keys():
    for k1 in d2.keys():
        if k == k1:
            d3[k] = d1[k] + d2[k1]

print('suma cheilor comune: ', d3)
"""

#VARIANTA2
df = d1

for k in d2.keys():
    if k in d1.keys():
        df[k] = d1[k] + d2[k]
    else:
        df[k] = d2[k]

print(df)