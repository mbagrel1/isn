def table(nombre, debut, fin):
    resultat = 0
    tableur = ""
    for i in range(debut, (fin + 1), 1):
        resultat = nombre * i
        produit = "{} * {} = {}\n".format(nombre, i, resultat)
        i = i + 1
        tableur += produit
    return tableur

def table2(nombre, debut, fin):
    return "\n".join([
        "{} x {} = {}".format(nombre, i, nombre * i)
        for i in range(debut, fin + 1)
    ])

nb = input("quelle table voulez vous : ")
begin = input("a partir de quel nombre ? ")
end = input("jusqu a quel nombre ? ")
print table2(nb, begin, end)