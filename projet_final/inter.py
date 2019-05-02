import pygame
from pygame.locals import *
from serial import Serial
from serial import time

pygame.init()

IMAGE_PHARAON = pygame.image.load("celian_pharaon.png")
IMAGE_PHARAON_PERDU = pygame.image.load("celian_perdu.png")
IMAGE_CHEVRON_J1 = pygame.image.load("chevron_j1.png")
IMAGE_CHEVRON_J2 = pygame.image.load("chevron_j2.png")
IMAGE_JEU = pygame.image.load("jeu.png")
FOND_VIDE = pygame.image.load("fond_vide.png")
IMAGE_FOND_SCORE_SOLO = pygame.image.load("fond_score_solo.png")
IMAGE_FOND_SCORE_MULTI = pygame.image.load("fond_score_multi.png")
IMAGE_PLAY = pygame.image.load("play.png")

IMAGE_FLECHE = pygame.image.load("fleche.png")

IMAGE_BOUTON_DEPART = pygame.image.load("bouton_depart.png")
IMAGE_BOUTON_AGAIN = pygame.image.load("bouton_again.png")

IMAGE_BOUTON_UN_JOUEUR = pygame.image.load("bouton_un_joueur.png")
IMAGE_BOUTON_DEUX_JOUEUR = pygame.image.load("bouton_deux_joueur.png")

#rect pour bouton_sur_interface

RECT_FLECHE = IMAGE_FLECHE.get_rect()
RECT_FLECHE.x = 750
RECT_FLECHE.y = 450

RECT_PLAY = IMAGE_PLAY.get_rect()
RECT_PLAY.x = 550
RECT_PLAY.y = 300

RECT_BOUTON_UN_JOUEUR = IMAGE_BOUTON_UN_JOUEUR.get_rect()
RECT_BOUTON_UN_JOUEUR.x = 60
RECT_BOUTON_UN_JOUEUR.y = 320

RECT_BOUTON_DEUX_JOUEUR = IMAGE_BOUTON_DEUX_JOUEUR.get_rect()
RECT_BOUTON_DEUX_JOUEUR.x = 440
RECT_BOUTON_DEUX_JOUEUR.y = 320

RECT_BOUTON_DEPART = IMAGE_BOUTON_DEPART.get_rect()
RECT_BOUTON_DEPART.x = 290
RECT_BOUTON_DEPART.y = 427

RECT_JEU = IMAGE_JEU.get_rect()
RECT_JEU.x = 0
RECT_JEU.y = 0



LARGEUR, HAUTEUR = 800, 500

# dictionnaire pour touches
CORRESPONDANCE_CLAVIER = {
    K_a: "a", K_b: "b", K_c: "c", K_d: "d", K_e: "e", K_f: "f", K_g: "g",
    K_h: "h", K_i: "i", K_j: "j", K_k: "k", K_l: "l", K_m: "m", K_n: "n",
    K_o: "o", K_p: "p", K_q: "q", K_r: "r", K_s: "s", K_t: "t", K_u: "u",
    K_v: "v", K_w: "w", K_x: "x", K_y: "y", K_z: "z"
}

# Fenetre principale
pygame.init()
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
fond_jeu = pygame.Surface(fenetre.get_size())
fond_jeu.fill((209, 196, 176))
fond_fin = pygame.Surface(fenetre.get_size())
fond_fin.fill((0, 0, 0))

#variables globales
J1 = "j1"
J2 = "j2"
J1G = "1g"
J2G = "2g"
NUL = "n"
GOD = "d"
ENC = "utf-8"
DEPART = "d"
GAGNE = "g"
PERDU = "p"
CONTINUER = "c"
FIN = "f"
NUMERO_MAX_NIVEAU = 10
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
POLICE_NIVEAU = pygame.font.SysFont("Arial", 24)
POLICE_JOUEUR = pygame.font.SysFont("Backlash BRK", 40)
POLICE_MESSAGE_VICTOIRE = pygame.font.SysFont("Arial", 25)
SINGLEPLAYER = "1"
MULTIPLAYER = "2"
VALIDE = POLICE_NIVEAU.render("Valide !", True, (0, 255, 0))
RATE = POLICE_NIVEAU.render("Perdu !", True, (255, 0, 0))

#connexion composant dans les deux sens
connexion = Serial(port="/dev/ttyUSB0", baudrate=9600, timeout=1)
if not connexion.isOpen():
    raise Exception("Connexion impossible")

# Musique Intro

pygame.mixer.music.load("musique2.wav")
pygame.mixer.music.play()

# message de l'interface
MESSAGE_JOUEUR_AVANT_PARTIE = POLICE_JOUEUR.render(
    "Name of the player  ", True, NOIR)
MESSAGE_JOUEUR_1_AVANT_PARTIE = POLICE_JOUEUR.render(
    "Name of player one : ", True, NOIR)
MESSAGE_JOUEUR_2_AVANT_PARTIE = POLICE_JOUEUR.render(
    "Name of player two : ", True, NOIR)
MESSAGE_ANNONCE_VAINQUEUR = POLICE_MESSAGE_VICTOIRE.render(
    "Vous avez battu le grand pharaon!", 1, NOIR)
MESSAGE_ANNONCE_PERDANT = POLICE_MESSAGE_VICTOIRE.render(
    "Celian reste le grand pharaon !", 1, NOIR)
MESSAGE_ANNONCE_VAINQUEUR_J1 = POLICE_MESSAGE_VICTOIRE.render(
    " J1 a gagne le jeu !", 1, BLANC)
MESSAGE_ANNONCE_VAINQUEUR_J2 = POLICE_MESSAGE_VICTOIRE.render(
    " J2 a gagne le jeu !", 1, BLANC)
MESSAGE_ANNONCE_DEUX_VAINQUEURS = POLICE_MESSAGE_VICTOIRE.render(
    "Vou etes les dieux du jeu", 1, BLANC)
MESSAGE_ANNONCE_MATCH_NUL = POLICE_MESSAGE_VICTOIRE.render(
    " MATCH NUL !", 1, BLANC)


liste_niveau_a_bliter = []
for niveau in range(1, (NUMERO_MAX_NIVEAU + 1)):
    texte_niveau = POLICE_NIVEAU.render("Niveau {} :".format(niveau), 1, BLANC)
    liste_niveau_a_bliter.append(texte_niveau)

#fonction qui envoie des message a la carte
def envoyer_vers_carte(texte):
    connexion.write("{}\r\n".format(texte).encode(ENC))

# fonction qui interprete le signal de la carte et renvoie un texte
def recevoir_de_carte(delai_attente=0.05):
    donnees = connexion.readline()
    while not donnees:
        time.sleep(delai_attente)
        donnees = connexion.readline()
    texte = donnees.decode(ENC)
    if texte.endswith("\r\n"):
        texte = texte[:-2]
    if not texte:
        # S'il n'y avait rien a pa une fin de ligne
        # on relance la fonction pour attendre du texte
        return recevoir_de_carte(delai_attente)
    return texte

class ToutQuitter(Exception):
    def __init__(self, *args):
        super().__init__(*args)

# fonction qui permet de seletionner le mode de jeu
def selection_mode_jeu():
    un_joueur = POLICE_JOUEUR.render("Singleplayer", True, NOIR)
    deux_joueur = POLICE_JOUEUR.render("Multiplayer", True, NOIR)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                raise ToutQuitter("selection_mode_jeu")
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                pos_souris = pygame.mouse.get_pos()
                x_souris = pos_souris[0]
                y_souris = pos_souris[1]
                if 60 < x_souris < 360 and 320 < y_souris < 410:
                    return SINGLEPLAYER
                elif 440 < x_souris < 740 and 320 < y_souris < 410:
                    return MULTIPLAYER
        pygame.draw.rect(fenetre, (209, 196, 176), (0, 250, 800, 260), 0)
        fenetre.blit(IMAGE_JEU, RECT_JEU)
        fenetre.blit(un_joueur, (115, 330))
        fenetre.blit(deux_joueur, (515, 330))
        fenetre.blit(IMAGE_BOUTON_UN_JOUEUR, RECT_BOUTON_UN_JOUEUR)
        fenetre.blit(IMAGE_BOUTON_DEUX_JOUEUR, RECT_BOUTON_DEUX_JOUEUR)
        pygame.display.flip()

# fonction qui demande le nom du joueur et lance jeu
def avant_partie_un_joueur():
    saisie_en_cours = True
    nom_joueur = ""
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                raise ToutQuitter("avant_partie_un_joueur")
            elif event.type == KEYDOWN:
                if event.key in CORRESPONDANCE_CLAVIER and saisie_en_cours:
                    nom_joueur += CORRESPONDANCE_CLAVIER[event.key]
                    nom_joueur = nom_joueur.title()
                if event.key == K_BACKSPACE and saisie_en_cours:
                    nom_joueur = nom_joueur[: -1]
                if event.key == K_SPACE and saisie_en_cours:
                    nom_joueur = nom_joueur + " "
                if nom_joueur and event.key == K_RETURN:
                    saisie_en_cours = False
            elif (event.type == MOUSEBUTTONDOWN and event.button == 1 and
                  not saisie_en_cours):
                pos_souris = pygame.mouse.get_pos()
                x_souris = pos_souris[0]
                y_souris = pos_souris[1]
                if 525 < x_souris < 680 and 275 < y_souris < 425:
                    return nom_joueur

        pygame.draw.rect(fenetre, (209, 196, 176), (0, 250, 800, 260), 0)
        fenetre.blit(IMAGE_JEU, RECT_JEU)
        fenetre.blit(MESSAGE_JOUEUR_AVANT_PARTIE, (10, 270))
        texte_nom_joueur = POLICE_JOUEUR.render(nom_joueur, True, (250, 97, 20))

        fenetre.blit(texte_nom_joueur, (50, 320))
        fenetre.blit(IMAGE_PLAY, RECT_PLAY)
        pygame.display.flip()

# fonction qui demande les noms des joueurs et lance la partie
def avant_partie_deux_joueur():
    saisie_en_cours_j1 = True
    saisie_en_cours_j2 = False
    nom_joueur_1 = ""
    nom_joueur_2 = ""

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                raise ToutQuitter("avant_partie_deux_joueur")
            elif event.type == KEYDOWN:
                print("coucou")
                if event.key in CORRESPONDANCE_CLAVIER and saisie_en_cours_j1:
                    nom_joueur_1 += CORRESPONDANCE_CLAVIER[event.key]
                    nom_joueur_1 = nom_joueur_1.title()
                if event.key == K_BACKSPACE and saisie_en_cours_j1:
                    nom_joueur_1 = nom_joueur_1[: -1]
                if event.key == K_SPACE and saisie_en_cours_j1:
                    nom_joueur_1 = nom_joueur_1 + " "
                if (nom_joueur_1 and saisie_en_cours_j1 and
                        not saisie_en_cours_j2 and event.key == K_RETURN):
                    saisie_en_cours_j1 = False
                    saisie_en_cours_j2 = True
                if event.key in CORRESPONDANCE_CLAVIER and saisie_en_cours_j2:
                    nom_joueur_2 += CORRESPONDANCE_CLAVIER[event.key]
                    nom_joueur_2 = nom_joueur_2.title()
                if event.key == K_BACKSPACE and saisie_en_cours_j2:
                    nom_joueur_2 = nom_joueur_2[: -1]
                if event.key == K_SPACE and saisie_en_cours_j2:
                    nom_joueur_2 = nom_joueur_2 + " "
                if (nom_joueur_2 and not saisie_en_cours_j1 and
                        saisie_en_cours_j2 and event.key == K_RETURN):
                    saisie_en_cours_j2 = False
            elif (event.type == MOUSEBUTTONDOWN and event.button == 1 and
                  not saisie_en_cours_j1 and not saisie_en_cours_j2):
                pos_souris = pygame.mouse.get_pos()
                x_souris = pos_souris[0]
                y_souris = pos_souris[1]
                if 525 < x_souris < 680 and 275 < y_souris < 425:
                    return nom_joueur_1, nom_joueur_2

        pygame.draw.rect(fenetre, (209, 196, 176), (0, 250, 800, 260), 0)
        fenetre.blit(IMAGE_JEU, RECT_JEU)
        fenetre.blit(MESSAGE_JOUEUR_1_AVANT_PARTIE, (10, 270))
        fenetre.blit(MESSAGE_JOUEUR_2_AVANT_PARTIE, (10, 385))
        texte_nom_joueur_1 = POLICE_JOUEUR.render(
            nom_joueur_1, True, (250, 97, 20))
        texte_nom_joueur_2 = POLICE_JOUEUR.render(
            nom_joueur_2, True, (250, 97, 20))
        fenetre.blit(texte_nom_joueur_1, (60, 315))
        fenetre.blit(texte_nom_joueur_2, (60, 430))
        fenetre.blit(IMAGE_PLAY, RECT_PLAY)
        pygame.display.flip()

# fonction qui execute le jeu pour un joueur
def partie_un_joueur(nom_joueur):
    jeu_en_cours = False
    jeu_fini = False
    liste_messages_a_bliter = []
    liste_temps_a_bliter = []
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                raise ToutQuitter("partie_un_joueur")
            elif (event.type == MOUSEBUTTONDOWN and event.button == 1 and
                  not jeu_en_cours and not jeu_fini):
                pos_souris = pygame.mouse.get_pos()
                x_souris = pos_souris[0]
                y_souris = pos_souris[1]
                if 300 < x_souris < 500 and 430 < y_souris < 480:
                    envoyer_vers_carte(DEPART)
                    print("DEPART")
                    jeu_en_cours = True
            elif (event.type == MOUSEBUTTONDOWN and event.button == 1 and
                  jeu_fini):
                pos_souris = pygame.mouse.get_pos()
                x_souris = pos_souris[0]
                y_souris = pos_souris[1]
                if 750 < x_souris < 800 and 450 < y_souris < 500:
                    return resultat

        pygame.draw.rect(fenetre, NOIR, (0, 800, 0, 500), 0)
        fenetre.blit(fond_jeu, (0, 0))
        fenetre.blit(IMAGE_FOND_SCORE_SOLO, (200, 70))
        texte_nom_joueur = POLICE_JOUEUR.render(nom_joueur, True, (237, 19, 88))
        fenetre.blit(texte_nom_joueur, (340, 25))
        fenetre.blit(IMAGE_BOUTON_DEPART, RECT_BOUTON_DEPART)

        for i, message_niveau in enumerate(liste_messages_a_bliter):
            fenetre.blit(message_niveau, (390, 85 + i * 30))

        for i, message_temps in enumerate(liste_temps_a_bliter):
            fenetre.blit(message_temps, (500, 85 + i * 30))

        for i, texte_niveau in enumerate(liste_niveau_a_bliter):
            fenetre.blit(texte_niveau, (235, 85 + i * 30))

        if jeu_en_cours:
            signal_de_carte = recevoir_de_carte()
            try:
                temps = float(signal_de_carte)
            except:
                raise Exception("temps non reconnu")
            message_temps = POLICE_NIVEAU.render(str(temps), True, BLANC)
            liste_temps_a_bliter.append(message_temps)

            signal_de_carte = recevoir_de_carte()
            if signal_de_carte == GAGNE:
                liste_messages_a_bliter.append(VALIDE)
                print("niveau")
            elif signal_de_carte == PERDU:
                liste_messages_a_bliter.append(RATE)
                jeu_fini = True
                resultat = PERDU
            elif signal_de_carte == GOD:
                print("god recu")
                jeu_fini = True
                resultat = GOD
            else:
                raise Exception("probleme de fin")
            jeu_en_cours = False
        if jeu_fini:
            fenetre.blit(IMAGE_FLECHE, RECT_FLECHE)

        pygame.display.flip()

def essai_joueur():
    signal_de_carte = recevoir_de_carte()
    try:
        temps = float(signal_de_carte)
    except:
        raise Exception("temps non reconnu")
    nouveau_temps_a_bliter = POLICE_NIVEAU.render(str(temps), True, (BLANC))

    signal_de_carte = recevoir_de_carte()
    if signal_de_carte == GAGNE:
        nouveau_message_a_bliter = VALIDE
    elif signal_de_carte == PERDU:
        nouveau_message_a_bliter = RATE
    else:
        raise Exception("resultat inconnu")

    return (nouveau_message_a_bliter, nouveau_temps_a_bliter)

def partie_deux_joueurs(nom_joueur_1, nom_joueur_2):
    jeu_fini = False
    jeu_en_cours = False
    image_chevron = IMAGE_CHEVRON_J1

    liste_messages_j1_a_bliter = []
    liste_temps_j1_a_bliter = []
    liste_messages_j2_a_bliter = []
    liste_temps_j2_a_bliter = []

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                raise ToutQuitter("partie_deux_joueurs")
            elif (event.type == MOUSEBUTTONDOWN and event.button == 1 and
                  not jeu_en_cours and not jeu_fini):
                pos_souris = pygame.mouse.get_pos()
                x_souris = pos_souris[0]
                y_souris = pos_souris[1]
                if 300 < x_souris < 500 and 430 < y_souris < 480:
                    envoyer_vers_carte(DEPART)
                    print("DEPART")
                    jeu_en_cours = True
            elif (event.type == MOUSEBUTTONDOWN and event.button == 1 and
                  jeu_fini):
                pos_souris = pygame.mouse.get_pos()
                x_souris = pos_souris[0]
                y_souris = pos_souris[1]
                if 750 < x_souris < 800 and 450 < y_souris < 500:
                    return resultat

        pygame.draw.rect(fenetre, NOIR, (0, 800, 0, 500), 0)
        fenetre.blit(fond_jeu, (0, 0))
        fenetre.blit(IMAGE_FOND_SCORE_MULTI, (65, 120))
        fenetre.blit(IMAGE_FOND_SCORE_MULTI, (465, 120))
        texte_nom_joueur_1 = POLICE_JOUEUR.render(
            nom_joueur_1, True, (237, 19, 88))
        texte_nom_joueur_2 = POLICE_JOUEUR.render(
            nom_joueur_2, True, (237, 19, 88))
        fenetre.blit(texte_nom_joueur_1, (160, 40))
        fenetre.blit(texte_nom_joueur_2, (550, 40))
        fenetre.blit(IMAGE_BOUTON_DEPART, RECT_BOUTON_DEPART)

        for i, message_niveau_j1 in enumerate(liste_messages_j1_a_bliter):
            fenetre.blit(message_niveau_j1, (200, 140 + i * 25))

        for i, message_temps_j1 in enumerate(liste_temps_j1_a_bliter):
            fenetre.blit(message_temps_j1, (280, 140 + i * 25))

        for i, texte_niveau_j1 in enumerate(liste_niveau_a_bliter):
            fenetre.blit(texte_niveau_j1, (90, 140 + i * 25))

        for i, message_niveau_j2 in enumerate(liste_messages_j2_a_bliter):
            fenetre.blit(message_niveau_j2, (600, 140 + i * 25))

        for i, message_temps_j2 in enumerate(liste_temps_j2_a_bliter):
            fenetre.blit(message_temps_j2, (680, 140 + i * 25))

        for i, texte_niveau_j2 in enumerate(liste_niveau_a_bliter):
            fenetre.blit(texte_niveau_j2, (490, 140 + i * 25))

        fenetre.blit(image_chevron, (380, 140))

        if jeu_en_cours:

            signal_de_carte = recevoir_de_carte()

            if signal_de_carte == J1:
                image_chevron = IMAGE_CHEVRON_J2
                nouveau_message_j1_a_bliter, nouveau_temps_j1_a_bliter = \
                    essai_joueur()
                liste_messages_j1_a_bliter.append(nouveau_message_j1_a_bliter)
                liste_temps_j1_a_bliter.append(nouveau_temps_j1_a_bliter)

            elif signal_de_carte == J2:
                image_chevron = IMAGE_CHEVRON_J1
                nouveau_message_j2_a_bliter, nouveau_temps_j2_a_bliter = \
                    essai_joueur()
                liste_messages_j2_a_bliter.append(nouveau_message_j2_a_bliter)
                liste_temps_j2_a_bliter.append(nouveau_temps_j2_a_bliter)
            else:
                raise Exception("Message inconnu")
            jeu_en_cours = False

            signal_de_carte = recevoir_de_carte()
            if signal_de_carte == FIN:
                print("FIN")
                signal_de_carte = recevoir_de_carte()
                if signal_de_carte not in [J1G, J2G, NUL, GOD]:
                    raise Exception("Message non conforme")
                else:
                    resultat = signal_de_carte
                    jeu_fini = True
                    image_chevron = FOND_VIDE
            elif signal_de_carte == CONTINUER:
                pass
            else:
                raise Exception("Message inconnu (2)")

        if jeu_fini:
            fenetre.blit(IMAGE_FLECHE, RECT_FLECHE)

        pygame.display.flip()

# fonction qui affiche la fenetre de fin
def fin_de_partie_un_joueur(resultat_partie):
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                raise ToutQuitter("fin_de_partie_un_joueur")
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                pos_souris = pygame.mouse.get_pos()
                x_souris = pos_souris[0]
                y_souris = pos_souris[1]
                if 290 < x_souris < 590 and 427 < y_souris < 517:
                    main()
        fenetre.blit(fond_fin, (0, 0))
        fenetre.blit(IMAGE_BOUTON_AGAIN, (290, 427))
        if resultat_partie == GOD:
            fenetre.blit(IMAGE_PHARAON_PERDU, (150, 0))
            fenetre.blit(MESSAGE_ANNONCE_VAINQUEUR, (140, 30))
        elif resultat_partie == PERDU:
            fenetre.blit(IMAGE_PHARAON, (150, 0))
            fenetre.blit(MESSAGE_ANNONCE_PERDANT, (155, 30))
        else:
            raise Exception("Resultat inconnu")

        pygame.display.flip()


def fin_de_partie_deux_joueur(resultat_partie):
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                raise ToutQuitter("fin_de_partie_deux_joueur")
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                pos_souris = pygame.mouse.get_pos()
                x_souris = pos_souris[0]
                y_souris = pos_souris[1]
                if 290 < x_souris < 590 and 427 < y_souris < 517:
                    main()

        fenetre.blit(fond_fin, (0, 0))
        fenetre.blit(IMAGE_BOUTON_AGAIN, (290, 427))
        if resultat_partie == J1G:
            fenetre.blit(MESSAGE_ANNONCE_VAINQUEUR_J1, (200, 50))
        elif resultat_partie == J2G:
            fenetre.blit(MESSAGE_ANNONCE_VAINQUEUR_J2, (200, 50))
        elif resultat_partie == GOD:
            fenetre.blit(MESSAGE_ANNONCE_DEUX_VAINQUEURS, (200, 50))
        elif resultat_partie == NUL:
            fenetre.blit(MESSAGE_ANNONCE_MATCH_NUL, (200, 50))
        else:
            raise Exception("resultat inconnu (2)")

        pygame.display.flip()

def handshake():
    print("Je vais aller dire bonjour a la carte")
    envoyer_vers_carte("Bonjour Mme la carte !")
    print("j'ai dis bonjour à Mme la carte.\n"
          "J'attends qu'elle me dise bonjour en retour")
    print("Mme la carte m'a dit bonjour : \"{}\"".format(recevoir_de_carte()))
    print("On peut commencer\n")

# programme principal


def main():
    handshake()

    mode = selection_mode_jeu()
    envoyer_vers_carte(mode)

    if mode == SINGLEPLAYER:
        nom_joueur = avant_partie_un_joueur()
        resultat_partie = partie_un_joueur(nom_joueur)
        fin_de_partie_un_joueur(resultat_partie)
    else:
        nom_joueur_1, nom_joueur_2 = avant_partie_deux_joueur()
        resultat_partie = partie_deux_joueurs(nom_joueur_1, nom_joueur_2)
        fin_de_partie_deux_joueur(resultat_partie)

if __name__ == "__main__":
    try:
        main()
    except ToutQuitter as ou_on_est_quand_on_quitte:
        print("On a quitté à {}".format(ou_on_est_quand_on_quitte))
    pygame.quit()
