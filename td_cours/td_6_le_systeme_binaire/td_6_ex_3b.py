#definition de fonction

def binaire_paire(liste):
    resultat = 0
    for x in liste:
        puissance = 7
        resultat = resultat + x * (2) ^ puissance
        puissance = puissance - 1
        return resultat
#programme principal
liste_octet = []
for i in range(8):
    bit = input("saisissez un bit : ")
    liste_octet.append(bit)
somme = binaire_paire(liste_octet)
if somme % 2 == 0:
    print "le nombre est pair"
else:
    print "le nombre est impair"

