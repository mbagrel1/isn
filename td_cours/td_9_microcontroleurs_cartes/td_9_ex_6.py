# pour aller plus loin: difficile
import board
import time
import pulseio
from adafruit_motor import servo
from analogio import AnalogIn
MLI = pulseio.PWMOut(board.D4, frequency=50)
servo_continu = servo.ContinuousServo(MLI, min_pulse=1000, max_pulse=2100)
photodiode = AnalogIn(board.A0)

Umax = 0.8
Umin = 0.5
vitmax = 0.5
vitmin = -0.5
a = (vitmax-vitmin)/(Umax-Umin)
b = vitmax - (a * Umax)

while True:
    tension = photodiode.value * 3.3 / 65535
    time.sleep(0.2)
    vite = a * tension + b
    print("vit",vite)
    print(tension)
    if vite >= 0.5:
        vite = 0.5
    elif vite <= -0.5:
        vite = -0.5
    servo_continu.throttle = vite

   