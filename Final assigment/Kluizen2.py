def toon_aantal_kluizen_vrij():
    infile = open('kluizen.txt', 'r')
    kluizendata = infile.readlines()
    infile.close()
    aantalkluizen = len(kluizendata)
    aantalvrij = 12 - aantalkluizen
    print('aantalvrij {}'.format(aantalvrij))


def nieuwe_kluis():
    infile = open('kluizen.txt', 'r')
    kluizendata= infile.read()
    infile.close()
    test = kluizendata.split(";")





def kluis_openen():
    infile = open('kluizen.txt', 'r')
    kluizendata = infile.readlines()
    infile.close()
    stringnummer = input('wat is je nummer?')
    code = input('wat is je code:')
    gegevenscorrect = False
    for regel in kluizendata:
        gegevens_van1_kluis = regel.split(';')
        stringkluisnummer = gegevens_van1_kluis[0]
        kluiscode = gegevens_van1_kluis[1].strip()
        if stringnummer == stringkluisnummer and code == kluiscode:
            gegevenscorrect = True
    if gegevenscorrect:
        print('correct')
    else:
       print('Deze code is onjuist')


print('1: ik wil weten hoeveel kuizen er vrij zijn\n'
      '2: Ik wil een nieuwe kluis\n'
      '3: Ik wil even iets uit mijn kluis halen\n')

kluis_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
keuze = eval(input('Wat is u keuze: '))

if keuze == 1:
    toon_aantal_kluizen_vrij()

elif keuze == 2:
    nieuwe_kluis()

elif keuze == 3:
    kluis_openen()




