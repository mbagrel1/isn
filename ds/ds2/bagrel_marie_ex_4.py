from random import randint
# definition de la fonction qui genere la liste de facon aleatoire
def gene_liste():
	liste_position = []
	position_alea = randint(0,9)
	for i in range(10):
		if i == position_alea:
			liste_position.append(8)
		else:
			liste_position.append(0)
	return liste_position
	
	
# programme principal : on suppose que l'utilisateur ne donc des coordonees qu'entre 0 et 9

liste_coordonnee = gene_liste()
liste_essai = ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
print liste_coordonnee
essai_tir = input("saisissez la coordonee pour tenter de couler le bateau : ")
while liste_coordonnee[essai_tir] != 8:
	print"tir rate"
	liste_essai[essai_tir] = "X"
	print liste_essai
	essai_tir = input("saisissez la coordonee pour tenter de couler le bateau : ")
	
print"Felicitations, bateau coule !"

		
	
