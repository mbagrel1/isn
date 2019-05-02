#interface réalisée avec Tkinter

from Tkinter import *
from dm_isn import impot2017

def calculer_impot2017():
    rimposable = float(stringvar_revenu.get())
    pfiscal = int(stringvar_parts.get())
    impot = impot2017(rimposable, pfiscal)
    texte_a_afficher = "Vous devez payer {} euros d'impots".format(impot)
    label_impots.configure(text=texte_a_afficher)

#interface graphique
fenetre_principale = Tk()

stringvar_revenu = StringVar()
label_revenu = Label(fenetre_principale, text="Votre revenu imposable :")
label_revenu.pack()
champ_revenu = Entry(fenetre_principale, textvariable=stringvar_revenu,
                     width=30)
champ_revenu.pack()

stringvar_parts = StringVar()
label_parts = Label(fenetre_principale,
                    text="Votre nombre de parts de votre foyer fiscal :")
label_parts.pack()
champ_parts = Entry(fenetre_principale, textvariable=stringvar_parts, width=30)
champ_parts.pack()

bouton_valider = Button(fenetre_principale, text="Valider",
                        command=calculer_impot2017)
bouton_valider.pack()

label_impots = Label(fenetre_principale, text="... Entrez les donnees puis cliquez sur valider ...")
label_impots.pack()

fenetre_principale.mainloop()
