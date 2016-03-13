import csv

r = csv.reader(open('popname.txt', 'rb'), delimiter=',')
m = {}
f = {}
for row in r:
    if row[1] == 'F':
        f[row[0]] = int(row[2])
    else:
        m[row[0]] = int(row[2])

print 'male: ', len(m), 'female: ', len(f)
s = sorted(f, key=f.get, reverse=True)
for i in range(10):
    print i, ':', s[i], f[s[i]]
