def ADN(chaine):
    poids_moleculaire=0
    for x in chaine:
        if x=="A" or x=="T":
            poids_moleculaire=poids_moleculaire + 260
        else:
            poids_moleculaire=poids_moleculaire + 245
    return poids_moleculaire

mot=raw_input("saisissez une sequence d'ADN :")
print ADN(mot)
