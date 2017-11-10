def seizoen(maand):
    if maand >=3 and maand <=5:
        res = 'lente'
        return res
    elif maand >=6 and maand <=8:
        res = 'zomer'
        return res
    elif maand >=9 and maand <=11:
        res = 'herfst'
        return res
    elif maand == 12 or maand >=1 and maand <=2:
        res = 'winter'
        return res


maand = eval(input('welke maand is het?:'))

print(seizoen(maand))