import requetes as r
import matplotlib.pyplot as plt
import networkx as nx

# Q1
fig = plt.figure()
nx.draw(r.json_vers_nx("../data_100.txt"))
fig.savefig("../G.png")
print(r.json_vers_nx("../data_100.txt"))