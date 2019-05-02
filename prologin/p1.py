prix_joseph = int(input())
nb_billet = int(input())
prix_billet_texte = input()

liste_prix = []
arnaque = 0
liste = prix_billet_texte.split(" ")
for x in liste:
    liste_prix.append(int(x))
est_arnaque = False
for x in liste_prix:
    if x < prix_joseph:
        arnaque = arnaque + 1
if arnaque >= 3.0:
    est_arnaque = True
if est_arnaque:
    print("ARNAQUE !")
else:
    print("Ok bon voyage, bisous, n'oublie pas de m'envoyer des photos !")
