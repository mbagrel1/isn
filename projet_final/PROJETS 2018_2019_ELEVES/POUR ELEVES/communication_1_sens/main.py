# envoi d'une tension via le port serie
import time
import board
from analogio import AnalogIn
U0 = AnalogIn(board.A0)
# sur carte trinket M0 A0 sur patte 1

while True:
    Upotar = U0.value*3.3/65535
    print(Upotar,Upotar)
    # print("coucou")
    time.sleep(0.05)
    
