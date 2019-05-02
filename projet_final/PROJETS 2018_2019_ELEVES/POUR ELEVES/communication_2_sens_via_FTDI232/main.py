# communication 2 sens via FTID232
import time
import board
import busio
from analogio import AnalogIn
uart = busio.UART(board.TX, board.RX, baudrate=9600)
N = AnalogIn(board.A0)

while True:
    time.sleep(0.05)
    U = N.value*3.3/65535
    
    data = uart.read(1)
    if data is not None:  
            print(data)  
            donnees_recues = chr(data[0])
            print(donnees_recues)
            
            if donnees_recues == "2":
                donnees_envoi = str(U)+"\r\n"
                uart.write(donnees_envoi)
    
    
    