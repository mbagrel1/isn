# troisieme test: potentiometre et DELs
import time
import board
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
delrouge = DigitalInOut(board.D2)
delverte = DigitalInOut(board.D3)
delrouge.direction = Direction.OUTPUT
delverte.direction = Direction.OUTPUT
potentiometre = AnalogIn(board.A0)

while True:
    tension = potentiometre.value * 3.3 / 65535
    print((tension, ))
    time.sleep(0.5)
    if tension > 1.5:
        delverte.value = False
        delrouge.value = False
        delrouge.value = True
        print("DEL rouge allumee")
    else:
        delrouge.value = False
        delverte.value = False
        delverte.value = True
        print("DEL verte allumee")

   
    # compléter votre programme
    # pensez a convertir la valuer lue en tension