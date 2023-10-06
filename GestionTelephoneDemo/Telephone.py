import tkinter
from logging import info
from tkinter import ttk
from tkinter import *
from tkinter import messagebox





# Crée la fenêtre principale
fenetre = Tk()
fenetre.title("LE PHONE DE DRO77 24/24 7/7")
#fenetre.geometry("1300x700+20+10")
fenetre.configure(background = "#4dacf9")

frame = tkinter.Frame(fenetre)
frame.pack()

# Crée les étiquettes et les champs de saisie

info_telephone_frame = tkinter.LabelFrame(frame, text = "INFORMATION SUR LE TELEPHONE", font = ("Arial", 15))
info_telephone_frame.grid(row = 0, column=0, padx=20, pady=20)

lblMarque = tkinter.Label(info_telephone_frame, text = " Marque du téléphone :", font = ("Arial", 14))
lblMarque.grid(row = 0, column=0)
txtMarque = tkinter.Entry(info_telephone_frame, font = ("Arial", 12))
txtMarque.grid(row = 1, column=0)

lblElements6 = tkinter.Label(info_telephone_frame, text = " 6 eme élements:", font = ("Arial", 14))
lblElements6.grid(row = 0, column=1)
txtElements6= tkinter.Entry(info_telephone_frame, font = ("Arial", 12))
txtElements6.grid(row = 1, column=1)

lblModel = tkinter.Label(info_telephone_frame, text = " Model du téléphone :", font = ("Arial", 14))
lblModel.grid(row = 2, column=0)
txtMarque = tkinter.Entry(info_telephone_frame, font = ("Arial", 12))
txtMarque.grid(row = 3, column=0)

lblPrix  = tkinter.Label(info_telephone_frame, text = " Prix du téléphone :", font = ("Arial", 14))
lblPrix.grid(row=4, column=0)
txtMarque = tkinter.Entry(info_telephone_frame, font = ("Arial", 12))
txtMarque.grid(row = 5, column=0)

lblQuantite  = tkinter.Label(info_telephone_frame, text = " Couleur du téléphone :", font = ("Arial", 14))
lblQuantite.grid(row=6, column=0)
txtMarque = tkinter.Entry(info_telephone_frame, font = ("Arial", 12))
txtMarque.grid(row = 7, column=0)

lblCouleur  = tkinter.Label(info_telephone_frame, text = " Taille du téléphone :", font = ("Arial", 14))
lblCouleur.grid(row=8, column=0)
txtMarque = tkinter.Entry(info_telephone_frame, font = ("Arial", 12))
txtMarque.grid(row = 9, column=0)




btnEnregistrer = tkinter.Button(info_telephone_frame, text = "Enregistrer", width=20,bg="#373d84",fg="#fdffee", font  = ("Arial", 14))
btnEnregistrer.grid(row=10, column=0)

btnModifier = tkinter.Button(info_telephone_frame, text = "Modifier", font  = ("Arial", 14), width=20)
btnModifier.grid(row=11, column=0)

btnSupprimer = tkinter.Button(info_telephone_frame, text = "Supprimer", font  = ("Arial", 14), width=20)
btnSupprimer.grid(row=12, column=0)

for composant in info_telephone_frame.winfo_children():
    composant.grid_configure(padx=10, pady=5)


table_telephone_frame = tkinter.LabelFrame(frame, text = "TABLE DE GESTION DE MES TELEPHONES", font = ("Arial", 15))
table_telephone_frame.grid(row = 0, column=1,sticky="news", padx=20, pady=20)

#Table
table = ttk.Treeview(table_telephone_frame, columns = (1, 2, 3, 4, 5, 6), height = 5, show = "headings")
#table.place(x = 600,y = 150, width = 760, height = 450)
table.grid(row=0, column=0)
#Entete
table.heading(1 , text = "CODE")
table.heading(2 , text = "MARQUE")
table.heading(3 , text = "MODEL")
table.heading(4 , text = "PRIX")
table.heading(5 , text = "QUANTITE")
table.heading(6 , text = "COULEUR")

#definir les dimentions des colonnes
table.column(1,width = 50)
table.column(2,width = 150)
table.column(3,width = 150)
table.column(4,width = 50)
table.column(5,width = 150)
table.column(6,width = 100)

# Crée le bouton d'enregistrement


# Lance la boucle principale de l'interface
fenetre.mainloop()







