import networkx as nx 
import pygraphviz as pgv 
G=nx.Graph(pgv.AGraph("network.dot"))

print(nx.info(G)) #Number of nodes: 14394;  Number of edges: 23090; Average degree:   3.2083
print(len(list(nx.connected_components(G)))) #1
print(nx.is_connected(G)) # True
print(nx.diameter(G)) #4
print(nx.average_shortest_path_length(G))# 2.548365263049295
print(nx.center(G)) #['AT1G64390', 'AT2G01023', 'AT3G14850', 'AT3G16510', 'AT5G01250', 'AT5G40450', 'AT5G67640']
print(nx.average_clustering(G)) #0.34426396587423747
print(nx.degree_centrality(G)) # degree centrality for all nodes
