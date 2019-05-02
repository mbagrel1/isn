import gtk
uneFenetre = gtk.Window(gtk.WINDOW_TOPLEVEL)
uneFenetre.set_title("oh la belle fenetre")
uneFenetre.set_default_size(640, 480)
uneFenetre.connect("destroy", gtk.main_quit)

unlabel = gtk.Label()
unlabel.set_text("oh le beau label")
uneFenetre.add(unlabel)

uneFenetre.show_all()
gtk.main()
