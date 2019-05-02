# fonction qui calcule la moyenne
def moyenne(liste_notes):
	somme = 0
	for x in liste_notes:
		somme = somme + x
	moyenne = somme / len(liste_notes)
	return moyenne

# fonction qui renvoie une appreciation associee a la moyenne
def appreciation(moyenne_notes):
	if moyenne_notes >= 16:
		message_final = "Tres bien"
	elif moyenne_notes >=13 :
		message_final = "Bien"
	elif moyenne_notes >= 9 :
		message_final = "ABien"
	else:
		message_final = "On risque de se revoir l'annee prochaine ! "
	return message_final

# programme principal
liste_de_notes = []
note = input("veuillez saisir une note : ")
while note >= 0:
	liste_de_notes.append(note)
	note = input("veuillez saisir une note : ")


moyenne_de_notes = moyenne(liste_de_notes)
print appreciation(moyenne_de_notes)
	
		
