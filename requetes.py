import json
import networkx as nx
import itertools
# Q1
def json_vers_nx(chemin):
    graph = nx.Graph()
    with open(chemin, "r") as file:
        for ligne in file:
            graph.add_edges_from(itertools.combinations([acteur.strip("[").strip("]") for acteur in json.loads(ligne)["cast"]], 2))
    return graph

# Q2
# Temps inférieur à 0.05 secondes
def collaborateurs_communs(graph, acteur1, acteur2):
    commun = []
    for v in list(graph.adj[acteur2]):
        if v in list(graph.adj[acteur1]):
            commun.append(v)
    return commun