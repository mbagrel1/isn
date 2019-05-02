
# deuxieme test:Dels et poussoir
import time
import board
from digitalio import DigitalInOut, Direction, Pull

delrouge = DigitalInOut(board.D2)
delverte = DigitalInOut(board.D3)
delrouge.direction = Direction.OUTPUT
delverte.direction = Direction.OUTPUT
poussoir = DigitalInOut(board.D0)
poussoir.direction = Direction.INPUT
poussoir.pull = Pull.DOWN  

while True:
    delrouge.value = True
    time.sleep(0.5)
    delrouge.value = False
    time.sleep(0.5) 
    if poussoir.value is True:
        for i in range(10):
            delverte.value = True
            time.sleep(0.1)
            delverte.value = False
            time.sleep(0.1) 
        print("poussoir appuye")

        
    
