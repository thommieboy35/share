infile = open('kaartnummers.txt', 'r')
lijst = infile.readlines()
infile.close()

aantal = len (lijst)
lst = []


print('deze file telt:' ,aantal, 'regels')

for regel in lijst: #hier zet ik alle kaartnummers in een nieuwe lijst
    deel = regel.split(',')
    lst.append(deel[0])

hoogste = max(lst) #berekenen hoogste kaarnummer
plaats = lst.index(hoogste)+1 #zoek plaats in lijst

print('het grootste kaartnummer:{} en dat staat op regel {}'.format(hoogste, plaats))