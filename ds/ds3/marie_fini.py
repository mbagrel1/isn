import pygame
from pygame.locals import *
from random import randint


#creation de la fenetre

pygame.init()
fenetre = pygame.display.set_mode((800, 400))
fond = pygame.image.load("background.jpg").convert()
pygame.display.set_caption("Teleportation")



#creation du perso et du rect
perso = pygame.image.load("perso.png").convert_alpha()
persorect = perso.get_rect()
persorect.x = 190
persorect.y = 190


#horloge
clock = pygame.time.Clock()
pygame.key.set_repeat(500, 10)




#teleporteurs

coord_ok = False
while coord_ok == False:
	x1, y1 = randint(75, 325),randint(75,325)
	x2,y2 = randint(475, 725), randint(75,325)
	if 175 < x1 < 255 or 175 < y2 < 255 or 175 < y1 < 255 or 575 < x2 < 625:
		coord_ok = False
	else:
		coord_ok = True
		
# rect des teleporteurs	
	
tele = pygame.image.load("teleport.png").convert_alpha()
telerect1 = tele.get_rect()
telerect2 = tele.get_rect()
telerect1.x = x1
telerect1.y = y1
telerect2.x = x2
telerect2.y = y2

#initialisation variable monde
monde = 1

#titre des mondes
police = pygame.font.SysFont("Arial", 20)
label1 = police.render("Monde 1",1,(255, 255, 255))
label2 = police.render("Monde 2",1,(255, 255, 255))

# Boucle infinie
continuer = True

while continuer == True:

#evenements
	for event in pygame.event.get():
		if event.type == QUIT:
			continuer = False

	#deplacement du personnage et contraintes
		if event.type == KEYDOWN:
			if event.key == K_DOWN:
				persorect = persorect.move(0, 10)
				if persorect.y >= 330:
					persorect.y = 330
			if event.key == K_UP:
				persorect = persorect.move(0, -10)
				if persorect.y <= 50:
					persorect.y = 50
			if event.key == K_LEFT:
				persorect = persorect.move(-10, 0)
				if monde == 1:
					if persorect.x <= 50:
						persorect.x = 50
				else: 
					if persorect.x <= 480:
						persorect.x = 480
			if event.key == K_RIGHT:
				persorect = persorect.move(10, 0)
				if monde == 1:
					if persorect.x >= 330:
						persorect.x = 330
				else:
					if persorect.x >= 760:
						persorect.x = 760
					
	#collision avec le teleporteur

	if persorect.colliderect(telerect1):
		persorect.x = 620
		persorect.y = 180
		monde = 2
		
	if persorect.colliderect(telerect2):
		persorect.x = 190
		persorect.y = 190
		monde = 1

	clock.tick(60)
	fenetre.blit(fond, [0,0])
	
	#dessin des carres
	
	pygame.draw.rect(fenetre, (255, 255, 255), (50, 50, 300, 300), 0)
	pygame.draw.rect(fenetre, (255, 255, 255), (480,50, 300, 300), 0)
	
	#blit du texte
	fenetre.blit(label1, [170, 20])
	fenetre.blit(label2, [570, 20])
	
	#blit du perso
	fenetre.blit(perso, persorect)
	
	#blit des teleporteurs
	fenetre.blit(tele, [x1, y1])
	fenetre.blit(tele, [x2, y2])
	

	
	pygame.display.flip()
