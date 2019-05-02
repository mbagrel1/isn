import gtk
from math import sqrt

def When_button_is_clicked(widget):
	global entree_a, entree_b, entree_c, discriminant, solution_1, solution_2
	A = float(entree_a.get_text())
	B = float(entree_b.get_text())
	C = float(entree_c.get_text())
	delta = B*B-4*A*C
	if delta >0:
		x1 ="x =" + str(( -B-sqrt(delta)) / 2 * A)
		x2 ="x =" +str(( -B + sqrt(delta)) / 2 * A)
		solution_1.set_text(x1)
		solution_2.set_text(x2)
		discri = "delta =" + str(delta)
		discriminant.set_text(discri)
	else:
		solution_1.set_text("x = impossible")
		solution_2.set_text("x = impossible ")
		discriminant.set_text(str(delta))



interface = gtk.Builder()

interface.add_from_file("interfacedelta.glade")

fenetre = interface.get_object("fenetre")

fenetre.connect("delete-event", gtk.main_quit)


bouton_val= interface.get_object("bouton")
bouton_val.connect("clicked", When_button_is_clicked)

entree_a= interface.get_object('entreea')
entree_b = interface.get_object('entreeb')
entree_c = interface.get_object('entreec')


discriminant = interface.get_object('discriminant')
solution_1 = interface.get_object('solution 1')
solution_2 = interface.get_object('solution 2')

fenetre.show_all()
gtk.main()


