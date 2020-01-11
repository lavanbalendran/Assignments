def iterate(dictionary):
    """
    @type dictionary: dict

    Print each key and value in dictionary.
    
    >>> iterate({'a': 40, 'b': 50, 'c': 60, 'd': 70})
    a : 40
    b : 50
    c : 60
    d : 70
    """
    for elem in dictionary.keys():
        print(elem,":", dictionary[elem])
        
def square_dict(num):
    """
    @type num: int

    Print a dictionary with the key as an int and its value as the square of
    the int. The number of elements in the dictionary is the same as num. 

    >>> square_dict(5)
    {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    >>> square_dict(9)
    {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
    """
    start = 1
    dic = {}
    while start <= num:
        dic[start] = start**2
        start = start + 1
    print(dic)        

def combine_dicts(d1, d2):
    """
    @type d1: dict
    @type d2: dict

    Print a new dictionary that combines all the keys of two dictionaries into
    one. If the two dictionaries have the same key, their values are added.

    >>> combine_dicts({1: 1, 2: 4, 3: 9},{1: 1, 2: 4, 3: 9, 4: 16, 5: 25})
    {1: 2, 2: 8, 3: 18, 4: 16, 5: 25}

    >>> combine_dicts({'a':3, 'b':4, 'c':5},{'a':9, 'c':8, 'd':7})
    {'a': 12, 'b': 4, 'c': 13, 'd': 7}
    """
    dic2 = {}
    len_d1 = len(d1)
    len_d2 = len(d2)
    for key in d1.keys():
        if key in d2.keys():
            val = d1[key] + d2[key]
            dic2[key] = val
        else:
            dic2[key] = d1[key]
    for key2 in d2.keys():
        if key2 not in dic2.keys():
            dic2[key2] = d2[key2]
    print(dic2)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
            
