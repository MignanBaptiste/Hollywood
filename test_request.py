import requetes as r
import matplotlib.pyplot as plt
import networkx as nx
import time
import random as rand

# Q1
t = time.time()
G = r.json_vers_nx("./data.txt")
print(nx.number_of_edges(G))
print(nx.number_of_nodes(G))
print(time.time()-t)

# Q2
for i in range(10000):
    t = time.time()
    act1 = rand.choice(list(G.nodes()))
    act2 = rand.choice(list(G.nodes()))
    print(act1 +"\n" + act2)
    res = r.collaborateurs_communs(G, act1, act2)
    print(res)
    if res != []:
        break
    print(time.time()-t)