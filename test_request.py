import requetes as r
import matplotlib.pyplot as plt
import networkx as nx
import time

# Q1
t = time.time()
G = r.json_vers_nx("./data.txt")
print(nx.number_of_edges(G))
print(nx.number_of_nodes(G))
print(time.time()-t)