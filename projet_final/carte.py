import board
import time
import random
import busio

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

ENC = "utf-8"
DEPART = "d"
GAGNE = "g"
PERDU = "p"
FIN = "f"
TEMPS_AVANT_PARTIE = 2
SINGLEPLAYER = "1"
MULTIPLAYER = "2"


LISTE_NIVEAUX = {1: 3, 2: 4, 3: 5, 4: 6, 5: 8, 6: 10, 7: 11, 8: 12, 9: 13, 10: 14}

NUMERO_MAX_NIVEAU = 10


uart = busio.UART(board.TX, board.RX, baudrate=9600)

def envoyer_vers_pc(texte):
    uart.write("{}\r\n".format(texte))

def recevoir_de_pc(delai_attente=0.05):
    donnees = uart.readline()
    while not donnees:
        time.sleep(0.05)
        donnees = uart.readline()
    texte = donnees
    if texte.endswith("\r\n"):
        texte = texte[:-2]
    if not texte:
        # S'il n'y a rien à part une fin de ligne,
        # on relance la fonction pour attendre du texte
        return recevoir_de_pc(delai_attente)
    return texte




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
    time.sleep(0.7)
    leds[numero_led].value = False

def doit_on_attendre(derniere_pos=None):
    tout_eteint = [False, False, False, False]
    if derniere_pos is not None:
        juste_derniere_pos_allumee = [False, False, False, False]
        juste_derniere_pos_allumee[derniere_pos] = True

    resultat_etat = etat_boutons()
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

# programme principal

def niveau(numero_niveau):
    n = LISTE_NIVEAUX[numero_niveau]
    sequence = alea_sequence(n)
    for pos in sequence:
        clignoter_led(pos)
    derniere_pos = None
    tdebut = time.time()
    for pos in sequence:
        if not bouton_correct(pos, derniere_pos):
            return False, 0
        derniere_pos = pos

    return True, (time.time() - tdebut)


def un_joueur():
    print("un joueur")
    numero_niveau = 1
    niveau_gagne = True
    signal_depart_de_pc = recevoir_de_pc()
    if signal_depart_de_pc == DEPART:
        print("recu depart")
        while numero_niveau <= NUMERO_MAX_NIVEAU and niveau_gagne:
            print("Vous jouez le niveau {}".format(numero_niveau))
            niveau_gagne, temps = niveau(numero_niveau)
            if niveau_gagne:
                print(temps)
                envoyer_vers_pc(str(temps))
                envoyer_vers_pc(GAGNE)
                numero_niveau += 1
                if numero_niveau > NUMERO_MAX_NIVEAU:
                    envoyer_vers_pc(FIN)
                    print("Vous etes le roi")
                else:
                    print("Vous passez au niveau superieur")
                    time.sleep(1)
            else:
                envoyer_vers_pc(str(temps))
                envoyer_vers_pc(PERDU)
                print("Vous etes quand meme tres nul. Vous avez perdu au niveau {}".format(numero_niveau))


def deux_joueur():
    numero_niveau = 1
    joueur1 = True
    joueur2 = True
    while numero_niveau <= NUMERO_MAX_NIVEAU and (joueur1 and joueur2):
        print("Joueur 1 essaie le niveau {}".format(numero_niveau))
        joueur1, tempsj1 = niveau(numero_niveau)
        if joueur1:
            print("Reussi")
            print(tempsj1)
        else:
            print("Perdu")
        time.sleep(2)
        print("Joueur 2 essaie le niveau {}".format(numero_niveau))
        joueur2, tempsj2 = niveau(numero_niveau)
        if joueur2:
            print("Reussi")
            print(tempsj2)
        else:
            print("Perdu")
        if joueur1 and joueur2:
            time.sleep(2)
            numero_niveau += 1
        elif joueur1 and not joueur2:
            print("le joueur 1 gagne")
        elif joueur2 and not joueur1:
            print("le joueur 2 gagne")
        else:
            print("match nul")

        if numero_niveau > NUMERO_MAX_NIVEAU:
            if tempsj1 > tempsj2:
                print("le joueur 2 gagne")
            elif tempsj2 > tempsj1:
                print("le joueur 1 gagne")
            else:
                print("Vous êtes des dieux, match nul")

print("coucou")
envoyer_vers_pc("cest moi le boss du game")
print("j'ai envoye")
signal_pc = recevoir_de_pc()
if signal_pc == SINGLEPLAYER:
    mode_jeu = 1
else:
    mode_jeu = 2

signal_pc = recevoir_de_pc()
if signal_pc == DEPART:
    time.sleep(TEMPS_AVANT_PARTIE)
    if mode_jeu == 1:
        un_joueur()
    else:
        deux_joueur()
else:
    raise Exception("signal recu : {}, attendu {}".format(signal_pc, DEPART))