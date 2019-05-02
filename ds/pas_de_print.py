# fonction qui indique en fonction de votre categorie
# si vous etes plus petit ou plus grand que la moyenne

def grand_ou_petit(categorie,taille):
	if categorie == "H" or categorie == "h":
		taille_moy = 1.76
	elif categorie == "F" or categorie == "f":
		taille_moy = 1.62
	else:
		message = "  erreur de saisie"
		return message

	if taille>=taille_moy:
		message = "  vous etes plus grand que la moyenne"
	else:
		message = "  vous etes plus petit que la moyenne"
	return message

#---------------prog principal------------- 
t=input(" entrer votre taille en metres = ")
cat=raw_input(" entrer votre categorie Homme ou Femme H / F : ")

print grand_ou_petit(cat,t)

