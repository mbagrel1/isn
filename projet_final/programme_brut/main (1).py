import board
import time
import random

from digitalio import DigitalInOut, Direction

led_connections = [board.D8, board.D9, board.D10, board.D11]

leds = []

for pin in led_connections:
    led = DigitalInOut(pin)
    led.direction = Direction.OUTPUT
    leds.append(led)

bouton_connections = [board.D2, board.D3, board.D4, board.D5]

boutons = []

for pin in bouton_connections:
    bouton = DigitalInOut(pin)
    bouton.direction = Direction.INPUT
    boutons.append(bouton)







def alea_led(derniere_pos):
    liste_alea_tirage = [[1, 2, 3], [0, 2, 3], [0, 1, 3], [0, 1, 2]]
    led_choisie = random.choice(liste_alea_tirage[derniere_pos])
    return led_choisie



def alea_sequence(nombre_led_a_allumer):
    leds_a_allumer = []
    derniere_pos = random.randint(0, 3)
    leds_a_allumer.append(derniere_pos)
    for led in range((nombre_led_a_allumer - 1)):
        derniere_pos = alea_led(derniere_pos)
        leds_a_allumer.append(derniere_pos)
    return leds_a_allumer

def bouton_appuye(numero_bouton):
    return boutons[numero_bouton].value

def etat_boutons():
    resultat_etat = []
    for numero_bouton in range(4):
        resultat_etat.append(bouton_appuye(numero_bouton))
    return resultat_etat

def clignoter_led(numero_led):
    leds[numero_led].value = True
    time.sleep(0.5)
    leds[numero_led].value = False

def doit_on_attendre(derniere_pos=None):
    tout_eteint = [False, False, False, False]
    if derniere_pos is not None:
        juste_derniere_pos_allumee = [False, False, False, False]
        juste_derniere_pos_allumee[derniere_pos] = True

    resultat_etat = etat_boutons()
    print(resultat_etat)
    if resultat_etat == tout_eteint:
        return True
    elif derniere_pos is not None and resultat_etat == juste_derniere_pos_allumee:
        return True
    else:
        return False


def bouton_correct(nouvelle_pos, derniere_pos=None):
    while doit_on_attendre(derniere_pos):
        time.sleep(0.1)
    juste_nouvelle_pos_allumee = [False, False, False, False]
    juste_nouvelle_pos_allumee[nouvelle_pos] = True
    return (etat_boutons() == juste_nouvelle_pos_allumee)

# programme principale

n = 4


sequence = alea_sequence(n)
for pos in sequence:
    clignoter_led(pos)
derniere_pos = None
for pos in sequence:
    if not bouton_correct(pos, derniere_pos):
        print("Vous avez perdu !")
        break

    derniere_pos = pos
else:
    print("Vous avez gagne !")

