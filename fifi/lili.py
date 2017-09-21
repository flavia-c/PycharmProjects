def concatenate_list(a, b):
    """
    concatenates 2 lists
    """
    a.extend(b)
    return a

def mimi():
    l1 = [4, 3, 5]
    l2 = [4, 6, 7]
    nl = concatenate_list(l1, l2)
    print('nl = {}'.format(nl))

if __name__ == '__main__':
    mimi()