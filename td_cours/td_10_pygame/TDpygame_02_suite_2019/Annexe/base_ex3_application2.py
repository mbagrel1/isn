# faire rebondir un personnage
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
 
#creation du vecteur vitesse
vitesse=[3,2]

# on cree une horloge pour reguler la vitesse de la boucle de jeu
clock = pygame.time.Clock()


# Boucle infinie
continuer = True


while continuer == True:
#---------gestion des evenements--------------
	for event in pygame.event.get():
		if event.type == QUIT:
			continuer = False

#------------gestion de l'evolution----------------
	persorect=persorect.move(vitesse)
	if persorect.right>=LARGEUR or persorect.left<=0:  # si on sort du cadre a gauche ou a droite, on inverse la vitesse suivant x
				vitesse[0]=-vitesse[0]
	if persorect.bottom>=HAUTEUR or persorect.top<=0: # si on sort du cadre en haut ou en bas, on inverse la vitesse suivant y
				vitesse[1]=-vitesse[1]

#----------affichage--------------------
	fenetre.blit(fond, (0, 0))
	fenetre.blit(perso,persorect)
	pygame.display.flip()
	 # --- on demande d'attendre ce qu'il faut pour un FPS de 60 (afficahge max de 100 fois par seconde)
	clock.tick(100)


pygame.quit()
