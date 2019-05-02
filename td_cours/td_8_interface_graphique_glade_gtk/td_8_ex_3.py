import gtk

def When_button_is_clicked(widget):
	global essai, message_fin, image, entrer
	mot = essai.get_text()
	if mot == "isn":
		entrer.set_text(" ")
		message_fin.set_text("mdp Valide")
		image.set_from_file("Unlock.png")



interface = gtk.Builder()

interface.add_from_file("interfacemdp.glade")

fenetre = interface.get_object("fenetre")

fenetre.connect("delete-event", gtk.main_quit)


bouton_val = interface.get_object("bouton")
bouton_val.connect("clicked", When_button_is_clicked)

essai= interface.get_object('essai')

entrer = interface.get_object('entrer_mdp')

message_fin = interface.get_object('message')

image = interface.get_object('image')
image.set_from_file('Lock.png')

fenetre.show_all()
gtk.main()

