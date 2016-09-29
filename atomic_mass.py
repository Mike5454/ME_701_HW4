import re

atom = open('atomic_masses.txt', 'r')

a = r'Atomic Number = .*'
b = r'Atomic Symbol = .*'
c = r'Mass Number = .*'
d = r'Standard Atomic Weight = .*'

m = [a,b,c,d]
give = []

for i in range(0,4):
    catalog = m[i]
    atm = open('atomic_masses.txt', 'r')
    elem = []
    for line in atm:
        s = str(line)
        n = re.search(catalog, s)
        if n:
           res = n.group(0).split(' = ')
           elem.append(res[1])
    give.append(elem)