
import csv



with open('Test.csv', 'w', newline='') as myCSVFile:

    writer = csv.writer(myCSVFile, delimiter=';')



    while True:

        naam = input('Wat is uw achternaamnaam? ')

        if naam == 'einde':

            break



        voor1 = input('Wat zijn je voorletters? ')



        geboortedatum = input('Wat is je geboortedatum? ')

        email = input('Wat is je email? ')

        writer.writerow((voor1, naam, geboortedatum, email))