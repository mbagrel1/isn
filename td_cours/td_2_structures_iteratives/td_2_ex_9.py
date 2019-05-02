from random import randint
p=2000
compteur=0
prix=randint(0,1000)
while p!= prix:
    p=input("Entrer votre proposition: ")
    if p > prix:
        print"Le nombre est trop grand"
        compteur=compteur+1
    elif p< prix:
        print"Le nombre est trop petit"
        compteur=compteur+1
    else:
        print"Bravo, vous avez trouve en", compteur, "coups"


