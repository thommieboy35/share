
def Kwadraten_som(lst):
    som = 0
    for getal in lst:
        if getal >=0:
            som = som + getal**2
    return (som)

lst2 = [4, 5, 3, -81]

resultaat = (Kwadraten_som(lst2))

print(resultaat)

