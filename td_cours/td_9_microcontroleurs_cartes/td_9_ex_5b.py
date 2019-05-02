# pour aller plus loin facile
import board
import time
import pulseio
from adafruit_motor import servo

MLI = pulseio.PWMOut(board.D4, frequency=50)
mon_servo = servo.Servo(MLI, min_pulse=900, max_pulse=2300, actuation_range=140)
# a vous de vous debrouiller
angle = 10

while True:
    if angle < 140:
        print(angle)
        mon_servo.angle = angle
        angle = angle + 10
        time.sleep(0.5)
        
    else:
        while angle >= 10:
            angle = angle - 10
            mon_servo.angle = angle
            print(angle)
            time.sleep(0.5)
    # penser aux boucles!
  
   