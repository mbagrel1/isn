import pygame
from pygame.locals import *

#initialisation
pygame.init()
LARGEUR,HAUTEUR=800,600
fenetre = pygame.display.set_mode((800, 600))

fond = pygame.image.load("background.jpg").convert()

perso = pygame.image.load("perso3.png").convert_alpha()

perso_x = 375
perso_y = 225
speed = 5
xmin = 0
xmax = LARGEUR-50
ymin = 0
ymax = HAUTEUR-50
continuer = True


pygame.key.set_repeat(50,5)
# boucle infinie permettant de garder la fenetre ouverte
while continuer == True:
	# Analyse de la liste des evenements qui se sont produits (au clavier ou a la souris)
	for event in pygame.event.get():
		# fermeture de la fenetre
		if event.type == QUIT:
			continuer = False

		# une touche du clavier a ete enfoncee
		if event.type == KEYDOWN:
			if event.key == K_DOWN:
				if perso_y< ymax :
					perso_y =perso_y + speed
			if event.key == K_UP:
				if perso_y > ymin :
					perso_y =perso_y - speed
			if event.key == K_RIGHT:
				if perso_x < xmax :
					perso_x =perso_x + speed
			if event.key == K_LEFT:
				if perso_x > xmin:
					perso_x =perso_x - speed
	# On redessine le fond et le personnage a sa nouvelle position
	fenetre.blit(fond, (0,0))
	fenetre.blit(perso, (perso_x, perso_y))
	pygame.display.flip()
