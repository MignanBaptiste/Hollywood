import json
import networkx as nx

# Q1
def json_vers_nx(chemin):
    graph = nx.Graph()
    with open(chemin, "r") as file:
        for ligne in file:
            ligne = json.loads(file.readline())
            for acteur in ligne["cast"]:
                for acteur2 in ligne["cast"]:
                    if acteur != acteur2:
                        graph.add_edge(acteur, acteur2)
    return graph