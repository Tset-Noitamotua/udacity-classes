def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    
    if node2 in G[node1]:
        G[node1][node2] += 1
    else:
        G[node1][node2]  = 1
    
    if node2 not in G:
        G[node2] = {}

    if node1 in G[node2]:
        G[node2][node1] += 1
    else:
        G[node2][node1]  = 1
    
    return G

import csv
r = csv.reader(open('marvel.txt', 'rb'), delimiter="\t")

marvelG = {}
characters = {}

for (char, book) in r:
    marvelG = make_link(marvelG, char, book)
    characters[char] = True

charG = {}
maxweight = (0, None, None)

for char1 in characters:
    for book in marvelG[char1]:
        for char2 in marvelG[book]:
            if char1 > char2:
                charG = make_link(charG, char1, char2)
                if charG[char1][char2] > maxweight[0]:
                    maxweight = (charG[char1][char2], char1, char2)

print maxweight