from tkinter import *
import requetes as r
import networkx as nx
import random as rand
import matplotlib.pyplot as plt

G = r.json_vers_nx("data.txt")

appli = Tk()
appli.title("SAE Graph")
appli.configure(width=1000)
appli.configure(height=800)
text = Label(appli, text="")
text.place(x=550, y=82)

def boutonCentralite():
    if acteur1.get() in G.nodes:
        text.configure(text=r.centralite2(G, acteur1.get())[0])

def boutonCentreHollywood():
    text.configure(text=r.centre_hollywood2(G))

def distanceCollab():
    if acteur1.get() in G.nodes and acteur2.get() in G.nodes:
        text.configure(text=r.distance3(G, acteur1.get(), acteur2.get()))

def collaborateurs_commun():
    if acteur1.get() in G.nodes and acteur2.get() in G.nodes:
        communs = r.collaborateurs_communs(G, acteur1.get(), acteur2.get())
        graphe = nx.Graph()
        for acteurs in communs:
            graphe.add_edge(acteur1.get(), acteurs)
            graphe.add_edge(acteur2.get(), acteurs)
            for acteur in communs:
                if acteur in G.adj[acteurs]:
                    graphe.add_edge(acteur, acteurs)
        fig = plt.figure()
        nx.draw(graphe)
        fig.savefig("GrapheCommun.png")

def collaborateurs_proches():
    if acteur1.get() in G.nodes:
        graphe = nx.Graph()
        proches = r.collaborateurs_proches(G,acteur1.get(),1)
        for acteur in proches:
            graphe.add_edge(acteur, acteur1.get())
        fig = plt.figure()
        nx.draw(graphe)
        fig.savefig("GrapheProches.png")

def eloignement_max():
    text.config(text=r.eloignement_max2(G))

def temp_text1(e):
   acteur1.delete(0,"end")

def temp_text2(e):
   acteur2.delete(0,"end")

taille_bouton = 20
bouton_centralite = Button(appli, text="Centralité", command=boutonCentralite)
bouton_centralite.config(width=taille_bouton)
bouton_centralite.place(x=50, y=140)

acteur1 = Entry(appli, textvariable=StringVar())
acteur1.insert(0, "acteur 1")
acteur1.pack(pady=20)
acteur1.bind("<FocusIn>", temp_text1)
acteur1.place(x=50, y=83)

acteur2 = Entry(appli, textvariable=StringVar())
acteur2.insert(0, "acteur 2")
acteur2.bind("<FocusIn>", temp_text2)
acteur2.place(x=200, y=83)

centre_hollywood = Button(appli, text="Centre de Hollywood", command=boutonCentreHollywood)
centre_hollywood.config(width=taille_bouton)
centre_hollywood.place(x=50, y=170)

distance_collaborateur = Button(appli, text="Distance", command=distanceCollab)
distance_collaborateur.config(width=taille_bouton)
distance_collaborateur.place(x=50, y=200)

bouton_collaborateurs_commun =Button(appli, text="Collaborateurs communs", command=collaborateurs_commun)
bouton_collaborateurs_commun.config(width=taille_bouton)
bouton_collaborateurs_commun.place(x=50, y=230)


bouton_collaborateurs_proches = Button(appli, text="Collaborateurs proches", command=collaborateurs_proches)
bouton_collaborateurs_proches.config(width=taille_bouton)
bouton_collaborateurs_proches.place(x=50, y=260)

bouton_eloignement_max = Button(appli, text="Eloignement max", command=eloignement_max)
bouton_eloignement_max.config(width=taille_bouton)
bouton_eloignement_max.place(x=50, y=290)

appli.mainloop()