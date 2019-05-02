#deplacer un personnage avec des fleches en utilisant les rect()
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

persorect=perso.get_rect()
persorect.center=(LARGEUR/2,HAUTEUR/2)


# Boucle infinie
continuer = True
#--------------- maintien des touches-----------
pygame.key.set_repeat(5,2)

while continuer == True:
#---------gestion des evenements--------------
	for event in pygame.event.get():
		if event.type == QUIT:
			continuer = False
		if event.type==KEYDOWN:
			if event.key==K_DOWN:
				persorect=persorect.move(0,2)
			if event.key==K_UP:
				persorect=persorect.move(0,-2)
			if event.key==K_LEFT:
				persorect=persorect.move(-2,0)
			if event.key==K_RIGHT:
				persorect=persorect.move(2,0)
#------------gestion de l'evolution----------------
		if persorect.top<=0:
			persorect.top=0
		if persorect.bottom>=HAUTEUR:
			persorect.bottom=HAUTEUR
		if persorect.left<=0:
			persorect.left=0
		if persorect.right>=LARGEUR:
			persorect.right=LARGEUR
#----------affichage--------------------
	fenetre.blit(fond, (0, 0))
	fenetre.blit(perso,persorect)
	pygame.display.flip()
	

pygame.quit()
