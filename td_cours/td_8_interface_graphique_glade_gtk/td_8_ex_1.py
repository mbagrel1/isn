import gtk

def When_button_is_clicked(widget):
	global label_compteur, nb
	nb = nb + 1
	text_label = str(nb)
	label_compteur.set_markup("<b><big><big><big>" + text_label + "</big></big></big></b>")

interface_1 = gtk.Builder()

interface_1.add_from_file("interface.glade")

nom_fenetre = interface_1.get_object("fenetre")

nom_fenetre.connect("delete-event", gtk.main_quit)

bouton_incr = interface_1.get_object("bouton")
bouton_incr.connect("clicked", When_button_is_clicked)

nb = 0
label_compteur = interface_1.get_object("label")

nom_fenetre.show_all()
gtk.main()
