argent = 1
taux=input("Quel taux de change voulez vous ?")
while argent<=500:
    resultat=taux*argent
    print argent, "$", "=",resultat,"euros"
    argent= argent*2.0
