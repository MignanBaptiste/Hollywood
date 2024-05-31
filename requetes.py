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
    for v in set(graph.adj[acteur2]):
        if v in set(graph.adj[acteur1]):
            commun.add(v)
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
    ...

def centre_hollywood(G): # Excèssivement longue (en années pour data)
    def critere(u):
        return centralite(G, u)
    return min(G.nodes(), key=critere)
# Q5
5
def eloignement_max(G:nx.Graph): # Pas fini
    u = rand.choice(list(G.nodes()))
    def critere(node):
        distance = distance3(G, u, node)
        if distance is None:
            return 0
        else:
            return distance
    return centralite(G, max(G.nodes, key = critere))
# Bonus
def centralite_groupe(G,S):
    return None