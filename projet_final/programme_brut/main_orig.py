import board
import time
import random

from analogio import AnalogIn
from digitalio import DigitalInOut, Direction, Pull

# connection des dels numériques
delliste = []
# liste des pattes de la carte
liste_conn = [[board.D2, board.D3, board.D4], [board.D5, board.D6, board.D7],
[board.D8, board.D9, board.D10], [board.D11, board.D12, board.D13]]

for triplet in liste_conn:
    rvb = []
    for patte in triplet:
        del1 = DigitalInOut(patte)
        del1.direction = Direction.OUTPUT
        rvb.append(del1)
    delliste.append(rvb)

# connection de boutons
b1 = AnalogIn(board.A2)
b2 = AnalogIn(board.A3)
b3 = AnalogIn(board.A4)
b4 = AnalogIn(board.A5)



# Fonction qui sort un triplet au hasard
def triplet_alea():
    liste_couleur = [[True, False, False], [False, True, False], [False, False, True],
    [True, True, False], [False, True, True], [True, False, True], [True, True, True]]
    argument_couleur = random.randint(0, 6)
    return liste_couleur[argument_couleur]

# melange position del au hasard
liste_position_del = []
liste_position_del_mel = []
def melange_position_del(niveau):
    for i in range(niveau):
        liste_position_del.append(i)
    for pos in range(1, (niveau + 1)):
        nombre_alea = random.randint(0, (niveau - pos))
        liste_position_del_mel.append(liste_position_del[nombre_alea])
        liste_position_del.remove(liste_position_del[nombre_alea])
    return liste_position_del_mel


# niveau 1 test

liste_couleur = []
for i in range(4):
    couleur = triplet_alea()
    liste_couleur.append(couleur)


allumer = True


while True:
    # allume une fois la sequence aleatoire
    if allumer:
        liste_del_mel = melange_position_del(4)
        for x in liste_del_mel:
            time.sleep(1)
            for j in range(3):
                delliste[x][j].value = liste_couleur[x][j]
            time.sleep(0.5)
            for j in range(3):
                delliste[x][j].value = False
        allumer = False
