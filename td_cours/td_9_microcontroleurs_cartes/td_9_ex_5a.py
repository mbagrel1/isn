# pour aller plus loin facile
import board
import time
import pulseio
from adafruit_motor import servo
MLI = pulseio.PWMOut(board.D4, frequency=50)
servo_continu = servo.ContinuousServo(MLI, min_pulse=1000, max_pulse=2100)
# a vous de vous debrouiller
vite = 0.5

while True:
    if vite >= -0.5:
        print(vite)
        servo_continu.throttle = vite
        vite = vite - 0.1
        time.sleep(0.5)
        
    else:
        while vite <= 0.5:
            vite = vite + 0.1
            servo_continu.throttle = vite
            print(vite)
            time.sleep(0.5)
    # penser aux boucles!
  
   