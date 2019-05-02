#Ce programme affiche les dix premiers termes de la table de multiplication par 8
print "les dix premiers termes de la table de multiplication par 8 sont :"
print ""
for i in range(10):
	produit = 8*i
	if produit %6 ==0:
		print "8", "*", i, "=", produit, "*"
	else:
		 print "8", "*", i, "=", produit
	
	
