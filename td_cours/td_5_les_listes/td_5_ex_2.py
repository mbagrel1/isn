from random import randint
valeur=["As","2","3","4","5","6","7","8","9", "10", "Valet", "Dame", "Roi"]
couleur=["coeur", "carreau", "pique", "trefle"]
cartes=[""]
for c in couleur:
    for v in valeur:
        cartes.append(v +" de "+ c)

nombre=randint(0,(len(cartes)-1))

print cartes[nombre]
