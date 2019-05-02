import pygame
from pygame.locals import *
from random import randint
LARGEUR = 800
HAUTEUR = 400
vit = 10
# Initialisation de la fenetre
pygame.init()
fenetre = pygame.display.set_mode((LARGEUR,HAUTEUR))
pygame.display.set_caption('Titre de la fenetre')

#chargement du fond ,du personnage
fond =pygame.image.load("background.jpg").convert()
perso=pygame.image.load("perso.png")
persorect=perso.get_rect()

passage =pygame.image.load("teleport.png")
passage1_rect=passage.get_rect()
passage2_rect=passage.get_rect()

persorect.center=(200,200)

police = pygame.font.SysFont("Arial", 20)
label1 = police.render("Monde 1", 1, (255,255,255))
label2 = police.render("Monde 2", 1, (255,255,255))

# Placement au hasard des teleporteurs (en evitant le centre des cadres
coord_ok = False
while coord_ok == False :
	x1,y1 =randint(75,325),randint(75,325)
	x2,y2 =randint(475,725),randint(75,325)
	if 175<x1<225 or 175<y1<225 or 575<x2<625 or 175<y2<225  :
		coord_ok = False
	else :
		coord_ok = True
passage1_rect.center=(x1,y1)
passage2_rect.center=(x2,y2)


#pygame.key.set_repeat(100,1)
clock = pygame.time.Clock()

# le personnage est initalement place dans le cadre 1
monde = 1

# Boucle infinie
continuer = True
while continuer == True:
	for event in pygame.event.get():
		if event.type == QUIT:
			continuer = False
		if event.type==KEYDOWN:
			if event.key==K_LEFT:
				if monde == 1 :
					if persorect.x>50 : persorect=persorect.move(-vit,0)
				else :
					if persorect.x>450 : persorect=persorect.move(-vit,0)
			if event.key==K_RIGHT:
				if monde == 1 :
					if persorect.x<330 : persorect=persorect.move(vit,0)
				else :
					if persorect.x<730 : persorect=persorect.move(vit,0)
			if event.key==K_UP:
				if persorect.y>50 : persorect=persorect.move(0,-vit)
			if event.key==K_DOWN:
				if persorect.y<330 : persorect=persorect.move(0,vit)
			if persorect.colliderect(passage1_rect) :
				monde = 2
				persorect.center=(600,200)
			if persorect.colliderect(passage2_rect) :
				monde = 1
				persorect.center=(200,200)
	fenetre.blit(fond, (0, 0))
	pygame.draw.rect(fenetre, (255,255,255), (50,50,300,300), 0)
	pygame.draw.rect(fenetre, (255,255,255), (450,50,300,300), 0)

	fenetre.blit(label1, (170, 20))
	fenetre.blit(label2, (570, 20))
	fenetre.blit(passage,passage1_rect)
	fenetre.blit(passage,passage2_rect)
	fenetre.blit(perso,persorect)

	clock.tick(60)
	pygame.display.flip()
