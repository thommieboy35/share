studentencijfers = [[95, 92, 86], [66, 75, 54], [89, 72, 100], [34, 0 ,0 ]]
gemiddeld=[]


def gemiddelde_per_student(cijfers):
    som = sum(cijfers)
    lengte = len(cijfers)
    gemiddelde = som/lengte
    return gemiddelde

def gemiddeld_van_alle_studenten(cijfer):
    cijfer = studentencijfers[0] + studentencijfers[1] +studentencijfers[2] + studentencijfers[3]
    som = sum(cijfer)
    antwoord = som/len(cijfer)
    return antwoord


student0 = gemiddelde_per_student(studentencijfers[0])
student1 = gemiddelde_per_student(studentencijfers[1])
student2 = gemiddelde_per_student(studentencijfers[2])
student3 = gemiddelde_per_student(studentencijfers[3])
gemiddelde = gemiddeld_van_alle_studenten(gemiddeld)
print(int(student0))
print(int(student1))
print(int(student2))
print(int(student3))
print(int(gemiddelde))