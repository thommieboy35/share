def standaardprijs(afstandkm):
    if afstandkm >50:
        res = 0.60 * afstandkm + 15
    else: res = afstandkm * 0.80
    if afstandkm <0:
        res = 0
    return res

def ritprijs (leeftijd, weekendrit, afstandkm):

    Dag = weekendrit
    #PRIJS VOOR WEEKEND RIT ZATERDAG!!!!!
    if Dag == 'zaterdag':
        if leeftijd <12:
            prijs =afstandkm/100*65
            return prijs
        if leeftijd >65:
            prijs = afstandkm/100*65
            return prijs
        if leeftijd <=65 >=12:
            prijs = afstandkm/100*60
            return prijs
    #PRIJS VOOR WEEKEND RIT ZONDAG!!!!
    if Dag == 'zondag':
        if leeftijd <12:
            prijs = afstandkm/100*65
            return prijs
        if leeftijd >65:
            prijs = afstandkm/100*65
            return prijs
        if leeftijd <=65 >=12:
            prijs = afstandkm/100*60
            return  prijs
    #PRIJZEN VOOR DOORDEWEEKS
    else:
        if leeftijd <12:
            prijs = afstandkm/100*70
            return  prijs
        if leeftijd >65:
            prijs = afstandkm/100*70
            return prijs
        if leeftijd >=12 <=65:
            prijs = afstandkm
            return prijs

km = eval(input('hoeveel km gaat u reizen:'))

KM = standaardprijs(km)


age1 = eval(input('Wat is de leeftijd van de persoon die gaat reizen? '))

vandaag = input('Op welke dag gaat u reizen? ')

Weekend = ritprijs(age1, vandaag, KM)

print(Weekend)

#negative afstand
#ritprijs(-10, zondag 10) = 0       Negativegetal, Weekend, <12
#ritprijs(-10, zondag 30) = 0       Negativegetal, Weekend, >=12 <=65
#ritprijs(-10, zondag 70) = 0       Negativegetal, Weekend, >65
#ritprijs(-10, week 10) = 0       Negativegetal, Weekend, <12
#ritprijs(-10, week 30) = 0       Negativegetal, Weekend, >=12 <=65
#ritprijs(-10, week 70) = 0       Negativegetal, Weekend, >65

#korte afstand
#ritprijs(10, zondag 10) = 5.20         korteafstand, weekend, <12
#ritprijs(10, zondag 30) = 4.80         korteafstand, weekend, >=12 <=65
#ritprijs(10, zondag 70) = 5.20         korteafstand, weekend, >65
#ritprijs(10, week 10) = 5.60        korteafstand, week, <12
#ritprijs(10, week 30) = 8.00        korteafstand, week, >12 <65
#ritprijs(10, week 70) = 5.60        korteafstand, week, >65

#lange afstand
#ritprijs(100, zondag 10) = 48.75         korteafstand, weekend, <12
#ritprijs(100, zondag 30) = 45.00         korteafstand, weekend, >=12 <=65
#ritprijs(100, zondag 70) = 48.75         korteafstand, weekend, >65
#ritprijs(100, week 10) = 52.50       korteafstand, week, <12
#ritprijs(100, week 30) = 75.00       korteafstand, week, >=12 <=65
#ritprijs(100, week 70) = 52.50         korteafstand, week, >65