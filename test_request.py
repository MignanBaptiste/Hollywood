import requetes as r
import matplotlib.pyplot as plt
import networkx as nx
import time
import random as rand

# Q1
def test_Q1(chemin):
    t = time.time()
    G = r.json_vers_nx(chemin)
    print(nx.number_of_edges(G))
    print(nx.number_of_nodes(G))
    print(time.time()-t)
    return G

# Q2
def test_Q2(G):
    nb = 1
    for i in range(nb):
        t = time.time()
        act1 = rand.choice(list(G.nodes()))
        act2 = rand.choice(list(G.nodes()))
        print(act1 +"\n" + act2)
        res = r.collaborateurs_communs(G, act1, act2)
        print(res)
        if res != set():
            break
        print(time.time()-t)

# Q3
def test_Q3(G):
    nb = 1
    temps_total1 = 0
    temps_total2 = 0
    for i in range(nb):
        act1 = rand.choice(list(G.nodes()))
        t = time.time()
        k = r.distance_naive(G, "Al Pacino", act1)
        t2 = time.time() - t
        print((k, t2))
        temps_total1 += t2
        t = time.time()
        k = r.distance3(G, "Al Pacino", act1)
        t2 = time.time()-t
        print((k, t2))
        temps_total2 += t2
    print(">>>>>>>>>>>>>>>>>>>>>>>>>")
    print(temps_total1)
    print(temps_total2)
    print(">>>>>>>>>>>>>>>>>>>>>>>>>")

# Q4
def test_Q4(G):
    t = time.time()
    print(r.centralite2(G, "Al Pacino"))
    print(time.time()-t)

    t = time.time()
    print(r.centre_hollywood2(G))
    print(time.time()-t)

    t = time.time()
    print(r.eloignement_max2(G))
    print(time.time()-t)


if __name__ == "__main__":
    chemin = "./data.txt"
    G = test_Q1(chemin)
    test_Q2(G)
    test_Q3(G)
    test_Q4(G)