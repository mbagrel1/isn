def tri_binaire(liste):
    Pair = False
    if liste[7] != 1:
        Pair = True
    return Pair


def conv_deci(liste):
    resultat = 0
    puissance = 7
    for x in liste:
        resultat = resultat + x * 2 ** puissance
        puissance = puissance - 1
    return resultat


liste_octet = []
for i in range(8):
    bit = input("saisissez un bit : ")
    liste_octet.append(bit)

if tri_binaire(liste_octet):
    print "le nombre est pair"
else:
    print "le nombre est impair"
print conv_deci(liste_octet)
