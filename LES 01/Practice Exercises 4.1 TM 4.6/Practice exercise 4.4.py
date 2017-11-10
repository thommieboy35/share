
def new_password(oldpassword, newpassword):

    if oldpassword != newpassword and len(newpassword) >= 6:
        for c in newpassword:
            if c in '0123456789':
                return True
        return False
    else:
        return False

#corrcte wachtwoorden --> true
res = new_password('vakProg17', 'Python17')
print(res)

# Hetzelfde wachtwoord --> False
print(new_password('huProg17', 'huProg17'))

#Te kort nieuw wachtwoord -->
print(new_password('vakProg17', 'Pro17'))

#Nieuw wachtwoord zonder cijfer --> Fals
print(new_password('vakProg17','huVakPro'))