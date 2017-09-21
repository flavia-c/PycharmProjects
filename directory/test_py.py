from coffee.tea import greater_than
from fifi.lili import concatenate_list

if __name__ == '__main__':
    gt = greater_than(7, 6)

    print('module_pachete_py {}'.format(gt))

    l1 = [4, 5]
    l2 = [6, 7]

    print('module_pachete_py {}'.format(concatenate_list(l1, l2)))
