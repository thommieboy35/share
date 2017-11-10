print('1: ik wil weten hoeveel kuizen er vrij zijn\n'
      '2: Ik wil een nieuwe kluis\n'
      '3: Ik wil even iets uit mijn kluis halen\n'
      '4: Ik geef mijn kluis terug\n')

infile = open('kluizen.txt')
inhoud = infile.readlines()
inhoud1 = infile.read()
infile.close()

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
lst1 = []

def totaal_aantal_kluizen_vrij(Lengtefile):
    Vrij = 12-len(inhoud)
    return Vrij

def nieuwe_kluis(Nummersvrij):
    for Nummer in Nummersvrij:
        if Nummer == inhoud1:
            Nummersvrij.remove(Nummer)
            return Nummersvrij


def kluis_openen():
    nummer = eval(input('Welk kluis nummer wilt u gebruiken?'))
    wachtwoord =eval(input('Wat is de code die u voor deze kluis gaat gebruiken?'))
    lijst = lst1 + nummer + wachtwoord
    for woord in lijst:
        if woord == inhoud1:
            print ('Dit kluis nummer of wachtwoord is al bezet')
        elif woord != inhoud1:
            infile.write(woord)
            print('Uw kluis is gereserveerd')

def kluis_teruggeven()



