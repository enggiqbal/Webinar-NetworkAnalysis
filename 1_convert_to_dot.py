import networkx as nx
import os, json
from networkx.drawing.nx_agraph import write_dot
#read json network and save as dot network 
json_file = open('query.cyjs')
data = json.load(json_file)

G = nx.Graph()
for n in data['elements']['nodes']:
    ntype = n['data']["type"]
    if n['data']["type"] == "": ntype = "None"
    G.add_node(n['data']["id"], type=ntype, label=n['data']["name"])

for n in data['elements']['edges']:
    G.add_edge(n['data']["source"], n['data']["target"])

print(nx.info(G))
out_file_name="network.dot"
write_dot(G, out_file_name)
os.system("sfdp -Goverlap=prism -Nshape=point -Goutputorder=edgesfirst -Tsvg "+out_file_name+" -O")