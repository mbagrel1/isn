# programme permettant de trouver le port COM connecte

#importation de la librairie pyserial
from serial import *

#---------------------trouve les ports COM--------------------
import serial.tools.list_ports as stls
comlist = stls.comports()   # recuperation des ports COM sous forme de liste avec code hexa
print comlist

# creation d'une liste permettant d'obtenir la liste des ports COM en decimal
connected = []
for element in comlist:
    connected.append(element.device)
print("Connected COM ports: " + str(connected))   #on liste les ports COM detectes

print connected
if connected==[]:
	print "pas de port detecte"
else:
	for element in connected:    # si le port COM detecte n'est pas le port COM1 on valide
		if element!='COM1':
			PORT_OK=element
			print "le port connecte est : ",PORT_OK
			break

#--------------------------------------------------------------------------
#-------------info sur site :https://pyserial.readthedocs.io/en/latest/tools.html
