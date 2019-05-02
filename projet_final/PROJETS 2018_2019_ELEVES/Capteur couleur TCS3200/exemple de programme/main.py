#----G.Rougeaux 21 mars 2019------
import time
import board
import digitalio
from pulseio import PulseIn
from analogio import AnalogIn
pulses = PulseIn(board.D3, maxlen=2) # correspond a la patte OUT
lecture = AnalogIn(board.A0)
# -------------pilotage de la lumiere ----------------
led = digitalio.DigitalInOut(board.D2)
led.direction = digitalio.Direction.OUTPUT
led.value = False
# -----------config de la frequence -------------
# laisser la frequence la plus basse soit (S0,S1)=(0,1)
S0 = digitalio.DigitalInOut(board.D8)
S0.direction = digitalio.Direction.OUTPUT
S1 = digitalio.DigitalInOut(board.D9)
S1.direction = digitalio.Direction.OUTPUT
S0.value = False  # frequence 2%
S1.value = True
# 2% 0 1 - 20% 1 0 - 100 % 1 1 -coupure 0 0
# 1.3 kHz - 13 kHz  - 70 kHz 
# ------------config des filtres -----------------
S2 = digitalio.DigitalInOut(board.D10)
S2.direction = digitalio.Direction.OUTPUT
S3 = digitalio.DigitalInOut(board.D11)
S3.direction = digitalio.Direction.OUTPUT
S2.value = False  # red
S3.value = False
# red 0 0  - bleu 0 1 - green 1 1 - sans filtres 1 0
# --------------parametre du temps--------------
# attente avant de lancer la mesure
time.sleep(2)  

while True:
    led.value = True
    time.sleep(0.5)
    print("nombre de pulses:", len(pulses))
    print("premier pulse:", pulses[0], "deuxieme pulse:", pulses[1])
