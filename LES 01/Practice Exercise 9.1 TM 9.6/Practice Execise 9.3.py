import csv

with open('Gamers.csv', 'r') as myCSVFile:
    reader = csv.reader(myCSVFile, delimiter=';')

    hoogstescore = 0
    hdatum = ''
    naam = ''

    for row in reader:
        score = int(row[2])

        if score > hoogstescore:

            hoogstescore = score
            naam=row[0]
            hdatum = row[1]



    print('De hoogste score is', hoogstescore, 'op', hdatum, 'behaald door', naam )
