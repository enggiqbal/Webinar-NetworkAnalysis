import networkx as nx 
from networkx.drawing.nx_agraph import write_dot
import pygraphviz as pgv 
import os 

G=nx.Graph(pgv.AGraph("network.dot"))
color={"METABOLIC":"red", "OTHER_RNA":"green","TXNFACTOR":"blue","PRE_TRNA":"yellow"}
nodes=list(G.nodes())
#remove node with degree 1 or not interested i.e., not in color list
for n in nodes:
    if G.degree(n)==1 or  G.nodes[n]['type'] not in color: 
        G.remove_node(n)
        continue
    
    G.nodes[n]['color']='black'
    if G.nodes[n]['type'] in color:
        G.nodes[n]['color']=color[G.nodes[n]['type']]

    G.nodes[n]['width']=min( G.degree(n)/15, 1.5)
    
for e in G.edges():
    G.edges[e]['color']='gray'
    if G.nodes[e[0]]['type'] == G.nodes[e[1]]['type']:
        G.edges[e]['color']=G.nodes[e[0]]['color']

out_file_name="network9.dot"
write_dot(G, out_file_name)
os.system("sfdp -Goverlap=prism -Nshape=point -Goutputorder=edgesfirst -Tsvg "+out_file_name+" -O")
os.system("sfdp -Goverlap=prism -Goutputorder=edgesfirst -Tsvg "+out_file_name+" > network9_lbl.dot.svg")

