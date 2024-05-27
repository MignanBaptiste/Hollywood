import requetes as r
import matplotlib.pyplot as plt
import networkx as nx
import time
import random as rand

# Q1
t = time.time()
G = r.json_vers_nx("./data_1000.txt")
print(nx.number_of_edges(G))
print(nx.number_of_nodes(G))
print(time.time()-t)

# Q2
# for i in range(10000):
    # t = time.time()
    # act1 = rand.choice(list(G.nodes()))
    # act2 = rand.choice(list(G.nodes()))
    # print(act1 +"\n" + act2)
    # res = r.collaborateurs_communs(G, act1, act2)
    # print(res)
    # if res != set():
    #     break
    # print(time.time()-t)

# Q3
for i in range(100000):
    t = time.time()
    act1 = rand.choice(list(G.nodes()))
    act2 = rand.choice(list(G.nodes()))
    k = r.distance_naive(G, "Al Pacino", act1)
    if k <= 1:
        print(k)
        print(act1 +"\n" + act2)
        break
    print(time.time()-t)