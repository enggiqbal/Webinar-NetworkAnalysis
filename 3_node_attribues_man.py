import networkx as nx 
import os
from networkx.drawing.nx_agraph import write_dot
import pygraphviz as pgv 

G=nx.Graph(pgv.AGraph("network.dot"))

color={"METABOLIC":"red", "OTHER_RNA":"green","TXNFACTOR":"blue","PRE_TRNA":"yellow"}
#Set color on node based on node type
for n in G.nodes():
    if G.nodes[n]['type'] in color:
        G.nodes[n]['color']=color[G.nodes[n]['type']]
    else:
        G.nodes[n]['color']='black'

out_file_name="network3.dot"
write_dot(G, out_file_name)
os.system("sfdp -Goverlap=prism -Nshape=point -Goutputorder=edgesfirst -Tsvg "+out_file_name+" -O")