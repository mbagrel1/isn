import pygame
from pygame.locals import *


# Declaration des fonctions

def change_repere(x1,y1) :  #x2,y2 repre pygame et x1,y1 repere classique
	x2 = x1
	y2 = 500-y1
	return (x2,y2)


#################################################################
#######     INITIALISATION PYGAME        ########################
#################################################################

# initialisation pygame
pygame.init()
SIZE = (700, 500)
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Moteur")
#creation du fond


dt = 0.1
# position initiale de la balle
balle_x = 350
balle_y = 400
# vitesse initiale de la balle
balle_vx= 0
balle_vy=0
# definition de l'acceleration (gravite uniquement)
ax=0
ay=-10


# on creer une horloge pour reguler la vitesse de la boucle de jeu
clock = pygame.time.Clock()

# -------- Boucle principale -----------
# tant que le jeu n'est pas fini
continuer = 1

while continuer == True :
	# on traite chaque evenement genere par pygame
	for event in pygame.event.get():
		# si on clique sur la croix de la fenetre ==> arret du jeu
		if event.type == pygame.QUIT:
			continuer = False
			print('fin')

    # --- on fait evoluer le jeu
	#~ balle_vx=
	#~ balle_vy=
	#~ balle_x=
	#~ balle_y=

    # --- on dessine le jeu
	x2,y2 = change_repere(balle_x,balle_y)
	screen.blit(fond, (0,0))



	# on inverse les affichages (double buffering)
	pygame.display.flip()

    # --- on demande d'attendre ce qu'il faut pour un FPS de 60
	clock.tick(60)
# -------- Fin Boucle principale -----------

pygame.quit()
