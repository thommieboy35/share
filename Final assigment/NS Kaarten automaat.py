def inlezen_beginstation(stations):
    beginstation = input('welk station vertrekt u: ')
    while beginstation not in stations:
        beginstation = input('Geef een nieuw station: ')
    return beginstation

def inlezen_eindstation(stations, beginstation):
    eindstation = input('waar wilt u naar toe: ')
    while eindstation not in stations:
        eindstation = input('Geef een ander station: ')
    while stations.index(eindstation) <= stations.index(beginstation):
        eindstation = input('het station klopt niet geef nieuw station: ')
    return eindstation

def omroepen_reis(stations, beginstation, eindstation):
    nummerB = stations.index(beginstation)+1
    nummerE = stations.index(eindstation)+1
    print('Het beginstation {} is het {}e station in het tracject'.format(beginstation, nummerB))
    print('Het eindstation {} is het {}e station in het traject'.format(eindstation, nummerE))
    afstand = nummerE - nummerB
    print('De afstand bedraagt {} station(s)'.format(afstand))
    prijs = afstand * 5
    print('De prijs van het kaartje is {} euro'.format(prijs))
    print('Jij stapt in de trein in: {}'.format(beginstation))
    for i in range(nummerB, nummerE-1):
        print('-'+stations[i])
    print('je eind station is {}'.format(eindstation))

stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam-sloterdijk', 'Amsterdam-Centraal', 'Amsterdam-Amstel', 'Utrecht-Centraal', 's-Hertogenbosch', 'Eindhoven', 'Weerd', 'Roermond', 'Sittard', 'Maastricht']

beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)
