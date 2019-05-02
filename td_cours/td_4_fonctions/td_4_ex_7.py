def factorielle(entier):
    resultat=1
    for i in range(1,(entier+1),1):
        resultat=resultat*i
    return resultat

nombre=input("Saisissez l'entier que vous voulez :")
print "le resultat est", factorielle(nombre)

