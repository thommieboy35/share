import random

def Monopolyworp(Worp1_dobbelsteen1, Worp1_dobbelsteen2, Worp2_dobbelsteen1, Worp2_dobbelsteen2, Worp3_dobbelsteen1, Worp3_dobbelsteen2):
    Totaal1 = Worp1_dobbelsteen1 + Worp1_dobbelsteen2
    Totaal2 = Worp2_dobbelsteen1 + Worp2_dobbelsteen2
    Totaal3 = Worp3_dobbelsteen1 + Worp3_dobbelsteen2
    print(Worp1_dobbelsteen1, Worp1_dobbelsteen2, 'Totaal:', Totaal1)
    if Worp1_dobbelsteen1 == Worp1_dobbelsteen2:
        print(Worp1_dobbelsteen2, Worp2_dobbelsteen2, 'Totaal:', Totaal2)
        if Worp2_dobbelsteen1 == Worp2_dobbelsteen2:
            print(Worp3_dobbelsteen1, Worp3_dobbelsteen2, 'Totaal:', Totaal3)
            print('Je gaat naar de gevangenis')






Worp1_dobbelsteen1= random.randrange (1, 2)
Worp1_dobbelsteen2= random.randrange (1, 2)
Worp2_dobbelsteen1= random.randrange (1, 2)
Worp2_dobbelsteen2= random.randrange (1, 2)
Worp3_dobbelsteen1= random.randrange (1, 2)
Worp3_dobbelsteen2= random.randrange (1, 2)

Monopolyworp(Worp1_dobbelsteen1, Worp1_dobbelsteen2, Worp2_dobbelsteen1, Worp2_dobbelsteen2, Worp3_dobbelsteen1, Worp3_dobbelsteen2)


