depart=input("Rentrer vos secondes :")
transit=0
heures=depart//3600
transit=depart%3600
minutes=transit//60
secondes=transit%60
print depart, "secondes", "correspond a :", heures, "heures", minutes,"minutes", secondes, "secondes"
