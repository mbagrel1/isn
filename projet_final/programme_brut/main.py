import board
import time
import random
from analogio import AnalogIn
from digitalio import DigitalInOut, Direction, Pull

# Fonction qui sort un triplet au hasard
def triplet_alea():
    liste_couleur = [[True, False, False], [False, True, False], [False, False, True],
    [True, True, False], [False, True, True], [True, False, True], [True, True, True]]
    argument_couleur = random.randint(0, 6)
    return liste_couleur[argument_couleur]


# connection de del1
delliste = []
liste_conn = [[board.D2, board.D3, board.D4], [board.D5, board.D6, board.D7],
[board.D8, board.D9, board.D10], [board.D11, board.D12, board.D1]]

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

# niveau 1
liste= []
for i in range(3):
    couleur = triplet_alea()
    liste.append(couleur)
    
while True:
    for k in range(3):
        for j in range(3):
            delliste[k][j].value = liste[k][j]
    
    time.sleep(0.5)
    
    delliste[0][0].value = False
    delliste[0][1].value = False 
    delliste[0][2].value = False
    
    delliste[1][0].value = False
    delliste[1][1].value = False 
    delliste[1][2].value = False
    
    delliste[2][0].value = False
    delliste[2][1].value = False 
    delliste[2][2].value = False
    
    time.sleep(0.6)
   