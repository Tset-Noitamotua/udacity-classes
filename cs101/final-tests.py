def tricky_loop(p):
    cnt = 0
    l = len(p)
    while True:
        cnt += 1
        if len(p) == 0:
            break
        else:
            if p[-1] == 0:
                p.pop() # assume pop is a constant time operation
            else:
                p[-1] = 0
    print 'Length:', l, 'count:', cnt
    return 101

#tricky_loop(range(10))
#tricky_loop(range(100))
#tricky_loop(range(1000))

#Reverse Index

#Define a procedure, reverse_index, that takes as input a Dictionary, and
#returns a new Dictionary where the keys are the values in the input dictionary.
#The value associated with a key in the result is a list of all the keys in the
#input dictionary that match this value (in any order).

def reverse_index(dict):
    result = {}
    for k in dict:
        if dict[k] in result:
            result[dict[k]].append(k)
        else:
            result[dict[k]] = [k]
    return result

#For example,

winners_by_year = {
    1930: 'Uruguay', 1934: 'Italy', 1938: 'Italy', 1950: 'Uruguay',
    1954: 'West Germany', 1958: 'Brazil', 1962: 'Brazil', 1966: 'England',
    1970: 'Brazil', 1974: 'West Germany', 1978: 'Argentina',
    1982: 'Italy', 1986: 'Argentina', 1990: 'West Germany', 1994: 'Brazil',
    1998: 'France', 2002: 'Brazil', 2006: 'Italy', 2010: 'Spain' }

#wins_by_country = reverse_index(winners_by_year)

#print wins_by_country['Brazil']
#>>> [1958, 2002, 1970, 1994, 1962]

#print wins_by_country['England'] 
#>>> [1966]

#Same Structure

#Define a procedure, same_structure, that takes two inputs. It should output
#True if the lists contain the same elements in the same structure, and False
#otherwise. Two values, p and q have the same structure if:

#    Neither p or q is a list.

#    Both p and q are lists, they have the same number of elements, and each
#    element of p has the same structure as the corresponding element of q.


#For this procedure, you can use the is_list(p) procedure from Homework 6:

def is_list(p):
    return isinstance(p, list)

def same_structure(a, b):
    ila = is_list(a)
    ilb = is_list(b)
    if not ila and not ilb:
        return True
    elif ila and not ilb:
        return False
    elif not ila and not ilb:
        return False
    if len(a) != len(b):
        return False
    for i in range(len(a)):
        result = same_structure(a[i], b[i])
        if result == False:
            return False
    return True

#Here are some examples:

#print same_structure(3, 7)
#>>> True

#print same_structure([1, 0, 1], [2, 1, 2])
#>>> True

#print same_structure([1, [0], 1], [2, 5, 3])
#>>> False

#print same_structure([1, [2, [3, [4, 5]]]], ['a', ['b', ['c', ['d', 'e']]]])
#>>> True

#print same_structure([1, [2, [3, [4, 5]]]], ['a', ['b', ['c', ['de']]]])
#>>> False