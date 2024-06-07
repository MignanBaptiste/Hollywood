import json
import networkx as nx
import itertools
import random as rand

# Q1
def json_vers_nx(chemin):
    """Charge un fichier de liste de film en format json pour en faire un graphe.

    Args:
        chemin (String): Chemin menant au fichier contenant la liste de film.

    Returns:
        graphe : Graphe avec pour sommets, les acteurs et s'ils ont déjà jouer dans un film ensemble en arêtes.
    
    Complexité:
        O(N**6)
    """
    graph = nx.Graph()
    with open(chemin, "r") as file:
        for ligne in file: # O(N)
            graph.add_edges_from(itertools.combinations([acteur.strip("[").strip("]") for acteur in json.loads(ligne)["cast"]], 2)) # O(N**5)
    return graph

# Q2
# Temps inférieur à 0.05 secondes
def collaborateurs_communs(graph, u, v):
    """Renvoie un ensemble contenant tous les collaborateurs communs des sommets u et v.

    Args:
        graph (graphe): Graphe contenant les acteurs et leurs connexions entre eux.
        u (String): Acteur 1.
        v (String): Acteur 2.

    Returns:
        set: Ensemble des collaborateurs communs de u et v.
    
    Complexité:
        O(N**2)
    """
    commun = set()
    for voisin in graph.adj[v]: # O(N)
        if voisin in graph.adj[u]: # O(N)
            commun.add(voisin)
    return commun

#Q3
def collaborateurs_proches(G,u,k):
    """Fonction renvoyant l'ensemble des acteurs à distance au plus k de l'acteur u dans le graphe G. La fonction renvoie None si u est absent du graphe.
    
    Parametres:
        G: le graphe
        u: le sommet de départ
        k: la distance depuis u
    
    Complexité:
        O(N**4)
    """
    if u not in G.nodes: # O(N)
        print(u,"est un illustre inconnu")
        return None
    collaborateurs = set()
    collaborateurs.add(u)
    for i in range(k): # O(N)
        collaborateurs_directs = set()
        for c in collaborateurs: # O(N)
            for voisin in G.adj[c]: # O(N)
                if voisin not in collaborateurs: # O(N)
                    collaborateurs_directs.add(voisin)
        collaborateurs = collaborateurs.union(collaborateurs_directs)
    collaborateurs.remove(u)
    return collaborateurs
# On reconnait un algorithme de parcours DFS car on parcours l'ensemble des sommets voisins d'une distance inférieur à k.

def est_proche(G,u,v,k=1):
    """_summary_

    Args:
        graph (graphe): Graphe contenant les acteurs et leurs connexions entre eux.
        u (String): Acteur 1.
        v (String): Acteur 2.
        k (int, optional): Distance maximal de proximité entre les deux sommets. Defaults to 1.

    Returns:
        boolean: True si u et v sont séparé par une distance inférieur ou égale à k.
    
    Complexité:
        O(N**4)
    """
    return v in collaborateurs_proches(G,u,k) # O(N**4)

def distance_naive(G,u,v): # O(N**6)
    """Renvoie la distance entre 2 acteurs d'un manière inefficace.

    Args:
        G (graphe): Graphe contenant les acteurs et leurs connexions entre eux.
        u (String): Acteur 1.
        v (String): Acteur 2.

    Returns:
        int: Distance entre l'acteur u et l'acteur v.
    
    Complexité:
        O(N**6)
    """
    if u == v:
        return 0
    for k in range(nx.number_of_nodes(G)): # O(N)
        if est_proche(G,u,v,k): # O(N**5)
            return k
    return None

def distance(G,u,v):
    """Fonction renvoyant la distance entre u et v de manière très efficace en utilisant une fonction de networkx.
    Fonction énormément de temps à être éxécuter, boucle trop longue.

    Args:
        G (graphe): Graphe contenant les acteurs et leurs connexions entre eux.
        u (String): Acteur 1.
        v (String): Acteur 2.

    Returns:
        int: Distance entre l'acteur u et l'acteur v.
    
    Complexité:
        O(N**3)
    """
    if u not in G.nodes:
        return None
    collaborateurs = set()
    collaborateurs.add(u)
    if u == v:
        return 0
    for k in range(nx.number_of_nodes(G)): # O(N)
        collaborateurs_directs = set()
        for c in collaborateurs: # O(N)
            for voisin in G.adj[c]: # O(N)
                if voisin not in collaborateurs: # O(1)
                    collaborateurs_directs.add(voisin)
        collaborateurs = collaborateurs.union(collaborateurs_directs)
        if v in collaborateurs:
            return k + 1

def distance2(G,u,v):
    """Fonction renvoyant la distance entre u et v de manière très efficace en utilisant une fonction de networkx.
    Fonction énormément de temps à être éxécuter, tant que v n'est pas dans les collaborateurs, la fonction ne s'arête pas.

    Args:
        G (graphe): Graphe contenant les acteurs et leurs connexions entre eux.
        u (String): Acteur 1.
        v (String): Acteur 2.

    Returns:
        int: Distance entre l'acteur u et l'acteur v.
    
    Complexité:
        O(N**3)
    """
    if u not in G.nodes or v not in G.nodes:
        return None
    collaborateurs = set()
    collaborateurs.add(u)
    distance = 0
    while v not in collaborateurs: # O(N)
        distance += 1
        collaborateurs_directs = set()
        for c in collaborateurs: # O(N)
            for voisin in G.adj[c]: # O(N)
                if voisin not in collaborateurs: # O(1)
                    collaborateurs_directs.add(voisin)
        collaborateurs = collaborateurs.union(collaborateurs_directs)
    return distance

def distance3(G, u, v):
    """Fonction renvoyant la distance entre u et v de manière très efficace en utilisant une fonction de networkx.
    La fonction la plus efficace pour l'utilisation que l'on en fait.

    Args:
        G (graphe): Graphe contenant les acteurs et leurs connexions entre eux.
        u (String): Acteur 1.
        v (String): Acteur 2.

    Returns:
        int: Distance entre l'acteur u et l'acteur v.
    
    Complexité:
        Estimation = pas beaucoup, O(N) ?.
    """
    try:
        return nx.shortest_path_length(G, u, v) # Fonction renvoyant le plus court chemin entre deux sommets du module networkx.
    except nx.NetworkXNoPath: # S'il n'y a pas de chemin reliant u et v, alors l'exception est levé.
        return None

def distance4(G, u, v): # Ne surtout pas utiliser
    """Fonction renvoyant la distance entre u et v de manière très efficace en utilisant une fonction de networkx.
    Fonction énormément de temps à être éxécuter.

    Args:
        G (graphe): Graphe contenant les acteurs et leurs connexions entre eux.
        u (String): Acteur 1.
        v (String): Acteur 2.

    Returns:
        int: Distance entre l'acteur u et l'acteur v.
    
    Complexité:
        O(N**4)
    """
    if u == v:
        return 0
    if u not in G.nodes():
        return None
    dico = dict()
    current = [u]
    i = 0
    while v not in dico: # O(N)
        suivant = set()
        for node in current: # O(N)
            if node not in dico: # O(1)
                dico[node] = i
                for voisin in G.adj[node]: # O(N)
                    if voisin not in dico and voisin not in current:  # O(N)
                        suivant.add(voisin)
        current = list(suivant)
    return dico[v]

# Q4
def centralite(G,u): # Trop longue (~ 5 minutes)
    """Fonction renvoyant la centralité d'un acteur dans le graphe, plus la valeur renvoyé est basse, plus il se rapproche du centre du graphe.
    Fonctionne mais n'est pas optimisé, prend trop de temps pour ce qui est demandé.

    Args:
        G (graphe): Graphe contenant les acteurs et leurs connexions entre eux.
        u (String): Acteur.

    Returns:
        int: Distance entre l'acteur u et l'acteur le plus éloigné du graphe.
    
    Complexité:
        O(N**2)
    """
    def critere(node):
        distance = distance3(G, u, node) # O(N)
        if distance is None:
            return 0
        else:
            return distance
    return distance3(G, u, max(G.nodes, key = critere)) # O(N)

def centralite2(G, u):
    """Fonction renvoyant la centralité d'un acteur dans le graphe, plus la valeur renvoyé est basse, plus il se rapproche du centre du graphe. 

    Args:
        G (graphe): Graphe contenant les acteurs et leurs connexions entre eux.
        u (String): Acteur.

    Returns:
        tuple(int, acteur): Tuple de distance entre l'acteur u et l'acteur le plus éloigné du graphe.
    
    Complexité:
        O(N**3)
    """
    if u not in G.nodes:
        return None
    collaborateurs = set()
    collaborateurs.add(u)
    distance = 0
    collaborateurs_directs = G.adj[u]
    old = collaborateurs_directs
    while collaborateurs_directs != set(): # O(N)
        collaborateurs = collaborateurs.union(collaborateurs_directs)
        distance += 1
        temp = set()
        for c in collaborateurs_directs: # O(N)
            for voisin in G.adj[c]: # O(N)
                if voisin not in collaborateurs: # O(1)
                    temp.add(voisin)
        old = collaborateurs_directs
        collaborateurs_directs = temp
        if collaborateurs_directs == set():
            return (distance, rand.choice(list(old)))
    return (distance, rand.choice(list(old)))

def centre_hollywood(G): # Excèssivement longue (en années pour data)
    """Renvoie l'acteur au centre du graphe, l'acteur qui est le plus proches de tous les autres sommets.
    Fonction prennant un quantité de temps astronomique car éxécute centralite2 sur tous les sommets de G. 

    Args:
        G (graphe): Graphe contenant les acteurs et leurs connexions entre eux.

    Returns:
        String: L'acteur le plus proche du centre du graphe.
    
    Complexité:
        O(N**4)
    """
    def critere(u):
        return centralite2(G, u) # O(N**3)
    return min(G.nodes(), key=critere) # O(N)

def centre_hollywood2(G):
    """Renvoie l'acteur ou l'un des acteurs s'il y en a plusieurs, au centre du graphe, l'acteur qui est le plus proches de tous les autres sommets.

    Args:
        G (graphe): Graphe contenant les acteurs et leurs connexions entre eux.

    Returns:
        String: L'acteur/ un des acteurs le plus proche du centre du graphe.

    Complexité:
        O(N**9) Absolument pas représentatif du temps réel pris par la fonction.
    """
    u = centralite2(G, rand.choice(list(G.nodes()))) # O(N**3)
    v = centralite2(G, u[1]) # O(N**3)
    index = v[0]//2
    
    for acteur1 in collaborateurs_proches(G, u[1], index): # O(N)
        for acteur2 in collaborateurs_proches(G, v[1], index): # O(N)
            if est_proche(G, acteur1, acteur2, 1): # O(N**4)
                if centralite2(G, acteur2)[0] < centralite2(G, acteur1)[0]: # O(N**3)
                    return acteur2
                else:
                    return acteur1

# Q5
def eloignement_max(G:nx.Graph):
    """Renvoie la distance maximal entre les acteurs les plus éloignés du graphe.
    Fonction non optimisé car elle éxécute la fonction distance3 sur l'ensemble des sommets du graphe.
    Ne renvoie pas le bon résultat car on ne calcul pas la distance entre les deux bords du graphe.

    Args:
        G (graphe): Graphe contenant les acteurs et leurs connexions entre eux.

    Returns:
        int: La distance entre les deux acteurs les plus éloignés dans le graphe.
    
    Complexité:
        O(N**6)
    """
    u = rand.choice(list(G.nodes()))
    def critere(node):
        distance = distance3(G, u, node) # O(N)
        if distance is None:
            return 0
        else:
            return distance
    return centralite2(G, max(G.nodes, key = critere)) # O(N**5)

def eloignement_max2(G):
    """Renvoie la distance maximal entre les acteurs les plus éloignés du graphe.
    Corrige les problèmes de la première fonction.

    Args:
        G (graphe): Graphe contenant les acteurs et leurs connexions entre eux.

    Returns:
        int: La distance entre les deux acteurs les plus éloignés dans le graphe.

    Complexité:
        O(N**6)
    """
    return centralite2(G, centralite2(G, rand.choice(list(G.nodes())))[1])[0] # O(N**6)
# Bonus
def centralite_groupe(G,S):
    """Fonction non réalisé, non fonctionnel"""
    return None