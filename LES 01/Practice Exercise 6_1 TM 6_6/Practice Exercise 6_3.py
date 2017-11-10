invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
strgetallen = invoer.split('-')
getallenrij = []

for strgetal in strgetallen:
    getal = int(strgetal)
    getallenrij.append(getal)
    getal1= sorted(getallenrij)
    getal2= max(getallenrij)
    getal3= min(getallenrij)
    getal4= len(getallenrij)
    getal5 = sum(getallenrij)
    getal6 = sum(getallenrij)/ len(getallenrij)

print('gesorteede list van ints: {}'.format(getal1))
print('grootste getal: {} en Kleinste getal: {}'.format(getal2, getal3))
print('aantal getallen: {} en som van de getallen: {} '.format(getal4, getal5))
print('Gemiddelde: {}'.format(getal6))