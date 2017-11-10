import csv
with open('Gamers.csv', 'r',) as myCSVFile:
    reader = csv.reader(myCSVFile, delimiter=';')
    duursteartikel = 0
    for row in reader:
        prijs = float(row['prijs'])
        if prijs > duursteartikel:
            duursteartikel = prijs
            naamduurste = row['naam']
            print(duursteartikel, naamduurste)

