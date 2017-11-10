groen = {'Boxtel', 'Best', 'Beukenlaan', 'Eindhoven', 'Geldorp', 'Heeze', 'Weert'}
bruin = {'Boxt', 'Best', 'Beukenlaan', 'Eindhoven', 'Helmond t Hout', 'Helmond Brouwhuis', 'Deurne'}

print(groen.intersection(bruin))
print(bruin.difference(groen))
print(groen | bruin)