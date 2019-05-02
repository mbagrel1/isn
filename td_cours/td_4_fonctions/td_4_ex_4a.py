def ADN(chaine):
    compteur=0
    for x in chaine:
        if x=="A":
            compteur=compteur+1
    return compteur

mot=raw_input("saisissez une sequence d'ADN:")
print ADN(mot)
