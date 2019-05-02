# recuperation de donnees provenant d'une carte
#affichage dans pygame
import pygame
from pygame.locals import *
from serial import *

#creation du port com
ser=Serial(port="COM11", baudrate=9600, timeout=1)
compteur=0  #variable compteur pour suivre le nombre d'envois

# Declaration des fonctions

def recupdonnees():
	global donnees,compteur
	if ser.isOpen():  # on lit caractere apres caractere jusqu'a recevoir caractere de fin de phrase
		messageinitial = ser.readline()  #reception du message
		donnees=messageinitial.rstrip('\r\n') #on elimine les caracteres de fin de phrase
		#permet de compter le nombre de valeurs recues
		compteur=compteur+1


def traiter_evenement():
	global continuer
	# on traite chaque evenement genere par pygame
	for event in pygame.event.get():
		# si on clique sur la croix de la fenetre ==> arret du jeu
		if event.type == pygame.QUIT:
			continuer = False
			print('fin')


# affichage du jeu avec pygame
def dessiner():
	global donnees
	VIOLET=(200,150,217)
	NOIR=(0,0,0)
	fond=pygame.Surface(screen.get_size())
	fond.fill((0,0,0))
	screen.blit(fond, (0,0))
	mapolice=pygame.font.SysFont("Arial",20)
	#SysFont (nom, taille, gras = False, italic = False)
	message="compteur = "+str(compteur)
	texte=mapolice.render(message,1,VIOLET)
	screen.blit(texte,(10,10))
	message2="nombre aleatoire recupere ="+donnees
	texte2=mapolice.render(message2,1,VIOLET)
	screen.blit(texte2,(10,30))



#################################################################
#######     INITIALISATION PYGAME        ########################
#################################################################

# initialisation pygame
pygame.init()
SIZE =(LARGEUR,HAUTEUR)= (700, 500)
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("transmission de donnees des cartes vers pygame")



# on creer une horloge pour reguler la vitesse de la boucle de jeu
clock = pygame.time.Clock()

# -------- Boucle principale -----------
# tant que le jeu n'est pas fini
continuer = 1
oldtemps=pygame.time.get_ticks()  #variable pour mesurer le temps ici t0 (optionnel)

while continuer == True :
    # --- on traite les evenements
	traiter_evenement()

    # ----on recupere les donnes du port COM
	recupdonnees()
    # --- on dessine le jeu
	dessiner()
    # on inverse les affichages (double buffering)
	pygame.display.flip()

 	#----mesure de delta entre chaque envoi---suivi sur console python
	newtemps=pygame.time.get_ticks()    #variable t instant mesure
	delai=newtemps-oldtemps             # delai=t-t0
	oldtemps=newtemps                    #t0 prend la valeur de t
	print ("delai en ms =",delai,"ms")
	#-----------------------------------------------
#-------------------info sur la vitesse de transmission-----------------------
	# si fps a un delai plus long que la vitesse d'envoi, c'est lui qui impose
	#si pas de fps, le delai entre chaque mesure est impose par la vitesse d'envoi
#--------------------------------------------------------------------------------
	clock.tick(100)  # reglage du fps

# -------- Fin Boucle principale -----------

pygame.quit()
ser.close()   #on ferme le port COM
