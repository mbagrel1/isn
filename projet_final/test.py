import pygame
from pygame.locals import *
continuer = True
continuer_jeu = True
continuer_fin = True
# initialisation
pygame.init()
LARGEUR, HAUTEUR = 800, 500
fenetre = pygame.display.set_mode((800, 500))
fenetre_jeu = pygame.display.set_mode((800, 500))


# Fenetre intro

font = pygame.font.SysFont("Arial", 24)
font2 = pygame.font.SysFont("Atavyros", 32)
text = font.render("Name of player one:", 1, (0, 0, 0))
text2 = font.render("Name of player two:", 1, (0, 0, 0))
button = pygame.image.load("play1.jpg").convert()
button_rect = button.get_rect()
button_rect.x = 550
button_rect.y = 250


# Fenetre jeu
font3 = pygame.font.SysFont("Arial", 60)
text3 = font.render("Name of player one:", 1, (250, 250, 250))
text4 = font.render("Name of player two:", 1, (250, 250, 250))
button2 = pygame.image.load("fleche.jpeg").convert()
button2_rect = button2.get_rect()
fond = pygame.Surface(fenetre.get_size())
button2_rect.x = 750
button2_rect.y = 450
fond.fill((0, 0, 0))

# Fenetre fin
fond2 = pygame.Surface(fenetre.get_size())
text5 = font3.render("Celian est le grand champion!", 1, (250, 250, 250))
fond2.fill((255, 0, 0))

# Niveaux
niveau1 = font.render("Niveau 1:", 1, (255, 255, 255))
niveau2 = font.render("Niveau 2:", 1, (255, 255, 255))
niveau3 = font.render("Niveau 3:", 1, (255, 255, 255))
niveau4 = font.render("Niveau 4:", 1, (255, 255, 255))
niveau5 = font.render("Niveau 5:", 1, (255, 255, 255))
niveau6 = font.render("Niveau 6:", 1, (255, 255, 255))
niveau7 = font.render("Niveau 7:", 1, (255, 255, 255))
niveau8 = font.render("Niveau 8:", 1, (255, 255, 255))
niveau9 = font.render("Niveau 9:", 1, (255, 255, 255))
niveau10 = font.render("Niveau 10:", 1, (255, 255, 255))
# Musique Intro

# pygame.mixer.music.load('musique.wav')
# pygame.mixer.music.play()


# Rectangle
j1 = raw_input("entrer le nom du joueur 1 :")
j2 = raw_input("entrer le nom du joueur 2 :")
joueur1 = font2.render(j1, 1, (244, 234, 25))
joueur2 = font2.render(j2, 1, (244, 234, 25))

# boucle infinie permettant de garder la fenetre ouverte
while continuer == True:
    # Analyse de la liste des evenements qui se sont produits
    for event in pygame.event.get():
        # fermeture de la fenetre
        if event.type == QUIT:
            continuer = False
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            posSouris = pygame.mouse.get_pos()
            x_souris = posSouris[0]
            y_souris = posSouris[1]
            print posSouris
            if 525 < x_souris < 680 and 275 < y_souris < 425:
                continuer = False
    pygame.draw.rect(fenetre, (255, 255, 255), (0, 200, 400, 300), 0)
    pygame.draw.rect(fenetre, (0, 0, 0), (0, 0, 800, 229), 0)
    pygame.draw.rect(fenetre, (255, 255, 255), (400, 229, 400, 337), 0)
    fenetre.blit(text, (10, 240))
    fenetre.blit(text2, (10, 360))
    fenetre.blit(joueur1, (30, 280))
    fenetre.blit(joueur2, (30, 400))
    fenetre.blit(button, button_rect)
    pygame.display.flip()
print "sortie"


while continuer_jeu == True:
    for event in pygame.event.get():
        # fermeture de la fenetre
        if event.type == QUIT:
            continuer_jeu = False
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            posSouris2 = pygame.mouse.get_pos()
            x_souris2 = posSouris2[0]
            y_souris2 = posSouris2[1]
            print posSouris2
            if 750 < x_souris2 < 800 and 450 < y_souris2 < 500:
                continuer_jeu = False
    pygame.draw.rect(fenetre, (0, 0, 0), (0, 800, 0, 500), 0)
    fenetre.blit(fond, (0, 0))
    pygame.draw.rect(fenetre, (255, 255, 255), (75, 150, 250, 260), 0)
    pygame.draw.rect(fenetre, (255, 255, 255), (475, 150, 250, 260), 0)
    pygame.draw.rect(fenetre, (0, 0, 0), (480, 155, 240, 250), 0)
    pygame.draw.rect(fenetre, (0, 0, 0), (80, 155, 240, 250), 0)
    fenetre.blit(text3, (95, 20))
    fenetre.blit(text4, (485, 20))
    fenetre.blit(joueur1, (274, 25))
    fenetre.blit(joueur2, (670, 25))
    fenetre.blit(niveau1, (80, 155))
    fenetre.blit(niveau2, (80, 180))
    fenetre.blit(niveau3, (80, 205))
    fenetre.blit(niveau4, (80, 230))
    fenetre.blit(niveau5, (80, 255))
    fenetre.blit(niveau6, (80, 280))
    fenetre.blit(niveau7, (80, 305))
    fenetre.blit(niveau8, (80, 330))
    fenetre.blit(niveau9, (80, 355))
    fenetre.blit(niveau10, (80, 380))
    fenetre.blit(joueur1, (274, 25))
    fenetre.blit(joueur2, (670, 25))
    fenetre.blit(niveau1, (480, 155))
    fenetre.blit(niveau2, (480, 180))
    fenetre.blit(niveau3, (480, 205))
    fenetre.blit(niveau4, (480, 230))
    fenetre.blit(niveau5, (480, 255))
    fenetre.blit(niveau6, (480, 280))
    fenetre.blit(niveau7, (480, 305))
    fenetre.blit(niveau8, (480, 330))
    fenetre.blit(niveau9, (480, 355))
    fenetre.blit(niveau10, (480, 380))
    fenetre.blit(button2, button2_rect)
    pygame.display.flip()
print "sortie"

while continuer_fin == True:
    for event in pygame.event.get():
        # fermeture de la fenetre
        if event.type == QUIT:
            continuer_jeu = False
    fenetre.blit(fond2, (0, 0))
    fenetre.blit(text5, (100, 0))
    pygame.display.flip()
