infile = open('kaartnummers.txt', 'r')
inhoud = infile.readlines()
infile.close()

for regel in inhoud:
    kaartinfo = regel.split(',')
    print( '{} heeft kaartnummer: {}'.format(kaartinfo[1].strip(), kaartinfo[0]))
