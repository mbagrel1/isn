# +---------------------------------------------------------------------------+
# |                           Import des librairies                           |
# +---------------------------------------------------------------------------+

import pygame
from pygame.locals import *
from serial import Serial
from serial import time


ENC = "utf-8"

# Initialisation de pygame
pygame.init()

#connexion composant dans les deux sens
connexion = Serial(port="/dev/ttyUSB0", baudrate=9600, timeout=1)
if not connexion.isOpen():
    raise Exception("Connexion impossible")

# Musique Intro

pygame.mixer.music.load("musique2.wav")
pygame.mixer.music.play()


# +---------------------------------------------------------------------------+
# |                           Chargement des images                           |
# +---------------------------------------------------------------------------+

# boutons
IMAGE_BOUTON_DEPART = pygame.image.load("bouton_depart.png")
IMAGE_BOUTON_AGAIN = pygame.image.load("bouton_again.png")
IMAGE_BOUTON_UN_JOUEUR = pygame.image.load("bouton_un_joueur.png")
IMAGE_BOUTON_DEUX_JOUEUR = pygame.image.load("bouton_deux_joueur.png")

# texte de fin de partie
IMAGE_GAME_OVER = pygame.image.load("game_over.png")
IMAGE_CONGRAT = pygame.image.load("congrat.png")

# autres elements de l'interface
IMAGE_ICONE = pygame.image.load("icone.png")
IMAGE_CHEVRON_J1 = pygame.image.load("chevron_j1.png")
IMAGE_CHEVRON_J2 = pygame.image.load("chevron_j2.png")
IMAGE_JEU = pygame.image.load("jeu.png")
FOND_VIDE = pygame.image.load("fond_vide.png")
IMAGE_FOND_SCORE_SOLO = pygame.image.load("fond_score_solo.png")
IMAGE_FOND_SCORE_MULTI = pygame.image.load("fond_score_multi.png")
IMAGE_PLAY = pygame.image.load("play.png")
IMAGE_FLECHE = pygame.image.load("fleche.png")

# +---------------------------------------------------------------------------+
# |                             Rect pour boutons                             |
# +---------------------------------------------------------------------------+

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

# +---------------------------------------------------------------------------+
# |                   Dictionnaire touche clavier et pygame                   |
# +---------------------------------------------------------------------------+

CORRESPONDANCE_CLAVIER = {
    K_a: "a", K_b: "b", K_c: "c", K_d: "d", K_e: "e", K_f: "f", K_g: "g",
    K_h: "h", K_i: "i", K_j: "j", K_k: "k", K_l: "l", K_m: "m", K_n: "n",
    K_o: "o", K_p: "p", K_q: "q", K_r: "r", K_s: "s", K_t: "t", K_u: "u",
    K_v: "v", K_w: "w", K_x: "x", K_y: "y", K_z: "z"
}

# +---------------------------------------------------------------------------+
# |                    Initialisation de la fenêtre pygame                    |
# +---------------------------------------------------------------------------+

LARGEUR, HAUTEUR = 800, 500
FENETRE = pygame.display.set_mode((LARGEUR, HAUTEUR))
NOM_FENETRE = pygame.display.set_caption("Light It Up !")
pygame.display.set_icon(IMAGE_ICONE)
FOND_JEU = pygame.Surface(FENETRE.get_size())
FOND_JEU.fill((209, 196, 176))
FOND_FIN = pygame.Surface(FENETRE.get_size())
FOND_FIN.fill((209, 196, 176))

# +---------------------------------------------------------------------------+
# |                          Signaux de commuication                          |
# +---------------------------------------------------------------------------+

J1 = "j1"
J2 = "j2"
J1G = "1g"
J2G = "2g"
NUL = "n"
GOD = "d"
DEPART = "d"
GAGNE = "g"
PERDU = "p"
CONTINUER = "c"
FIN = "f"
SINGLEPLAYER = "1"
MULTIPLAYER = "2"
CLIC_GAUCHE = 1
NUMERO_MAX_NIVEAU = 10

# +---------------------------------------------------------------------------+
# |                          Couleurs de l'interface                          |
# +---------------------------------------------------------------------------+

BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)
BEIGE = (209, 196, 176)
ORANGE = (250, 97, 20)
FUSHIA = (237, 19, 88)

# +---------------------------------------------------------------------------+
# |                          Polices de l'interface                           |
# +---------------------------------------------------------------------------+

POLICE_NIVEAU = pygame.font.Font("/home/marie/.fonts/Aileron-Regular.otf", 24)
POLICE_JOUEUR = pygame.font.SysFont("Backlash BRK", 40)
POLICE_MESSAGE_VICTOIRE = pygame.font.SysFont("Backlash BRK", 40)

# +---------------------------------------------------------------------------+
# |                          Messages de l'interface                          |
# +---------------------------------------------------------------------------+

MESSAGE_JOUEUR_AVANT_PARTIE = POLICE_JOUEUR.render(
    "Name of the player  ", True, NOIR)
MESSAGE_JOUEUR_1_AVANT_PARTIE = POLICE_JOUEUR.render(
    "Name of player one : ", True, NOIR)
MESSAGE_JOUEUR_2_AVANT_PARTIE = POLICE_JOUEUR.render(
    "Name of player two : ", True, NOIR)
MESSAGE_ANNONCE_VAINQUEUR = POLICE_MESSAGE_VICTOIRE.render(
    "You have reached the maximum level !", 1, NOIR)
MESSAGE_ANNONCE_PERDANT = POLICE_MESSAGE_VICTOIRE.render(
    "You have failed this game !", 1, NOIR)
MESSAGE_ANNONCE_DEUX_VAINQUEURS = POLICE_MESSAGE_VICTOIRE.render(
    "You both have reached the maximum level", 1, NOIR)
MESSAGE_ANNONCE_MATCH_NUL = POLICE_MESSAGE_VICTOIRE.render(
    "Equality !", 1, NOIR)
VALIDE = POLICE_NIVEAU.render("Correct !", True, VERT)
RATE = POLICE_NIVEAU.render("Wrong !", True, ROUGE)

# boucle pour permettre le blit des niveau dans le jeu

LISTE_NIVEAU_A_BLITER = []
for niveau in range(1, (NUMERO_MAX_NIVEAU + 1)):
    texte_niveau = POLICE_NIVEAU.render("Level {} ".format(niveau), 1, BLANC)
    LISTE_NIVEAU_A_BLITER.append(texte_niveau)

# +---------------------------------------------------------------------------+
# |      Type d'exception qui est utilisé pour quitter la fenetre de jeu      |
# +---------------------------------------------------------------------------+

class ToutQuitter(Exception):
    def __init__(self, *args):
        super().__init__(*args)

# +---------------------------------------------------------------------------+
# | Définition des fonctions qui assurent la communication dans les deux sens |
# +---------------------------------------------------------------------------+

def envoyer_vers_carte(texte):
    """Fonction envoyant le texte spécifié vers la carte.
    :param texte: texte à envoyer vers la carte
    :return: rien (None)
    """
    connexion.write("{}\r\n".format(texte).encode(ENC))


def recevoir_de_carte(delai_attente=0.05):
    """Fonction recupérant le texte envoyé par la carte.
    :param delai_attente: temps de rafraichissement entre deux tours de boucles
    :return: le texte reçu de la carte
    """
    donnees = connexion.readline()
    while not donnees:
        time.sleep(delai_attente)
        donnees = connexion.readline()
    texte = donnees.decode(ENC)
    if texte.endswith("\r\n"):
        # (si le texte fini par les caractères de fin de lignes,
        # on enlève ces caractères)
        texte = texte[:-2]
    if not texte:
        # S'il n'y avait rien a par une fin de ligne
        # on relance la fonction pour attendre du texte
        return recevoir_de_carte(delai_attente)
    return texte

# +---------------------------------------------------------------------------+
# |                      Définition des fonctions du jeu                      |
# +---------------------------------------------------------------------------+

def selection_mode_jeu():
    """Fonction qui affiche le menu de selection du mode de jeu.
    :return: le mode de jeu selectionne par l'utilisateur
    """
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                raise ToutQuitter("selection_mode_jeu")
            elif event.type == MOUSEBUTTONDOWN and event.button == CLIC_GAUCHE:
                # si on detecte l'evenement de clic gauche appuyé de la souris
                pos_souris = pygame.mouse.get_pos()
                x_souris = pos_souris[0]
                y_souris = pos_souris[1]
                if 60 < x_souris < 360 and 320 < y_souris < 410:
                    # le bouton solo est considéré comme selectionné
                    return SINGLEPLAYER
                elif 440 < x_souris < 740 and 320 < y_souris < 410:
                    # le bouton deux joueurs est considéré comme sélectionné
                    return MULTIPLAYER
        pygame.draw.rect(FENETRE, BEIGE, (0, 250, 800, 260), 0)
        FENETRE.blit(IMAGE_JEU, (0, 0))
        FENETRE.blit(IMAGE_BOUTON_UN_JOUEUR, RECT_BOUTON_UN_JOUEUR)
        FENETRE.blit(IMAGE_BOUTON_DEUX_JOUEUR, RECT_BOUTON_DEUX_JOUEUR)
        pygame.display.flip()

def avant_partie_un_joueur():
    """Fonction qui permet la saisie du nom du joueur solo
    :return: le nom du joueur solo
    """
    saisie_en_cours = True
    nom_joueur = ""
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                raise ToutQuitter("avant_partie_un_joueur")
            elif event.type == KEYDOWN:
                if event.key in CORRESPONDANCE_CLAVIER and saisie_en_cours:
                    # si la touche appuye est dans le dictionnaire
                    # si la saisie n'est pas fini
                    nom_joueur += CORRESPONDANCE_CLAVIER[event.key]
                    # on ajoute la lettre correspondante au nom
                    nom_joueur = nom_joueur.title()
                    # on met la première lettre en majuscule
                if event.key == K_BACKSPACE and saisie_en_cours:
                    nom_joueur = nom_joueur[: -1]
                    # on efface le dernier caractère si la chaine
                    # n'est pas vide
                if event.key == K_SPACE and saisie_en_cours:
                    nom_joueur = nom_joueur + " "
                    # on ajoute un espace à la chaine
                if nom_joueur and event.key == K_RETURN:
                    saisie_en_cours = False
                    # on termine la saisie en appuyant sur entrée
            elif (event.type == MOUSEBUTTONDOWN and
                  event.button == CLIC_GAUCHE and
                  not saisie_en_cours):
                pos_souris = pygame.mouse.get_pos()
                x_souris = pos_souris[0]
                y_souris = pos_souris[1]
                if 525 < x_souris < 680 and 275 < y_souris < 425:
                    # le bouton play est considéré comme appuyé
                    return nom_joueur

        pygame.draw.rect(FENETRE, BEIGE, (0, 250, 800, 260), 0)
        FENETRE.blit(IMAGE_JEU, (0, 0))
        FENETRE.blit(MESSAGE_JOUEUR_AVANT_PARTIE, (10, 270))
        texte_nom_joueur = POLICE_JOUEUR.render(nom_joueur, True, ORANGE)

        FENETRE.blit(texte_nom_joueur, (50, 320))
        FENETRE.blit(IMAGE_PLAY, RECT_PLAY)
        pygame.display.flip()


def avant_partie_deux_joueur():
    """ Fonction qui permet la saisie des noms des deux joueurs
    :return: les noms des deux joueurs
    """
    saisie_en_cours_j1 = True
    saisie_en_cours_j2 = False
    nom_joueur_1 = ""
    nom_joueur_2 = ""

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                raise ToutQuitter("avant_partie_deux_joueur")
            elif event.type == KEYDOWN:
                if event.key in CORRESPONDANCE_CLAVIER and saisie_en_cours_j1:
                    # si la touche appuyée est dans le dictionnaire
                    # si la saisie du nom du j1 est en cours
                    nom_joueur_1 += CORRESPONDANCE_CLAVIER[event.key]
                    # on ajoute la lettre au nom du j1
                    nom_joueur_1 = nom_joueur_1.title()
                    # on met la première lettre de chaque mot j1 en majuscule
                if event.key == K_BACKSPACE and saisie_en_cours_j1:
                    nom_joueur_1 = nom_joueur_1[: -1]
                    # on efface la dernière lettre
                    #si la chaine du j1 n'est pas vide
                if event.key == K_SPACE and saisie_en_cours_j1:
                    nom_joueur_1 = nom_joueur_1 + " "
                    # on ajoute un espace à la chaine du j1
                if (nom_joueur_1 and saisie_en_cours_j1 and
                        not saisie_en_cours_j2 and event.key == K_RETURN):
                    # on termine la saisie du j1 en appuyant sur entrée
                    saisie_en_cours_j1 = False
                    saisie_en_cours_j2 = True
                if event.key in CORRESPONDANCE_CLAVIER and saisie_en_cours_j2:
                    # si la touche appuyée est dans le dictionnaire
                    # si la saisie du nom du j2 est en cours
                    nom_joueur_2 += CORRESPONDANCE_CLAVIER[event.key]
                    # on ajoute la lettre au nom du j2
                    nom_joueur_2 = nom_joueur_2.title()
                    # on met la première lettre de chaque mot j2 en majuscule
                if event.key == K_BACKSPACE and saisie_en_cours_j2:
                    nom_joueur_2 = nom_joueur_2[: -1]
                    # on efface la dernière lettre
                    #si la chaine du j2 n'est pas vide
                if event.key == K_SPACE and saisie_en_cours_j2:
                    nom_joueur_2 = nom_joueur_2 + " "
                    # on ajoute un espace à la chaine du j2
                if (nom_joueur_2 and not saisie_en_cours_j1 and
                        saisie_en_cours_j2 and event.key == K_RETURN):
                    # on termine la saisie du j2 en appuyant sur entrée
                    saisie_en_cours_j2 = False
            elif (event.type == MOUSEBUTTONDOWN and
                  event.button == CLIC_GAUCHE and not saisie_en_cours_j1 and
                  not saisie_en_cours_j2):
                    # si la saisie n'est plus en cours et si on clique gauche
                pos_souris = pygame.mouse.get_pos()
                x_souris = pos_souris[0]
                y_souris = pos_souris[1]
                if 525 < x_souris < 680 and 275 < y_souris < 425:
                    # le bouton play est considéré comme appuyé
                    return nom_joueur_1, nom_joueur_2

        pygame.draw.rect(FENETRE, BEIGE, (0, 250, 800, 260), 0)
        FENETRE.blit(IMAGE_JEU, (0, 0))
        FENETRE.blit(MESSAGE_JOUEUR_1_AVANT_PARTIE, (10, 270))
        FENETRE.blit(MESSAGE_JOUEUR_2_AVANT_PARTIE, (10, 385))
        texte_nom_joueur_1 = POLICE_JOUEUR.render(
            nom_joueur_1, True, ORANGE)
        texte_nom_joueur_2 = POLICE_JOUEUR.render(
            nom_joueur_2, True, ORANGE)
        FENETRE.blit(texte_nom_joueur_1, (60, 315))
        FENETRE.blit(texte_nom_joueur_2, (60, 430))
        FENETRE.blit(IMAGE_PLAY, RECT_PLAY)
        pygame.display.flip()

def partie_un_joueur(nom_joueur):
    """Fonction qui affiche dans l'interface l'avancement dans le jeu solo
    :param nom_joueur: le nom du joueur solo
    :return: le résultat perdu ou gagné de la partie et le niveau
             correspondant à la fin de la partie
    """
    jeu_en_cours = False
    jeu_fini = False
    liste_messages_a_bliter = []
    liste_temps_a_bliter = []
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                raise ToutQuitter("partie_un_joueur")
            elif (event.type == MOUSEBUTTONDOWN and
                  event.button == CLIC_GAUCHE and not jeu_en_cours and
                  not jeu_fini):
                    # si le jeu est en cours et pas fini et qu'on clique gauche
                pos_souris = pygame.mouse.get_pos()
                x_souris = pos_souris[0]
                y_souris = pos_souris[1]
                if 300 < x_souris < 500 and 430 < y_souris < 480:
                    # le bouton play est consdéré comme appuyé
                    envoyer_vers_carte(DEPART)
                    print("DEPART")
                    jeu_en_cours = True
            elif (event.type == MOUSEBUTTONDOWN and
                  event.button == CLIC_GAUCHE and jeu_fini):
                    # si on clique gauche et que je jeu est fini
                pos_souris = pygame.mouse.get_pos()
                x_souris = pos_souris[0]
                y_souris = pos_souris[1]
                if 750 < x_souris < 800 and 450 < y_souris < 500:
                    # le bouton fleche est considéré comme cliqué
                    niveau = len(liste_messages_a_bliter)
                    return resultat, niveau

        pygame.draw.rect(FENETRE, NOIR, (0, 800, 0, 500), 0)
        FENETRE.blit(FOND_JEU, (0, 0))
        FENETRE.blit(IMAGE_FOND_SCORE_SOLO, (200, 70))
        texte_nom_joueur = POLICE_JOUEUR.render(nom_joueur, True, FUSHIA)
        FENETRE.blit(texte_nom_joueur, (340, 25))
        FENETRE.blit(IMAGE_BOUTON_DEPART, RECT_BOUTON_DEPART)

# boucle qui permet d'afficher les messages correct ou perdu dans l'interface
        for i, message_niveau in enumerate(liste_messages_a_bliter):
            FENETRE.blit(message_niveau, (375, 85 + i * 30))

# boucle qui permet d'afficher le temps pour chaque niveau
        for i, message_temps in enumerate(liste_temps_a_bliter):
            FENETRE.blit(message_temps, (500, 85 + i * 30))

# boucle qui permet d'afficher les niveaux dans l'interface
        for i, texte_niveau in enumerate(LISTE_NIVEAU_A_BLITER):
            FENETRE.blit(texte_niveau, (235, 85 + i * 30))

        if jeu_en_cours:
            signal_de_carte = recevoir_de_carte()
            try:
                temps = float(signal_de_carte)
            except:
                raise Exception("temps non reconnu")
            message_temps = POLICE_NIVEAU.render(
                "{:.2f}".format(temps), True, BLANC)
            liste_temps_a_bliter.append(message_temps)

            signal_de_carte = recevoir_de_carte()
            if signal_de_carte == GAGNE:
                liste_messages_a_bliter.append(VALIDE)
                # le niveau est considéré comme gagné
                print("niveau gagné")
            elif signal_de_carte == PERDU:
                liste_messages_a_bliter.append(RATE)
                #le niveau est considéré comme perdu
                print("niveau perdu")
                jeu_fini = True
                resultat = PERDU
            elif signal_de_carte == GOD:
                liste_messages_a_bliter.append(VALIDE)
                # le jeu est considéré comme gagné
                print("god recu")
                jeu_fini = True
                resultat = GOD
            else:
                raise Exception("probleme de fin")
            jeu_en_cours = False
        if jeu_fini:
            FENETRE.blit(IMAGE_FLECHE, RECT_FLECHE)
            # on affiche la flèche qui permet d'accéder à l'interface de fin

        pygame.display.flip()

def essai_joueur():
    """Fonction pour le mode deux joueurs qui permet de generer les
        messages à afficher dans l'interface de jeu en fonction des donnees
        de la carte pour un niveau
        :return: le message qui valide ou invalide le niveau et le
                 temps associé au niveau essayé
        """
    signal_de_carte = recevoir_de_carte()
    try:
        temps = float(signal_de_carte)
    except:
        raise Exception("temps non reconnu")
    nouveau_temps_a_bliter = POLICE_NIVEAU.render(
        "{:.2f}".format(temps), True, (BLANC))

    signal_de_carte = recevoir_de_carte()
    if signal_de_carte == GAGNE:
        nouveau_message_a_bliter = VALIDE
        # le niveau est considéré comme gagné
        print("niveau gagné")
    elif signal_de_carte == PERDU:
        nouveau_message_a_bliter = RATE
        # le niveau est considéré comme perdu
        print("niveau perdu")
    else:
        raise Exception("resultat inconnu")

    return (nouveau_message_a_bliter, nouveau_temps_a_bliter)

def partie_deux_joueurs(nom_joueur_1, nom_joueur_2):
    """ Fonction qui affiche dans l'interface l'avancement dans le jeu
        deux joueurs
    :param nom_joueur1: le nom du joueur 1
    :param nom_joueur2: le nom du joueur 2
    :return : le resultat de la fin de la partie (match nul, joueur 1
              vainqueur, joueur 2 vainqueur ou dieux)
    """
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
            elif (event.type == MOUSEBUTTONDOWN and
                  event.button == CLIC_GAUCHE and
                  not jeu_en_cours and not jeu_fini):
                # si le jeu est en cours et n'est pas fini et qu'on clique gauche
                pos_souris = pygame.mouse.get_pos()
                x_souris = pos_souris[0]
                y_souris = pos_souris[1]
                if 300 < x_souris < 500 and 430 < y_souris < 480:
                    # le bouton play est considéré comme appuyé
                    envoyer_vers_carte(DEPART)
                    print("DEPART")
                    jeu_en_cours = True
            elif (event.type == MOUSEBUTTONDOWN and
                  event.button == CLIC_GAUCHE and jeu_fini):
                # si le jeu est fini et qu'on clique gauche
                pos_souris = pygame.mouse.get_pos()
                x_souris = pos_souris[0]
                y_souris = pos_souris[1]
                if 750 < x_souris < 800 and 450 < y_souris < 500:
                    # le bouton flèche est considéré comme cliqué
                    return resultat

        pygame.draw.rect(FENETRE, NOIR, (0, 800, 0, 500), 0)
        FENETRE.blit(FOND_JEU, (0, 0))
        FENETRE.blit(IMAGE_FOND_SCORE_MULTI, (55, 120))
        FENETRE.blit(IMAGE_FOND_SCORE_MULTI, (465, 120))
        texte_nom_joueur_1 = POLICE_JOUEUR.render(
            nom_joueur_1, True, FUSHIA)
        texte_nom_joueur_2 = POLICE_JOUEUR.render(
            nom_joueur_2, True, FUSHIA)
        FENETRE.blit(texte_nom_joueur_1, (160, 40))
        FENETRE.blit(texte_nom_joueur_2, (550, 40))
        FENETRE.blit(IMAGE_BOUTON_DEPART, RECT_BOUTON_DEPART)


#pour le joueur 1
# boucle qui permet d'afficher les messages correct ou perdu dans l'interface
        for i, message_niveau_j1 in enumerate(liste_messages_j1_a_bliter):
            FENETRE.blit(message_niveau_j1, (180, 140 + i * 25))


# boucle qui permet d'afficher le temps pour chaque niveau
        for i, message_temps_j1 in enumerate(liste_temps_j1_a_bliter):
            FENETRE.blit(message_temps_j1, (280, 140 + i * 25))


# boucle qui permet d'afficher les niveaux dans l'interface
        for i, texte_niveau_j1 in enumerate(LISTE_NIVEAU_A_BLITER):
            FENETRE.blit(texte_niveau_j1, (80, 140 + i * 25))

# pour le joueur 2
# boucle qui permet d'afficher les messages correct ou perdu dans l'interface

        for i, message_niveau_j2 in enumerate(liste_messages_j2_a_bliter):
            FENETRE.blit(message_niveau_j2, (580, 140 + i * 25))


# boucle qui permet d'afficher le temps pour chaque niveau
        for i, message_temps_j2 in enumerate(liste_temps_j2_a_bliter):
            FENETRE.blit(message_temps_j2, (680, 140 + i * 25))


# boucle qui permet d'afficher les niveaux dans l'interface
        for i, texte_niveau_j2 in enumerate(LISTE_NIVEAU_A_BLITER):
            FENETRE.blit(texte_niveau_j2, (480, 140 + i * 25))

        FENETRE.blit(image_chevron, (380, 140))

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
            FENETRE.blit(IMAGE_FLECHE, RECT_FLECHE)
            # on affiche la fleche qui permet de mettre l'écran de jeu

        pygame.display.flip()

def fin_de_partie_un_joueur(resultat_partie, niveau):
    """Fonction qui permet l'affichage des messages de fin de partie un joueur
       dans l'interface de jeu
    :param resultat_partie: le resultat god ou perdu de la carte
    : param niveau: le niveau ou la fin de partie a été déclenchée
    :return: rien (None)
    """
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                print("sortie")
                raise ToutQuitter("fin_de_partie_un_joueur")
            elif event.type == MOUSEBUTTONDOWN and event.button == CLIC_GAUCHE:
                # si on clique gauche
                pos_souris = pygame.mouse.get_pos()
                x_souris = pos_souris[0]
                y_souris = pos_souris[1]
                if 290 < x_souris < 590 and 427 < y_souris < 517:
                    # le bouton recommencer est considéré comme cliqué
                    print("recommencer")
                    main()
        niveau_affiche = POLICE_MESSAGE_VICTOIRE.render(
            "Level : {}".format(niveau), True, ORANGE)
        FENETRE.blit(FOND_FIN, (0, 0))
        FENETRE.blit(IMAGE_BOUTON_AGAIN, (290, 427))
        FENETRE.blit(niveau_affiche, (310, 230))
        if resultat_partie == GOD:
            FENETRE.blit(IMAGE_CONGRAT, (3, 10))
            FENETRE.blit(MESSAGE_ANNONCE_VAINQUEUR, (90, 300))
        elif resultat_partie == PERDU:
            FENETRE.blit(IMAGE_GAME_OVER, (8, 10))
            FENETRE.blit(MESSAGE_ANNONCE_PERDANT, (155, 300))
        else:
            raise Exception("Resultat inconnu")

        pygame.display.flip()


def fin_de_partie_deux_joueur(resultat_partie, nom_joueur_1, nom_joueur_2):
    """Fonction qui permet l'affichage des messages de fin de partie
       deux joueurs sur l'interface de jeu.
    :param resultat_partie: le resultat de la partie deux joueurs
                            (message correspondant)
    :param nom_joueur_1: le nom du joueur 1
    :param nom_joueur_2: le nom du joueur 2
    :return: rien (None)
    """

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                raise ToutQuitter("fin_de_partie_deux_joueur")
            elif event.type == MOUSEBUTTONDOWN and event.button == CLIC_GAUCHE:
                # si on clique gauche
                pos_souris = pygame.mouse.get_pos()
                x_souris = pos_souris[0]
                y_souris = pos_souris[1]
                if 290 < x_souris < 590 and 427 < y_souris < 517:
                    # le bouton recommencer est considéré comme cliqué
                    print("recommencer")
                    main()

        FENETRE.blit(FOND_FIN, (0, 0))
        FENETRE.blit(IMAGE_BOUTON_AGAIN, (290, 427))
        if resultat_partie == J1G:
            FENETRE.blit(IMAGE_GAME_OVER, (8, 10))
            MESSAGE_ANNONCE_VAINQUEUR_J1 = POLICE_MESSAGE_VICTOIRE.render(
                " {} has won the match !".format(nom_joueur_1), 1, NOIR)
            FENETRE.blit(MESSAGE_ANNONCE_VAINQUEUR_J1, (170, 250))
        elif resultat_partie == J2G:
            FENETRE.blit(IMAGE_GAME_OVER, (8, 10))
            MESSAGE_ANNONCE_VAINQUEUR_J2 = POLICE_MESSAGE_VICTOIRE.render(
                " {} has won the match !".format(nom_joueur_2), 1, NOIR)
            FENETRE.blit(MESSAGE_ANNONCE_VAINQUEUR_J2, (170, 250))
        elif resultat_partie == GOD:
            FENETRE.blit(IMAGE_CONGRAT, (3, 10))
            FENETRE.blit(MESSAGE_ANNONCE_DEUX_VAINQUEURS, (90, 250))
        elif resultat_partie == NUL:
            FENETRE.blit(IMAGE_GAME_OVER, (3, 10))
            FENETRE.blit(MESSAGE_ANNONCE_MATCH_NUL, (310, 250))
        else:
            raise Exception("resultat inconnu (2)")

        pygame.display.flip()

def handshake():
    """Fonction qui permet de vérifier le fonctionnement de la
       communication dans les deux sens avant de commencer le jeu
    :return: rien (None)
    """
    print("Je vais aller dire bonjour a la carte")
    envoyer_vers_carte("Bonjour Mme la carte !")
    print("j'ai dis bonjour à Mme la carte.\n"
          "J'attends qu'elle me dise bonjour en retour")
    signal_de_carte = recevoir_de_carte()
    if signal_de_carte == "Bonjour M. le PC !":
        print("Mme la carte m'a dit bonjour : \"{}\"".format(signal_de_carte))
        print("On peut commencer\n")
    else:
        raise Exception("Message pas courtois")

# +---------------------------------------------------------------------------+
# |                            Fonction principale                            |
# +---------------------------------------------------------------------------+

def main():
    """Fonction principale"""
    handshake()

    mode = selection_mode_jeu()
    envoyer_vers_carte(mode)

    if mode == SINGLEPLAYER:
        nom_joueur = avant_partie_un_joueur()
        resultat_partie, niveau = partie_un_joueur(nom_joueur)
        fin_de_partie_un_joueur(resultat_partie, niveau)
    else:
        nom_joueur_1, nom_joueur_2 = avant_partie_deux_joueur()
        resultat_partie = partie_deux_joueurs(nom_joueur_1, nom_joueur_2)
        fin_de_partie_deux_joueur(resultat_partie, nom_joueur_1, nom_joueur_2)

if __name__ == "__main__":
    try:
        main()
    except ToutQuitter as ou_on_est_quand_on_quitte:
        print("On a quitté à {}".format(ou_on_est_quand_on_quitte))
    pygame.quit()
