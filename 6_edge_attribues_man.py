import networkx as nx 
from networkx.drawing.nx_agraph import write_dot
import pygraphviz as pgv 
from collections import Counter
import os 
G=nx.Graph(pgv.AGraph("network.dot"))
color={"METABOLIC":"red", "OTHER_RNA":"green","TXNFACTOR":"blue","PRE_TRNA":"yellow"}

for n in G.nodes():
    if G.nodes[n]['type'] in color:
        G.nodes[n]['color']=color[G.nodes[n]['type']]
    else:
        G.nodes[n]['color']='black'
    G.nodes[n]['width']=min( G.degree(n)/15, 1.5)
#set gray color for other edges
for e in G.edges():
    G.edges[e]['color']='gray'
    if G.nodes[e[0]]['type'] == G.nodes[e[1]]['type']:
        G.edges[e]['color']=G.nodes[e[0]]['color']

out_file_name="network6.dot"
write_dot(G, out_file_name)
os.system("sfdp -Goverlap=prism -Nshape=point -Goutputorder=edgesfirst -Tsvg "+out_file_name+" -O")
