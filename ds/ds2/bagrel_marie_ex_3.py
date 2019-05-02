# definition de la fonction qui compte le nombre de mots en reperant les espaces
def reperespace(phrase_a_tester):
	compteur = 0
	for i in range((len(phrase_a_tester)- 1)):
		if phrase_a_tester[i] == " " and phrase_a_tester[i+1] != " " and phrase[i-1]!= " ":
			compteur = compteur+1
	if compteur != 0:
		nombre_mot = compteur + 1
	return nombre_mot

# programme principal

phrase = raw_input("saisissez une phrase dont vous souhaitez connaitre le nombre de mots : ")
print reperespace(phrase)			
