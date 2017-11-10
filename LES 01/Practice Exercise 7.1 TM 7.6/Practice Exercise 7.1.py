som = 0
aantal = 0
while True:
    getal= eval(input('geef getal:'))
    if getal == 0:
        break
    else:
        som = som + getal
        aantal += 1

print(som)
print(aantal)