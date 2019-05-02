# reception de donnees envoyees depuis la carte 
# il faut installer la librairie pyserial
from serial import *
import time

#creation du port com
ser=Serial(port="COM4", baudrate=9600, timeout=1)

#---explication-------------------
#~ si le port de communication est ouvert, on lit les donnees envoyees sous forme d'une seule ligne
#~ l'instruction ser.readline() permet de lire le message envoye jusqu'a ce qu'elle detecte un caractere de fin de phrase
#~ si vous envoyez depuis la carte avec l'instruction print() le caractere de fin de phrase est automatiquement envoye
#~ si vous envoez depuis la carte via une liaison uart avec l'instruction uart.write() il faudra ajouter le caractere de fin de phrase avant d'envoyer vos donnees
#~ on stocke la chaine de caracteres lus dans "messageinitial"
#~ il est preferable de lire plus vite que la vitesse d'envoi pour eviter les lectures a retardement

if ser.isOpen():  
	while True:
		messageinitial = ser.readline()
		print "le message initial recu est: ",messageinitial
		print"---------------------------"
		time.sleep(0.04)





