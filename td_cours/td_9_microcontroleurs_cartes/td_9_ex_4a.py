# Quatrieme test NanoS ou Tiny S(servo moteur a angle)
import board
import time
import pulseio
from adafruit_motor import servo

MLI = pulseio.PWMOut(board.D4, frequency=50)
mon_servo = servo.Servo(MLI, min_pulse=900, max_pulse=2300, actuation_range=140)

while True:
    mon_servo.angle = 30
    time.sleep(1)
    mon_servo.angle = 90
    time.sleep(1) 
    # completer en vous aidant du Powerpoint
  
  
   