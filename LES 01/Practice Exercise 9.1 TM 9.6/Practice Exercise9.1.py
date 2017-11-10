try:
    index = int(input('Geef een index:'))
    print(4356/index)
except ValueError:
    print('Je moet een geheel getal invoeren')
except ZeroDivisionError:
    print('De list bevat een 0')
except TypeError:
    print('De list bevat een niet numeriek element')
except IndexError:
    print('je moet een getal tussend -5 en 4 invoeren')
