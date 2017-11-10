while True:
    woord = input('geef een woord in: ')
    if len(woord) == 4:
        print('in lezen van correctestring: {} is geslaagd'.format(woord))
        break
    else: print('{} heeft {} letters'.format(woord, len(woord)))