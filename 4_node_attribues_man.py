import networkx as nx 
from networkx.drawing.nx_agraph import write_dot
import pygraphviz as pgv 
import os 
G=nx.Graph(pgv.AGraph("network.dot"))
color={"METABOLIC":"red", "OTHER_RNA":"green","TXNFACTOR":"blue","PRE_TRNA":"yellow"}
#set size of the node based on degrees/neighbors
for n in G.nodes():
    if G.nodes[n]['type'] in color:
        G.nodes[n]['color']=color[G.nodes[n]['type']]
    else:
        G.nodes[n]['color']='black'
    G.nodes[n]['width']=min( G.degree(n)/15, 1.5)

out_file_name="network4.dot"
write_dot(G, out_file_name)
os.system("sfdp -Goverlap=prism -Nshape=point -Goutputorder=edgesfirst -Tsvg "+out_file_name+" -O")