compteur=0
mdp=raw_input("entrer un mot de passe :")
for i in range (0,2,1):
    while mdp!="esseyhenkor":
        mdp=raw_input("entrer un mot de passe :")
    if mdp=="esseyhenkor":
        print"BIENVENUE"
    else:
        print"ECHEC:cloture de la session"
