import json
import networkx as nx
import itertools
import random as rand

# Q1
def json_vers_nx(chemin):
    graph = nx.Graph()
    with open(chemin, "r") as file:
        for ligne in file:
            graph.add_edges_from(itertools.combinations([acteur.strip("[").strip("]") for acteur in json.loads(ligne)["cast"]], 2))
    return graph

# Q2
# Temps inférieur à 0.05 secondes
def collaborateurs_communs(graph, u, v):
    commun = set()
    for voisin in set(graph.adj[v]):
        if voisin in set(graph.adj[u]):
            commun.add(voisin)
    return commun

#Q3
def collaborateurs_proches(G,u,k):
    """Fonction renvoyant l'ensemble des acteurs à distance au plus k de l'acteur u dans le graphe G. La fonction renvoie None si u est absent du graphe.
    
    Parametres:
        G: le graphe
        u: le sommet de départ
        k: la distance depuis u
    """
    if u not in G.nodes:
        print(u,"est un illustre inconnu")
        return None
    collaborateurs = set()
    collaborateurs.add(u)
    for i in range(k): # O(N**4)
        collaborateurs_directs = set()
        for c in collaborateurs: # O(N**3)
            for voisin in G.adj[c]: # O(N**2)
                if voisin not in collaborateurs: # O(N)
                    collaborateurs_directs.add(voisin)
        collaborateurs = collaborateurs.union(collaborateurs_directs)
    return collaborateurs
# On reconnait un algorithme de parcours DFS car on parcours l'ensemble des sommets voisins d'une distance inférieur à k.

def est_proche(G,u,v,k=1):
    return v in collaborateurs_proches(G,u,k) # O(N**5)

def distance_naive(G,u,v): # O(N**6)
    if u == v:
        return 0
    for k in range(nx.number_of_nodes(G)): # O(N**6)
        if est_proche(G,u,v,k):
            return k
    return None

def distance(G,u,v): # O(N**4)
    if u not in G.nodes:
        return None
    collaborateurs = set()
    collaborateurs.add(u)
    if u == v:
        return 0
    for k in range(nx.number_of_nodes(G)): # O(N**4)
        collaborateurs_directs = set()
        for c in collaborateurs: # O(N**3)
            for voisin in G.adj[c]: # O(N**2)
                if voisin not in collaborateurs: # O(N)
                    collaborateurs_directs.add(voisin)
        collaborateurs = collaborateurs.union(collaborateurs_directs)
        if v in collaborateurs:
            return k + 1

def distance2(G,u,v): # O(N**4)
    if u not in G.nodes:
        return None
    collaborateurs = set()
    collaborateurs.add(u)
    distance = 0
    while v not in collaborateurs:
        distance += 1
        collaborateurs_directs = set()
        for c in collaborateurs:
            for voisin in G.adj[c]:
                if voisin not in collaborateurs:
                    collaborateurs_directs.add(voisin)
        collaborateurs = collaborateurs.union(collaborateurs_directs)
    return distance

def distance3(G, u, v):
    try:
        return nx.shortest_path_length(G, u, v)
    except nx.NetworkXNoPath:
        return None

def distance4(G, u, v): # Ne surtout pas utiliser
    if u == v:
        return 0
    if u not in G.nodes():
        return None
    dico = dict()
    current = [u]
    i = 0
    while v not in dico:
        suivant = set()
        for node in current:
            if node not in dico:
                dico[node] = i
                for voisin in G.adj[node]:
                    if voisin not in dico and voisin not in current:
                        suivant.add(voisin)
        current = list(suivant)
    return dico[v]

# Q4
def centralite(G,u): # Trop longue (~ 5 minutes)
    def critere(node):
        distance = distance3(G, u, node)
        if distance is None:
            return 0
        else:
            return distance
    return distance3(G, u, max(G.nodes, key = critere))

def centralite2(G, u):
    if u not in G.nodes:
        return None
    collaborateurs = set()
    collaborateurs.add(u)
    distance = 0
    collaborateurs_directs = G.adj[u]
    old = collaborateurs_directs
    while collaborateurs_directs != set():
        collaborateurs = collaborateurs.union(collaborateurs_directs)
        distance += 1
        temp = set()
        for c in collaborateurs_directs:
            for voisin in G.adj[c]:
                if voisin not in collaborateurs:
                    temp.add(voisin)
        old = collaborateurs_directs
        collaborateurs_directs = temp
        if collaborateurs_directs == set():
            return (distance, rand.choice(list(old)))
    return (distance, rand.choice(list(old)))

def centre_hollywood(G): # Excèssivement longue (en années pour data)
    def critere(u):
        return centralite2(G, u)
    return min(G.nodes(), key=critere)

def centre_hollywood2(G):
    u = rand.choice(list(G.nodes()))

# Q5
def eloignement_max(G:nx.Graph): # Pas fini
    u = rand.choice(list(G.nodes()))
    def critere(node):
        distance = distance3(G, u, node)
        if distance is None:
            return 0
        else:
            return distance
    return centralite2(G, max(G.nodes, key = critere))

def eloignement_max2(G):
    u = rand.choice(list(G.nodes()))
    return centralite2(G, centralite2(G, u)[1])[0]
# Bonus
def centralite_groupe(G,S):
    return None