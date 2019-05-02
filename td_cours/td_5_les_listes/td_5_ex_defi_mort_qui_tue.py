def tri_insertion(nb_entrant, liste_rangee):
    """permet de placer le nombre entrant dans la liste en conservant le tri"""
    i = 0
    while i < len(liste_rangee) and nb_entrant > liste_rangee[i]:
        i = i + 1
    liste_rangee.insert(i, nb_entrant)

# Programme principal
liste_ordonnee = []
nb_de_nombres = input("saisissez le nombre d'entiers a comparer : ")
for i in range(nb_de_nombres):
    nb_a_trier = input("saisissez un nombre entier : ")
    tri_insertion(nb_a_trier, liste_ordonnee)
print liste_ordonnee