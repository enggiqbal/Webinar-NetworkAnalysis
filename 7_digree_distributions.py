import networkx as nx 
import pygraphviz as pgv 
from collections import Counter
import matplotlib.pyplot as plt 

G=nx.Graph(pgv.AGraph("network.dot"))
degreeset=[str(G.degree(n)) for n in G.nodes()]
degree_counter=Counter(degreeset)

#ploting degree vs number of nodes
x, y =zip(*degree_counter.most_common())
plt.bar(x,y, align='center')
plt.xlabel("degree")
plt.ylabel("node count")
for index, value in enumerate(y):
    plt.text(index, value, str(value))
plt.show()