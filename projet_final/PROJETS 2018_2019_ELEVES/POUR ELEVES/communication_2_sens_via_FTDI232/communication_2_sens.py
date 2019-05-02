# connexion via USB serial FTID232
#dans gestionnaire de peripherique trouver le numero du port COM
from serial import *
import time
ser=Serial(port="COM13", baudrate=9600, timeout=1)

if ser.isOpen():
	while True:
		ser.write("2")    
		time.sleep(0.5)
		messageinitial = ser.readline()
		print messageinitial

