chaine=raw_input("saisissez une chaine de caractere :")
voyelle=["a","e","i","o","u","y","A","E","I","O","U","Y"]
def carac(liste):
    fin=[]
    for x in liste:
        if x in voyelle:
            fin.append(x)
    return len(fin)

print carac(chaine)
