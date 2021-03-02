import networkx as nx 
from networkx.drawing.nx_agraph import write_dot
import pygraphviz as pgv 
from collections import Counter
import random

G=nx.Graph(pgv.AGraph("network.dot"))
nodes=list(G.nodes())
for n in nodes:
    if G.degree(n)==1:
        G.remove_node(n)

clustering=nx.clustering(G)
C=Counter(clustering.values())
number_of_colors = len(C)
L=list(C.keys())

color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
             for i in range(number_of_colors)]
for n in G.nodes():
    G.nodes[n]['color']=color[L.index(clustering[n])]


write_dot(G, "network12.dot")
