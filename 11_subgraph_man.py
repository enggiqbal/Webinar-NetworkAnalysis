import networkx as nx 
from networkx.drawing.nx_agraph import write_dot
import pygraphviz as pgv 
import os
G=nx.Graph(pgv.AGraph("network.dot"))
color={"METABOLIC":"red", "OTHER_RNA":"green","TXNFACTOR":"blue","PRE_TRNA":"yellow"}
nodes=list(G.nodes())
selected=[]
for n in nodes:
    if G.degree(n)>3 and G.nodes[n]['label']!="" : 
        selected.append(n)

    G.nodes[n]['color']='black'
    if 'type' in  G.nodes[n] and G.nodes[n]['type'] in color:
        G.nodes[n]['color']=color[G.nodes[n]['type']]
    G.nodes[n]['width']=min( G.degree(n)/15, 1.5)
#highligh interesting subnetwork
for e in G.edges():
    if e[0] in selected and e[1] in selected:
        G.edges[e]['color']='black'
        G.edges[e]['penwidth']=3
    else: 
        G.edges[e]['color']='gray'
        G.edges[e]['penwidth']=0.2

out_file_name="network11.dot"
write_dot(G, out_file_name)
os.system("sfdp -Goverlap=prism -Nshape=point -Goutputorder=edgesfirst -Tsvg "+out_file_name+" -O")
