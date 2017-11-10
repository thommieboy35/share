def lang_genoeg(lengte):
    if lengte >120:
        return ('gefeliciteerd')
    else:
        return ('je bent te klein sukkel')

getal = eval(input('hoe lang ben je? '))

res = lang_genoeg(getal)

print(res)