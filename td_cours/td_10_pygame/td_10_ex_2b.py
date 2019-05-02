import pygame
from pygame.locals import *


# Declaration des fonctions

# evolution du jeu
def evoluer():
    global dt, vx, vy, ax, ay, x, y
    vx=vx+ax*dt
    vy=vy+ay*dt
    x=x+vx*dt
    y=y+vy*dt
    if y<=0:
        vy=-vy


# affichage du jeu avec pygame
def dessiner():
    global x2, y2, img
    x2,y2 = change_repere(x,y)
    screen.blit(fond, (0,0))
    pygame.draw.ellipse(screen,(255,255,255),(x2,y2,10,10))



def traiter_evenement():
    global vy, continuer, x, g, fond, ay
        # on traite chaque evenement genere par pygame
    for event in pygame.event.get():
                # si on clique sur la croix de la fenetre ==> arret du jeu
        if event.type == pygame.QUIT:
            continuer = False
            print('fin')
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                vy= vy+20
            if event.key ==K_t:
                fond = pygame.image.load("sol_terre.jpg")

            if event.key ==K_j:
                fond = pygame.image.load("sol_jupiter2.jpg")
                ay = 2.53 * g

            if event.key ==K_m:
                fond = pygame.image.load("sol_martien.jpg")
                ay = g * 0.38

            if event.key ==K_s:
                fond = pygame.image.load("sol_soleil.jpg")
                ay = g*27.96


        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if x>=20:
                    x=x-20
            if event.button == 3:
                if x<=680:
                    x=x+20





def change_repere(x1,y1) :
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
dt = 0.1
g= -10
#fond
fond = pygame.image.load("sol_terre.jpg")
# position initiale de la balle
x = 350

y = 400
# vitesse initiale de la balle
vx= 0
vy=0
# definition de l'acceleration (gravite uniquement)
ax=0
ay=g


# on creer une horloge pour reguler la vitesse de la boucle de jeu
clock = pygame.time.Clock()

# -------- Boucle principale -----------
# tant que le jeu n'est pas fini
continuer = 1
while continuer == True :
    # --- on traite les evenements
    traiter_evenement()

    # --- on fait evoluer le jeu
    evoluer()


    # --- on dessine le jeu
    dessiner()
    # on inverse les affichages (double buffering)
    pygame.display.flip()


    # --- on demande d'attendre ce qu'il faut pour un FPS de 60
    clock.tick(60)
# -------- Fin Boucle principale -----------

pygame.quit()
