import string, re

def valid(f):
    "Formula f is valid iff it has no numbers with leading zero and evals true."
    try:
        return eval(f) == True
    except ZeroDivisionError:
        return False
    except:
        return False

e = ('1 + 2 == 3', '1 + 1 == 5', '1 + 5 ==')
for i in e:
    print i, '=>', valid(i)