import gtk


def addition(widget):
    global entree_nb1, entree_nb2, resultat
    nb1 = entree_nb1.get_text()
    nb2 = entree_nb2.get_text()
    if nb1 == "" or nb2 == "":
        resultat.set_text("entrer 2 nombres valides")
    else:
        nb1 = float(nb1)
        nb2 = float(nb2)
        somme = str(nb1 + nb2)
        resultat.set_text(somme)

def soustraction(widget):
    global entree_nb1, entree_nb2, resultat
    nb1 = entree_nb1.get_text()
    nb2 = entree_nb2.get_text()
    if nb1 == "" or nb2 == "":
        resultat.set_text("entrer 2 nombres valides")
    else:
        nb1 = float(nb1)
        nb2 = float(nb2)
        somme = str(nb1 - nb2)
        resultat.set_text(somme)

def division(widget):
    global entree_nb1, entree_nb2, resultat
    nb1 = entree_nb1.get_text()
    nb2 = entree_nb2.get_text()
    if nb1 == "" or nb2 == "":
        resultat.set_text("entrer 2 nombres valides")
    else:
        nb1 = float(nb1)
        nb2 = float(nb2)
        if nb2 == 0:
            resultat.set_text("impossible de diviser par zero")
        else:
            somme = str(nb1 + nb2)
            resultat.set_text(somme)
            quotient = str(nb1 / nb2)
            resultat.set_text(quotient)

def multiplication(widget):
    global entree_nb1, entree_nb2, resultat
    nb1 = entree_nb1.get_text()
    nb2 = entree_nb2.get_text()
    if nb1 == "" or nb2 == "":
        resultat.set_text("entrer 2 nombres valides")
    else:
        nb1 = float(nb1)
        nb2 = float(nb2)
        produit = str(nb1 * nb2)
        resultat.set_text(produit)

def suppression(widget):
    global entree_nb1, entree_nb2, resultat
    entree_nb1.set_text(" ")
    entree_nb2.set_text(" ")
    resultat.set_text(" ")

"""Interface graphique avec glade """
interface = gtk.Builder()

interface.add_from_file("interfacecalc.glade")
#connection de la fenetre
fenetre = interface.get_object("fenetre")
fenetre.connect("delete_event", gtk.main_quit)
fenetre.set_title("Calculatrice_ISN")
fenetre.set_icon_from_file("calc.png")

#connection des entrees de texte
entree_nb1 = interface.get_object("entry1")
entree_nb2 = interface.get_object("entry2")

#connection des boutons operateurs
plus = interface.get_object("plus")
plus.connect("clicked", addition)
moins = interface.get_object("moins")
moins.connect("clicked", soustraction)
diviser = interface.get_object("divise")
diviser.connect("clicked", division)
times = interface.get_object("fois")
times.connect("clicked", multiplication)

#connection du bouton supprimer
supprimer = interface.get_object("suppr")
supprimer.connect("clicked", suppression)

#connection de l'affichage du resultat
resultat = interface.get_object("resultat")



fenetre.show_all()
gtk.main()
