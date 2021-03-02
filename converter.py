import networkx as nx 
import json 
from networkx.drawing.nx_agraph import write_dot
from tqdm import tqdm 
import os 

# G=nx.Graph(nx.read_dot(path))

json_file= open('/Users/iqbal/Desktop/query.cyjs')
data = json.load(json_file)

G=nx.Graph()
#"size": n['data']["size"],
nodes=[(n['data']["id"], {"type":n['data']["type"],  "label":n['data']["name"] }) for n in  data['elements']['nodes']]
edges=[(n['data']["source"], n['data']["target"]) for n in  data['elements']['edges']]
#MOTYAPSLR
color={"METABOLIC":"red", "OTHER_RNA":"green","TXNFACTOR":"blue","ANTISENSE_LONG_NONCODING_RNA":"yellow"}
 
G.add_nodes_from(nodes)
G.add_edges_from(edges)

G_org=G.copy()

# for n in tqdm(G_org.nodes()):
#     if G_org.degree(n)<10:
#         G.remove_node(n)
# write_dot(G, "out_no_degree_one.dot")
selected_edges=[]
for n in tqdm(G.nodes()):
    if G.nodes[n]['type'] in color:
        G.nodes[n]['color']=color[G.nodes[n]['type']]
    else:
        G.nodes[n]['color']='white'

    if G.degree(n) > 5:
        selected_edges.append(n)
    # if G.degree(n)==1:
    #     G.nodes[n]['color']='red'
    G.nodes[n]['width']=min( G.degree(n)/15, 1.5)

for e in G.edges():
    G.edges[e]['color']='black'
    if e[0] in selected_edges and e[1] in selected_edges:
        G.edges[e]['color']='blue'
        G.edges[e]['penwidth']=5
        G.edges[e]['splines']='curved'

# nx.set_edge_attributes(G,['gray'] * len(G.edges) )
    
write_dot(G, "out.dot")

os.system("sfdp -Goverlap=prism -Nshape=point -Gbgcolor=black -Goutputorder=edgesfirst -Tsvg out.dot > out.svg")
# sfdp -Goverlap=prism -Tsvg out.dot > out.svg

# sfdp -Goverlap=prism -Nshape=point -Goutputorder=edgesfirst -Gbgcolor=black  -Tsvg out.dot > out.svg