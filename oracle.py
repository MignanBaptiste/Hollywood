from tkinter import *
import requetes as r
import networkx as nx

G = None

appli = Tk()
appli.title("SAE Graph")
appli.configure(width=1000)
appli.configure(height=800)

text = Label(appli, text="text")
text.place(x=300, y=50)

def boutonFichier(Graph):
    Graph = r.json_vers_nx("./data_100.txt")

def boutonCentralite():
    text.configure(text=r.centralite2(G, saisie_nom.get()))

def boutonCentreHollywood():
    text.configure(text=r.centre_hollywood2(G))

def distanceCollab():
    text.configure(text=r.distance3(G, "Al Pacino", "Zoe Saldana"))

bouton_quitter = Button(appli, text="json_vers_nx", command=boutonFichier(G))
bouton_quitter.place(x=50, y=50)

bouton_centralite = Button(appli, text="Centralité de :", command=boutonCentralite)
bouton_centralite.place(x=50, y=80)

saisie_nom = Entry(appli, textvariable=StringVar())
saisie_nom.place(x=170, y=83)

centre_hollywood = Button(appli, text="Centre de Hollywood", command=boutonCentreHollywood)
centre_hollywood.place(x=50, y=110)

distance_collaborateur = Button(appli, text="Distance", command=boutonCentreHollywood)

# bouton_centralite = Button(appli, text="valider", command=boutonCentralite)
# bouton_centralite.place(x=50, y=80)

# liste = Listbox(appli)






appli.mainloop()