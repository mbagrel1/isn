
def nombreDeE(chaine):
    lettre="e"
    LETTRE="E"
    compteur=0
    for x in chaine:
        if x==lettre or x==LETTRE:
            compteur=compteur+1
    return compteur

mot=raw_input("Saisissez une chaine de caractere : ")

print"La lettre e est presente", nombreDeE(mot), "fois dans la chaine"


