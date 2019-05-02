import gtk

def When_button_calc_is_clicked(widget):
	global entree_ray, message_fin
	rayon = int(entree_ray.get_text())
	aire = 3.14*rayon*rayon
	textmessage = str(aire)
	message_fin.set_markup("<b><big><big><big>" + textmessage + "</big></big></big></b>")


interface = gtk.Builder()

interface.add_from_file("interfacaire.glade")

fenetre = interface.get_object("fenetre")

fenetre.connect("delete-event", gtk.main_quit)


bouton_calc = interface.get_object("bouton")
bouton_calc.connect("clicked", When_button_calc_is_clicked)

entree_ray = interface.get_object('entree')

label_ray = interface.get_object('label')

message_fin = interface.get_object('message')

fenetre.show_all()
gtk.main()
