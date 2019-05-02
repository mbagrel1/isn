# quatrieme servo continu
import board
import time
import pulseio
from adafruit_motor import servo

MLI = pulseio.PWMOut(board.D4, frequency=50)
servocontinu = servo.ContinuousServo(MLI, min_pulse=1000, max_pulse=2100)

while True:
    servocontinu.throttle = 1
    time.sleep(1)
    servocontinu.throttle = -1
    time.sleep(1)
   
    # completer votre programme en vous aidant du powerpoint