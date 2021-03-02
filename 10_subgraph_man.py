import networkx as nx 
from networkx.drawing.nx_agraph import write_dot
import pygraphviz as pgv 
import os
G=nx.Graph(pgv.AGraph("network.dot"))

color={"METABOLIC":"red", "OTHER_RNA":"green","TXNFACTOR":"blue","PRE_TRNA":"yellow"}
nodes=list(G.nodes())
#remove all node with degree less than 4 and have not label
for n in nodes:
    if G.degree(n)<4 or G.nodes[n]['label']=="" : 
        G.remove_node(n)
        continue
    
    G.nodes[n]['color']='black'
    if 'type' in  G.nodes[n] and G.nodes[n]['type'] in color:
        G.nodes[n]['color']=color[G.nodes[n]['type']]
    G.nodes[n]['width']=min( G.degree(n)/15, 1.5)
    
for e in G.edges():
    G.edges[e]['color']='gray'
    if G.nodes[e[0]]['type'] == G.nodes[e[1]]['type']:
        G.edges[e]['color']=G.nodes[e[0]]['color']

out_file_name="network10.dot"
write_dot(G, out_file_name)
os.system("sfdp -Goverlap=prism -Nshape=point -Goutputorder=edgesfirst -Tsvg "+out_file_name+" -O")
# os.system("sfdp -Goverlap=prism -Goutputorder=edgesfirst -Tsvg "+out_file_name+" > network10_lbl.dot.svg")

