zin = input('vul hier een zin in: ')
woorden = zin.split()
aantal_letters = 0
aantal_woorden= 0
for woord in woorden:
    aantal_letters = aantal_letters + len(woord)
aantal_woorden = len(woorden)

gemiddelde = aantal_letters/aantal_woorden

print(gemiddelde)

