import requetes as r
import matplotlib.pyplot as plt
import networkx as nx
import time

# Q1
def test_json_vers_nx():
    G = r.json_vers_nx("../data.txt")
    print(nx.number_of_edges(G))
    print(nx.number_of_nodes(G))