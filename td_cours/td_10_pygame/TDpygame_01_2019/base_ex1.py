import pygame
from pygame.locals import *

LARGEUR = 200
HAUTEUR = 200
# Initialisation de la fenetre
pygame.init()
fenetre = pygame.display.set_mode((800,600))
pygame.display.set_caption('Jeu pygame')
#fond =

# Boucle infinie
continuer = True
while continuer == True:
	for event in pygame.event.get():
		if event.type == QUIT:
			continuer = False

	#fenetre.blit(fond, (0, 0))
	pygame.display.flip()
