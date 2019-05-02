montant=input("Entrer le total: ")
if montant>100:
    montant=0.9*montant
    print"Le montant reduit est de", montant, "euros"
else:
    print"Le montant est toujours de", montant, "euros"
