import pygame
from pygame.locals import *
continuer=True 
#initialisation
pygame.init()
LARGEUR,HAUTEUR=800,500
fenetre = pygame.display.set_mode((800, 500))


font=pygame.font.SysFont("Arial", 24)
text=font.render("Name of player one:",1,(0,0,0))
text2=font.render("Name of player two:",1,(0,0,0))
titre = pygame.image.load("titre1.JPG").convert_alpha()
#Rectangle



# boucle infinie permettant de garder la fenetre ouverte
while continuer == True:
	# Analyse de la liste des evenements qui se sont produits 
	for event in pygame.event.get():
		# fermeture de la fenetre
		if event.type == QUIT:
			continuer = False
	pygame.draw.rect(fenetre, (255, 255, 255), (0, 200, 400, 300),0)
	pygame.draw.rect(fenetre, (0, 0, 0), (0, 0, 800, 229),0)
	pygame.draw.rect(fenetre, (255, 0, 0), (400, 229, 400, 337),0)
	fenetre.blit(text,(10,240))
	fenetre.blit(text2,(10,360))
	fenetre.blit(titre, (0, 0))
	pygame.display.flip()

