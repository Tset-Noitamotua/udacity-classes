def clique(n):
    print 'in a clique'
    for j in range(n):
        for i in range(j):
            print i, 'is friends with', j

clique(4)