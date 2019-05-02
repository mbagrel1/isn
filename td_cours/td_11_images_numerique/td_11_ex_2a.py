entree = raw_input("saisissez le nom de l'image et l extension: ")
fichier = open(entree, "r")
fichier2 = open("sortie.pgm", "w")

fichier2.write(fichier.read())

fichier.close()
fichier2.close()