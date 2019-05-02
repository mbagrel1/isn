#detection d'une collision et modification du mouvement
import pygame
from pygame.locals import *

LARGEUR = 800
HAUTEUR = 600
# Initialisation de la fenetre
pygame.init()
fenetre = pygame.display.set_mode((LARGEUR,HAUTEUR))
pygame.display.set_caption('deplacement_personnage')

#chargement du fond ,du personnage et du mur
fond =pygame.image.load("background.jpg")
perso=pygame.image.load("perso.png")

persorect=perso.get_rect()                  # creation d'un objet Rect() de meme taille que le personnage et a la position (0,0)
persorect.center=(LARGEUR/2,HAUTEUR/2)      #positionnement du personnage au centre de l'ecran

mur=pygame.image.load("mur.png")            #chargement de l'image du mur
murrect=mur.get_rect()                      # creation d'un objet Rect() de meme taille que le mur et initialement a la position (0,0)
murrect.x=300                               # on modifie ici la position de l'objet Rect()
murrect.y=200

# copie de l'ancienne position
oldpersorect=persorect.copy()

# Boucle infinie
continuer = True
#--------------- maintien des touches-----------
pygame.key.set_repeat(5,1)

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
#-----------gestion de la collision--------------
	if persorect.colliderect(murrect)==True:
		persorect=oldpersorect
		print"collision"                                    # affichage qui permet de voir dans la console si il y a collision
	else:
		oldpersorect=persorect
		print"deplacement libre"

#----------affichage--------------------
	fenetre.blit(fond, (0, 0))
	fenetre.blit(perso,persorect)
	fenetre.blit(mur,murrect)
	pygame.display.flip()


pygame.quit()
