string = input('insert text: ')
list = string.split(',')
list_sort = sorted(list)
print(list_sort)

string_asc = ','.join(list_sort)
print(string_asc)
string_asc_lower = string_asc.lower()
print('Lista concatenata: ', string_asc_lower)

list_sort.reverse()
print('Lista reversibila: ', list_sort)

string_desc = ','.join(list_sort)
string_desc_upper = string_desc.upper()
print('Lista descrescatoare: ', string_desc_upper)

