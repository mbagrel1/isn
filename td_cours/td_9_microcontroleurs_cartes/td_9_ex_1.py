# premier test:clignotement delrouge
import time
import board
from digitalio import DigitalInOut, Direction

delrouge = DigitalInOut(board.D2)
delrouge.direction = Direction.OUTPUT

pause = 0.5
while True:
    delrouge.value = False
    time.sleep(0.5)
    delrouge.value = True
    time.sleep(pause)
    if pause >= 0.2:
        pause = pause - 0.1
    else:
        pause = 0.5
    
 
    
    # completer le programme
    # pour mettre une pause de 100 ms par exemple utiliser l'instruction
    # time.sleep(0.1)
    # la valeur de l'argument est en secondes