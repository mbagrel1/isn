import pygame
from pygame.locals import *

LARGEUR = 800
HAUTEUR = 600
l=400
h=300

# Initialisation de la fenetre
pygame.init()
fenetre = pygame.display.set_mode((LARGEUR,HAUTEUR))
pygame.display.set_caption("my first window")

#fond =
fond = pygame.Surface (fenetre.get_size())
fond.fill((189,23,23))

#Import image
img=pygame.image.load("Yoshi.png").convert_alpha()
pygame.key.set_repeat(500, 10)

# Boucle infinie
continuer = True
while continuer == True:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
        if event.type==KEYDOWN:
            if event.key==K_RIGHT:
                if l<=740:
                    l=l+10
            if event.key==K_LEFT:
                if l > 0:
                    l=l-10
            if event.key==K_DOWN:
                if h<=540:
                    h=h+10
            if event.key==K_UP:
                if h > 0:
                    h=h-10

    fenetre.blit(fond, (0,0))
    fenetre.blit(img,(l,h))
    pygame.display.flip()

