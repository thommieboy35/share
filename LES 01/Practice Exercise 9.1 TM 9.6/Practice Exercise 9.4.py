import csv
with open('Gamers.csv', 'w', newline='') as myCSVFile:
    writer = csv.reader(myCSVFile, delimiter= ';')
    writer.writerow('artikelnummer', '')
    while True:
        artikelnummer = input ('Wat is de naam van het artikel?')
        if artikelnummer == '':
            break
        artikelcode = input('Wat is het artikelcode?')
        naam = input('Wat is de naam van het product?')
        voorraad = input('Wat is de voorraad van het product?')
        prijs=input('wat is de prijs van het product?')
        writer.writerow((artikelnummer, artikelcode, naam, voorraad, prijs))


