#base_ex3_a_completer_eleve
import pygame
from pygame.locals import *

LARGEUR = 800
HAUTEUR = 600
# Initialisation de la fenetre
pygame.init()
fenetre = pygame.display.set_mode((LARGEUR,HAUTEUR))
pygame.display.set_caption('deplacement_personnage')

#chargement du fond et du personnage
fond =pygame.image.load("background.jpg")
perso=pygame.image.load("perso.png")

#creation du rect correspondant  au personnage
nouv_rect = Rect(350,300, 50,50)
persorect = perso.get_rect()

# Boucle infinie
continuer = True


while continuer == True:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
        if event.type==KEYDOWN:
            if event.key==K_RIGHT:
                if persorect.right <= 800:
                    persorect.x = persorect.x +10
            if event.key==K_LEFT:
                if persorect.left >= 10:
                    persorect.x = persorect.x -10
            if event.key==K_DOWN:
                if persorect.bottom <=590:
                    persorect.y= persorect.y +10
            if event.key==K_UP:
                if persorect.top >= 10:
                    persorect.y = persorect.y -10


    fenetre.blit(fond, (0, 0))
    fenetre.blit(perso,(0,0))
    fenetre.blit(perso, persorect)


    pygame.display.flip()

pygame.quit()
