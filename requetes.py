import json
import networkx as nx
import itertools
# Q1
def json_vers_nx(chemin):
    graph = nx.Graph()
    with open(chemin, "r") as file:
        for ligne in file:
            acteurs = json.loads(ligne)["cast"]
            acteurs = [acteur.strip("[").strip("]") for acteur in acteurs]
            graph.add_edges_from(itertools.combinations(acteurs, 2))
    return graph
