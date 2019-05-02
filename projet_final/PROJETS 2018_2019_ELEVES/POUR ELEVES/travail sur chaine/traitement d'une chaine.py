#cet exemple montre comment envoyer plusieurs valeurs en utilisant une seule chaine
#on souhaite envoyer 2 valeurs de tensions
Uphoto = 2586*3.3/65535
Upotar = 1532*3.3/65535
print(Uphoto, Upotar)
# tout transformer en une seule chaine avant envoi. mettre des caracteres deparateurs ";" ou tabulation "\t" ou ","
donnes_envoie = str(Upotar) + ";" + str(Uphoto) + "\r\n"

#-----------on suppose l'envoie du message en utilisant liaison.write(donnes_envoie)--------

# ----------on suppose la reception en utilisant liaison.readline()--------------------------

# on suppose le message recu et stocke dans la variable messagerecu, on l'affiche au niveau de la reception
messagerecu=donnes_envoie
print messagerecu

#on separe les differents elements en utilisant la methode split
liste=messagerecu.split(";")

# en affichant on constate que l'on a bien les elements separes dans une liste, mais 
# il reste les caracteres de fin de phrase \r\n
print liste

# on peut avant d'utiliser la methode split(), eliminer les caracteres de fin de phrase avec 
#la methode rstrip()
print "----------suppression de \\r\\n---------------"
newmessage=messagerecu.rstrip('\r\n')
liste2=newmessage.split(";")
print liste2

# on peut maintenant recuperer les differents elements de la liste
# exemple on peut recupere la tension Uphoto et Upotar
Upotar=liste2[0]
Uphoto=liste2[1]
print "Uphoto=", Uphoto
print "Upotar=", Upotar

# n'oubliez de convertir en nombre Uphoto et Upotar qui sont en fait du texte..!
