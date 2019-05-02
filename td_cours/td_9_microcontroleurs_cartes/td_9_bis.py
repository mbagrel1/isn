# pour aller plus loin: difficile
import board
import time
from math import log
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
delrouge = DigitalInOut(board.D2)
delverte = DigitalInOut(board.D3)
delrouge.direction = Direction.OUTPUT
delverte.direction = Direction.OUTPUT

thermo = AnalogIn(board.A0)

while True: 
    uctn = thermo.value
    rctn = (uctn * 4700) / (3.3 - uctn)
    kelvin = 1 / ((1/3977) * log((rctn / 10000)) + (1 / 298))
    degre = kelvin - 273.15
    if degre < 21:
        delrouge.value = False
        delverte.value = False
        delverte.value = True
    elif degre < 22.5:
        delverte.value = False
        delrouge.value = False
        delrouge.value = True
        time.sleep(0.5) 
    else:
        delrouge.value = False
        delrouge.value = True 
   