from serial import Serial
import time

ENC = "utf-8"

connexion = Serial(port="/dev/ttyUSB0", baudrate=9600, timeout=1)

if not connexion.isOpen():
    raise Exception("Connexion impossible")

def envoyer_vers_carte(texte):
    connexion.write("{}\r\n".format(texte).encode(ENC))

def recevoir_de_carte(delai_attente=0.05):
    donnees = connexion.readline()
    while not donnees:
        time.sleep(delai_attente)
        donnees = connexion.readline()
    texte = donnees.decode(ENC)
    if texte.endswith("\r\n"):
        texte = texte[:-2]
    if not texte:
        # S'il n'y avait rien à part une fin de ligne
        # on relance la fonction pour attendre du texte
        return recevoir_de_carte(delai_attente)
    return texte

while True:
    valeur = int(recevoir_de_carte())
    print("[carte -> pc] {}".format(valeur))
    envoyer_vers_carte(valeur + 1)


