import re

atom = open('atomic_masses.txt', 'r')

a = r'Atomic Number = .*'
b = r'Atomic Symbol = .*'
c = r'Mass Number = .*'
d = r'Standard Atomic Weight = .*'

m = [a,b,c,d]
outFile = open('Atomic_Masses_Output', 'w')

for g in range(0,4):
    if g==0:
        outFile.write('Atomic Number' + '\n' + '\n')
    if g==1:
        outFile.write('\n' + 'Atomic Symbol' + '\n' + '\n')
    if g==2:
        outFile.write('\n' + 'Mass Number' + '\n' + '\n')
    if g==3:
        outFile.write('\n' + 'Standard Atomic Weight' + '\n' + '\n')
    
    atom = open('atomic_masses.txt', 'r')
    entry = m[g]
    for line in atom:
        s = str(line)
        n = re.search(entry, s)
        if n:
            result = n.group(0).split(' = ')
            print result[1]
            
            outFile.write(result[1] + '\n')
    g=g+1
           
outFile.close()