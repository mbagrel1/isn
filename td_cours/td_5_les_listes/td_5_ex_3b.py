from random import randint
resultat=[]
for i in range(0,20,1):
    nb=randint(1,6)
    resultat.append(nb)

resultat.sort()

print resultat
