s = 'guido van Rossum heeft programmeertaal'

klinker = ('aeiou')
for zin in s:
    for k in klinker:
        if k == zin:
            print(zin)