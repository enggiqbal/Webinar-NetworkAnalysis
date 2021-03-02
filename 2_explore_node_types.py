import networkx as nx 
import pygraphviz as pgv 
from collections import Counter
import matplotlib.pyplot as plt 
G=nx.Graph(pgv.AGraph("network.dot"))

#explore node types
node_type_values=nx.get_node_attributes(G,"type").values()
node_type_count=Counter(node_type_values)
print(node_type_count.most_common())

#ploting  node type vs node count
node_types, node_count=zip(*node_type_count.most_common())
plt.bar(node_types, node_count, align='center')
plt.xticks(rotation=45, ha="right")
for index, value in enumerate( node_count):
    plt.text(index, value, str(value))
plt.xlabel("Node Type")
plt.ylabel("Node Count")
plt.show()