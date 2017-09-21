def greater_than(a, b):
    """

    :param a: is an int
    :param b: is an int
    :return: turns true if a > b
    """
    if a>b:
        return True
    return False

if __name__ == '__main__': #ruleaza strict functia apelata din pachet in module_pachete_py
    gt = greater_than(7, 5)
    print('tea {}'.format(gt))