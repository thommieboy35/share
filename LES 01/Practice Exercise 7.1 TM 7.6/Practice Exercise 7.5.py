dict = {}
def namen():
    while True:
        Naam = input('Wat is je naam:')
        print('Volgende naam: {}'.format(Naam))
        if Naam == '':
            break
        elif Naam in dict.keys():
            dict[Naam]+=1
        else: dict[Naam]=1


namen()

for woord in dict.values():
    for woord1 in dict.keys():
        if woord >2:
            print('Er is {} student met de naam {}'.format(woord, woord1 ))
        else: print('Er zijn {} studenten met de naam {}'.format(woord, woord1 ))

print(dict)